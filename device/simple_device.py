import paho.mqtt.client as mqtt
import time
import random
import json
import os

# ================================
# 🔧 Configuration
# ================================
BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", 1883))
DATA_TOPIC = "smart_home/sensor_data"
DEVICE_ID = os.getenv("DEVICE_ID", "device_001")
COMMAND_TOPIC = f"smart_home/commands/{DEVICE_ID}"

# ================================
# 🔌 MQTT Callbacks
# ================================
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"✅ Connected to MQTT Broker: {BROKER}:{PORT}")
        # Subscribe to command topic (for cloud-to-device messages)
        client.subscribe(COMMAND_TOPIC)
        print(f"📡 Subscribed to command topic: {COMMAND_TOPIC}")
    else:
        print(f"⚠️ Connection failed with code {rc}")

def on_message(client, userdata, msg):
    print(f"📩 Received message on {msg.topic}: {msg.payload.decode()}")

    # Example of how a command might be handled locally
    try:
        command_data = json.loads(msg.payload.decode())
        command = command_data.get("command")

        if command == "light_on":
            print("💡 Turning ON the light.")
        elif command == "light_off":
            print("💤 Turning OFF the light.")
        elif command == "alert":
            print("🚨 Alert triggered!")
        else:
            print(f"⚙️ Unknown command: {command}")
    except json.JSONDecodeError:
        print("⚠️ Received non-JSON command message.")

# ================================
# 📡 MQTT Setup
# ================================
client = mqtt.Client(client_id=DEVICE_ID)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

# ================================
# 🌡️ Sensor Data Simulation
# ================================
try:
    while True:
        data = {
            "device_id": DEVICE_ID,
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(40, 60), 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        payload = json.dumps(data)
        client.publish(DATA_TOPIC, payload)
        print(f"📤 Sent sensor data: {payload}")
        time.sleep(5)

except KeyboardInterrupt:
    print("🛑 Simulation stopped by user.")
finally:
    client.loop_stop()
    client.disconnect()
    print("🔌 Disconnected from broker.")
