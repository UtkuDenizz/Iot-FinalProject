from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
import psycopg2
from psycopg2.extras import RealDictCursor
import os
import json
import paho.mqtt.client as mqtt

# ============================================================
# 🔧 AYARLAR
# ============================================================
SECRET_KEY = "MY_SUPER_SECRET"       # Token gizli anahtarı
ALGORITHM = "HS256"                  # Şifreleme yöntemi

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "iot_data")
DB_USER = os.getenv("DB_USER", "iot_user")
DB_PASS = os.getenv("DB_PASS", "iot_password")

MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

# ============================================================
# 🗄️ VERİTABANI BAĞLANTISI
# ============================================================
def get_db_connection():
    """Veritabanına bağlanır ve connection döner."""
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

# ============================================================
# 🔐 TOKEN OLUŞTURMA ve DOĞRULAMA
# ============================================================
security = HTTPBearer()

def create_token(username: str):
    """Kullanıcı giriş yaptığında JWT token üretir."""
    expire_time = datetime.utcnow() + timedelta(hours=2)
    payload = {"sub": username, "exp": expire_time}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Gönderilen token geçerli mi kontrol eder."""
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=403, detail="Token geçersiz veya süresi dolmuş.")

# ============================================================
# 📦 VERİ MODELLERİ
# ============================================================
class LoginRequest(BaseModel):
    username: str
    password: str

class SensorData(BaseModel):
    device_id: str
    temperature: float
    humidity: float
    timestamp: str

class CommandPayload(BaseModel):
    command: str

# ============================================================
# 📡 MQTT FONKSİYONLARI
# ============================================================
def on_mqtt_message(client, userdata, msg):
    """Cihazdan gelen sensör verilerini veritabanına kaydeder."""
    try:
        data = json.loads(msg.payload.decode())

        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO sensor_data (device_id, temperature, humidity, timestamp)
                    VALUES (%s, %s, %s, %s)
                """, (
                    data.get("device_id"),
                    data.get("temperature"),
                    data.get("humidity"),
                    data.get("timestamp"),
                ))
                conn.commit()

        print(f"📥 Kaydedildi: {data}")

    except Exception as e:
        print(f"❌ MQTT Hatası: {e}")


# MQTT BAĞLANTI
mqtt_client = mqtt.Client(client_id="api_backend", protocol=mqtt.MQTTv311)
mqtt_client.on_message = on_mqtt_message

try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.subscribe("smart_home/sensor_data")
    mqtt_client.loop_start()
    print("✅ MQTT Bağlandı ve dinlemeye başladı.")
except:
    print("⚠️ MQTT bağlantısı başarısız.")

# ============================================================
# 🌐 FASTAPI UYGULAMASI
# ============================================================
app = FastAPI(title="Smart Home IoT API")

@app.get("/")
def home():
    return {"message": "Smart Home IoT API çalışıyor 🚀"}

# ============================================================
# 🔑 LOGIN
# ============================================================
@app.post("/login")
def login(data: LoginRequest):
    """Basit kullanıcı girişi (admin / admin123)."""
    if data.username == "admin" and data.password == "admin123":
        return {"access_token": create_token(data.username), "token_type": "bearer"}

    raise HTTPException(status_code=401, detail="Kullanıcı adı veya şifre hatalı.")

# ============================================================
# 📊 TÜM SENSOR VERİLERİNİ GETİR
# ============================================================
@app.get("/data", dependencies=[Depends(verify_token)])
def get_data():
    """Veritabanındaki tüm sensör verilerini döner."""
    try:
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM sensor_data ORDER BY id DESC")
                return cur.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================
# 📝 MANUEL VERİ EKLEME
# ============================================================
@app.post("/data", dependencies=[Depends(verify_token)])
def insert_data(data: SensorData):
    """Elle veri eklemek için kullanılır."""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO sensor_data (device_id, temperature, humidity, timestamp)
                    VALUES (%s, %s, %s, %s)
                """, (data.device_id, data.temperature, data.humidity, data.timestamp))
                conn.commit()

        return {"status": "saved"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================
# 📡 CİHAZA KOMUT GÖNDER
# ============================================================
@app.post("/command/{device_id}", dependencies=[Depends(verify_token)])
def send_command(device_id: str, cmd: CommandPayload):
    """Belirli bir cihaza MQTT ile komut gönderir."""
    topic = f"smart_home/commands/{device_id}"
    message = json.dumps({"device_id": device_id, "command": cmd.command})

    try:
        mqtt_client.publish(topic, message)
        return {"status": "sent", "topic": topic, "message": message}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
