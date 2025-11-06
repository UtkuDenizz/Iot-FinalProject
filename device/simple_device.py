import paho.mqtt.client as mqtt
import time
import random
import json

# MQTT broker settings
BROKER = "localhost"
PORT = 1883
TOPIC = "smart_home/sensor_data"
DEVICE_ID = "device_001"

# Callback when connected to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

# Callback when a message is received from the broker
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# Create MQTT client instance
client = mqtt.Client(client_id=DEVICE_ID)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Start background network loop
client.loop_start()

try:
    while True:
        # Generate example sensor data (temperature, humidity, etc.)
        data = {
            "device_id": DEVICE_ID,
            "temperature": round(random.uniform(20, 30), 2),
            "humidity": round(random.uniform(40, 60), 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        # Convert to JSON and publish to topic
        payload = json.dumps(data)
        client.publish(TOPIC, payload)
        print(f"Sent: {payload}")

        time.sleep(5)  # send every 5 seconds

except KeyboardInterrupt:
    print("Simulation stopped.")
    client.loop_stop()
    client.disconnect()
