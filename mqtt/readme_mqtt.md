# Task #3 - MQTT Broker Service

This task implements the **MQTT broker infrastructure** to enable data communication between IoT devices and the backend.

**Infrastructure Details:**
- MQTT broker: Mosquitto, running on Azure VM or locally
- Device simulator: `device/simple_device.py` sends data to the broker
- Data sent: `device_id`, `temperature`, `humidity`, `timestamp`
- Backend integration: The FastAPI application subscribes to the broker, receives messages, and stores them in the `postgres` database
- Command sending: Backend can send commands to devices via `/command/{device_id}` endpoint using MQTT topics
- Broker configuration: Defined in `mqtt/mosquitto.conf`
- Data flow: Device → MQTT broker → Backend → Database

**Usage:**
1. Start the MQTT broker (`mosquitto -c mosquitto.conf`)
2. Run `simple_device.py` to start sending data
3. Run the backend FastAPI server (`uvicorn api.main:app --reload`)
4. Incoming data is stored in the `sensor_data` table and can be accessed via the REST API

**Summary:**
Task #3 uses a VM or local MQTT broker to successfully handle communication between the IoT device simulator and the backend, storing data in the cloud database.