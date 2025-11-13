import paho.mqtt.client as mqtt
import time
import random
import json
import os

BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", 1883))
DEVICE_ID = os.getenv("DEVICE_ID", "device_001")

DATA_TOPIC = "smart_home/sensor_data"
COMMAND_TOPIC = f"smart_home/commands/{DEVICE_ID}"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT Broker: {BROKER}:{PORT}")
        client.subscribe(COMMAND_TOPIC)
    else:
        print("Failed to connect:", rc)

def on_message(client, userdata, msg):
    print(f"Command received: {msg.payload.decode()}")

# FIX HERE (NO callback_api_version)
client = mqtt.Client(client_id=DEVICE_ID, protocol=mqtt.MQTTv311)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

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
        print(f"Sent data: {payload}")

        time.sleep(5)

except KeyboardInterrupt:
    print("Stopped")

finally:
    client.loop_stop()
    client.disconnect()
