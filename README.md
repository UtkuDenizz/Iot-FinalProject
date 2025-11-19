🏠 Smart Home IoT System
📘 Project Overview

The Smart Home IoT System is a fully containerized smart home environment that allows users to monitor and control IoT devices such as temperature/humidity sensors and smart lights.

The system contains:

IoT devices (simulator)

MQTT communication layer

FastAPI backend

PostgreSQL database

All components run inside Docker containers, allowing easy deployment, modularity, and realistic IoT behavior.

🧩 System Components
Component	Description
FastAPI Backend	REST API for device control, user authentication, and sensor data processing.
PostgreSQL Database	Stores all incoming sensor data for long-term tracking.
Mosquitto MQTT Broker	Handles publish/subscribe messaging between devices and backend.
IoT Device Simulator	Python script sending sensor data and receiving commands.
Postman/Swagger UI	Used to test API endpoints easily.

All containers communicate inside the shared iot_network.

⚙️ Technologies Used

Python 3.11

FastAPI

PostgreSQL

Eclipse Mosquitto (MQTT Broker)

paho-mqtt

Docker & Docker Compose

🧱 System Architecture
🗺️ System Context Diagram

🧩 Container Diagram

🚀 Setup Guide
1️⃣ Clone the project
git clone https://github.com/<your-username>/Iot-Final-Project.git
cd Iot-Final-Project

2️⃣ Start all backend services (API + MQTT + Database)
docker compose up -d --build


This starts:

smart_home_api

postgres_db

mqtt-broker

3️⃣ Open the API Documentation
http://localhost:8000/docs


You can test login, send commands, and query device data directly from here.

4️⃣ Run the IoT Device Simulator
cd device
python simple_device.py


The simulator will:

Publish temperature & humidity data to MQTT

Receive commands from the backend (e.g., turn on/off)

📡 API Endpoints Overview
Method	Endpoint	Description
GET	/	API health check
POST	/login	Returns JWT access token
GET	/data	Retrieve stored sensor data (requires token)
POST	/data	Insert sensor data manually (requires token)
POST	/command/{device_id}	Sends a control command to device via MQTT
💾 Database Schema
Table: sensor_data
Column	Type	Description
id	SERIAL PRIMARY KEY	Unique row ID
device_id	VARCHAR(50)	Device identifier
temperature	FLOAT	Temperature value
humidity	FLOAT	Humidity value
timestamp	TIMESTAMP	Date/time of reading
🧭 Business Context Summary

The Smart Home IoT System aims to improve daily comfort and efficiency by providing:

Real-time monitoring

Remote device control

Local and reliable data storage

Easy expandability for additional IoT devices

A realistic IoT architecture using modern technologies

The system is ideal for educational use, demonstrating how MQTT, Docker, and FastAPI work together in a real IoT environment.

👨‍💻 Authors

Deniz Utku Çelebi
Utku Deniz Duman
Collegium Da Vinci – IoT & Cloud Computing Project
