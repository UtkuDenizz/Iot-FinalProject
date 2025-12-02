import time
import random
import json
import requests
import paho.mqtt.client as mqtt
from datetime import datetime

# =====================================================
# DEVICE SETTINGS
# =====================================================
DEVICE_ID = "device_001"
API_URL = "https://smart-home-api-fjegf4a9hce4fwcz.francecentral-01.azurewebsites.net"
LOGIN_URL = f"{API_URL}/login"
DATA_URL = f"{API_URL}/data"
MQTT_BROKER = "4.233.74.143"
MQTT_PORT = 1883

COMMAND_TOPIC = f"smart_home/commands/{DEVICE_ID}"
SENSOR_TOPIC = "smart_home/sensor_data"


# =====================================================
# AUTH: Login to API and get token
# =====================================================
def get_jwt_token():
    try:
        response = requests.post(LOGIN_URL, json={"username": "admin", "password": "admin123"})
        token = response.json().get("access_token")
        print("[AUTH] Token acquired:", token[:15], "...")
        return token
    except Exception as e:
        print("[AUTH ERROR]", e)
        return None


jwt_token = get_jwt_token()


# =====================================================
# MQTT CALLBACKS
# =====================================================

def on_connect(client, userdata, flags, rc):
    print(f"[INFO] Connected to MQTT Broker {MQTT_BROKER} with result code {rc}")

    # Subscribe burada yapılmalı!
    client.subscribe(COMMAND_TOPIC)
    print(f"[INFO] Subscribed to command topic: {COMMAND_TOPIC}")


def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"\n💡 [MESSAGE RECEIVED] Topic: {msg.topic} | Payload: {payload}")

        # Eğer komut JSON formatında ise parse et
        data = json.loads(payload)
        command = data.get("command")

        if command == "light_on":
            print("👉 ACTION: LIGHT TURNED ON")
        elif command == "light_off":
            print("👉 ACTION: LIGHT TURNED OFF")
        else:
            print("⚠ Unknown command:", command)

    except Exception as e:
        print("[MESSAGE ERROR]", e)


# MQTT CLIENT
client = mqtt.Client(client_id=DEVICE_ID, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

print(f"[INFO] Device simulator started (ID={DEVICE_ID})")
print(f"[INFO] Waiting for commands on topic: {COMMAND_TOPIC}")


# =====================================================
# SENSOR DATA GENERATOR
# =====================================================
def generate_sensor_data():
    return {
        "device_id": DEVICE_ID,
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }


# =====================================================
# MAIN LOOP
# =====================================================
while True:
    data = generate_sensor_data()

    # MQTT publish
    client.publish(SENSOR_TOPIC, json.dumps(data))
    print("[MQTT PUBLISHED]", data)

    # Send to API
    try:
        headers = {"Authorization": f"Bearer {jwt_token}"}
        r = requests.post(DATA_URL, json=data, headers=headers)
        print("[API]", r.status_code, r.text)
    except Exception as e:
        print("[API ERROR]", e)

    time.sleep(5)
