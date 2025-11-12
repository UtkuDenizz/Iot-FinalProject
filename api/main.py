from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime
import paho.mqtt.client as mqtt
import json

"""
Smart Home IoT API
------------------
Handles sensor data from IoT devices via MQTT and stores it in PostgreSQL.
Provides REST endpoints for data access and device commands.
"""

app = FastAPI(title="Smart Home IoT API")

# ==========================
# 🔧 Configuration
# ==========================
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "iot_data")
DB_USER = os.getenv("DB_USER", "iot_user")
DB_PASS = os.getenv("DB_PASS", "iot_password")

MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

# ==========================
# 🔌 MQTT Client Setup
# ==========================
mqtt_client = mqtt.Client()
mqtt_client.will_set("smart_home/status", json.dumps({"status": "disconnected"}))

try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()
    print(f"✅ Connected to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}")
except Exception as e:
    print(f"⚠️ MQTT connection failed: {e}")

# ==========================
# 📦 Data Models
# ==========================
class SensorData(BaseModel):
    device_id: str
    temperature: float
    humidity: float
    timestamp: datetime = datetime.utcnow()

class CommandPayload(BaseModel):
    command: str

# ==========================
# 🗄️ Database Connection
# ==========================
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

# ==========================
# 🌐 API Endpoints
# ==========================
@app.get("/")
def root():
    return {"message": "Smart Home IoT API is running"}

@app.post("/data")
def insert_data(data: SensorData):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO sensor_data (device_id, temperature, humidity, timestamp)
                    VALUES (%s, %s, %s, %s)
                """, (data.device_id, data.temperature, data.humidity, data.timestamp))
                conn.commit()
                mqtt_payload = json.dumps(data.dict(), default=str)
                mqtt_client.publish("smart_home/sensor_data", mqtt_payload)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data")
def get_all_data():
    try:
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM sensor_data ORDER BY id DESC")
                rows = cur.fetchall()
                return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/command/{device_id}")
def send_command(device_id: str, payload: CommandPayload):
    topic = f"smart_home/commands/{device_id}"
    message = json.dumps({"device_id": device_id, "command": payload.command})
    try:
        mqtt_client.publish(topic, message)
        return {"status": "command sent", "topic": topic, "message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send command: {e}")
