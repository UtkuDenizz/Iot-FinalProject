from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta
import psycopg2
from psycopg2.extras import RealDictCursor
import json
import paho.mqtt.client as mqtt


# ============================================================
# 🔧 SETTINGS
# ============================================================
SECRET_KEY = "MY_SUPER_SECRET"
ALGORITHM = "HS256"

DB_HOST = "smarthomepostgres.postgres.database.azure.com"
DB_NAME = "postgres"
DB_USER = "iot_user"
DB_PASS = "CoffeeLover@77"
DB_PORT = 5432

MQTT_BROKER = "4.233.74.143"   # Azure VM MQTT
MQTT_PORT = 1883


# ============================================================
# 🗄 DATABASE CONNECTION
# ============================================================
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
        sslmode="require"
    )


def initialize_database():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sensor_data (
                id SERIAL PRIMARY KEY,
                device_id VARCHAR(255),
                temperature FLOAT,
                humidity FLOAT,
                timestamp VARCHAR(255)
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Database initialized.")
    except Exception as e:
        print("❌ Database initialization failed:", e)


initialize_database()


# ============================================================
# 🔐 TOKEN MANAGEMENT
# ============================================================
security = HTTPBearer()


def create_token(username: str):
    expire_time = datetime.utcnow() + timedelta(hours=2)
    payload = {"sub": username, "exp": expire_time}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid or expired token")


# ============================================================
# 📦 MODELS
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
# 📡 MQTT SETUP
# ============================================================
def on_mqtt_message(client, userdata, msg):
    """Save incoming MQTT sensor data to database."""
    try:
        data = json.loads(msg.payload.decode())
        print("📥 MQTT RECEIVED:", data)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO sensor_data (device_id, temperature, humidity, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (
            data.get("device_id"),
            data.get("temperature"),
            data.get("humidity"),
            data.get("timestamp")
        ))
        conn.commit()
        cur.close()
        conn.close()

        print("✅ Data saved to DB")

    except Exception as e:
        print("❌ MQTT ERROR:", e)


def on_mqtt_connect(client, userdata, flags, rc):
    print("🔗 API connected to MQTT broker:", MQTT_BROKER)
    client.subscribe("smart_home/sensor_data")
    print("📡 Subscribed to smart_home/sensor_data")


mqtt_client = mqtt.Client(client_id="api_backend", protocol=mqtt.MQTTv311)
mqtt_client.on_message = on_mqtt_message
mqtt_client.on_connect = on_mqtt_connect

try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()
    print("✅ MQTT connecting...")
except Exception as e:
    print("⚠️ MQTT connection failed:", e)


# ============================================================
# 🌐 FASTAPI APP
# ============================================================
app = FastAPI(title="Smart Home IoT API")


@app.get("/")
def home():
    return {"message": "Smart Home IoT API is running 🚀"}


# ============================================================
# 🔑 LOGIN
# ============================================================
@app.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "admin123":
        return {
            "access_token": create_token(data.username),
            "token_type": "bearer"
        }
    raise HTTPException(status_code=401, detail="Invalid username or password")


# ============================================================
# 📊 GET DATA
# ============================================================
@app.get("/data", dependencies=[Depends(verify_token)])
def get_data():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM sensor_data ORDER BY id DESC")
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================
# 📝 MANUAL INSERT
# ============================================================
@app.post("/data", dependencies=[Depends(verify_token)])
def insert_data(data: SensorData):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO sensor_data (device_id, temperature, humidity, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (data.device_id, data.temperature, data.humidity, data.timestamp))
        conn.commit()
        cur.close()
        conn.close()
        return {"status": "saved"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================
# 📡 SEND COMMAND TO DEVICE
# ============================================================
@app.post("/command/{device_id}", dependencies=[Depends(verify_token)])
def send_command(device_id: str, cmd: CommandPayload):
    topic = f"smart_home/commands/{device_id}"
    message = json.dumps({"device_id": device_id, "command": cmd.command})

    try:
        mqtt_client.publish(topic, message)
        print("📤 COMMAND SENT:", message)
        return {"status": "sent", "topic": topic, "message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
