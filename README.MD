🏠 Smart Home IoT System
IoT & Cloud Computing Final Project – Collegium Da Vinci

A fully functional cloud-enabled Smart Home IoT System designed for real-time monitoring and remote control of devices.
The project integrates:

IoT device simulation

MQTT messaging

Cloud-hosted FastAPI backend

Azure PostgreSQL database

Swagger & Postman testing interfaces

The backend runs on Azure App Service, the MQTT Broker on Azure VM, and all data is securely stored in Azure PostgreSQL.

🚀 Project Overview
✔ IoT Device Simulator

Sends temperature & humidity data every 5 seconds

Receives device commands (light_on, light_off) via MQTT

✔ MQTT Broker (Mosquitto on Azure VM)

Handles all IoT messaging

API subscribes to sensor data

Device simulator subscribes to commands

✔ Cloud Backend — FastAPI (Azure App Service)

REST API for device control & data management

Publishes MQTT commands

JWT authentication

Saves all sensor data into Azure PostgreSQL

✔ Azure PostgreSQL Flexible Server

Stores all sensor readings

SSL-secured database connection

Accessible only through API

✔ Swagger API Documentation (Cloud)

🔗 https://smart-home-api-fjegf4a9hce4fwcz.francecentral-01.azurewebsites.net/docs

✔ Postman Collection

Used to test:

Login

Retrieve data

Add data manually

Send MQTT commands

🧱 System Architecture (High-Level Overview)
IoT Device → MQTT Broker (Azure VM) → Cloud API (Azure App Service) → Azure PostgreSQL

🖥 IoT Device Simulator

Publishes sensor data → smart_home/sensor_data

Subscribes to → smart_home/commands/device_001

☁ MQTT Broker (Azure VM)

Routes data between devices and backend

🌐 FastAPI Backend (Cloud)

Exposes REST endpoints

Handles JWT auth

Saves incoming MQTT data

Sends commands to devices

🗄 Azure PostgreSQL

Stores all sensor data in sensor_data table

🧩 C4 Architecture Diagrams

✔ System Context Diagram
✔ Container Diagram

Both diagrams are included in the repository and document how cloud, IoT, and software layers interact.

🔐 Authentication

The API uses JWT-based authentication.

Login
POST /login
{
  "username": "admin",
  "password": "admin123"
}

Use the token in all protected endpoints:
Authorization: Bearer <token>

📡 Main API Endpoints
Method	Endpoint	Description
GET	/	Health check
POST	/login	Obtain JWT token
GET	/data	Get all sensor data
POST	/data	Insert data manually
POST	/command/{device_id}	Send MQTT command

Full docs:
🔗 https://smart-home-api-fjegf4a9hce4fwcz.francecentral-01.azurewebsites.net/docs

🖥️ Running the Device Simulator

Open terminal:

cd device
python simple_device.py


The device will:

Publish sensor data

Listen for MQTT commands

Send data to the cloud API

Example output:

[MQTT PUBLISHED] {temperature: 24.8, humidity: 55.1}
[API] 200 OK
[COMMAND RECEIVED] light_on

🗄 Database Schema (Azure PostgreSQL)

Table: sensor_data

Column	Type	Description
id	SERIAL PRIMARY KEY	Unique row ID
device_id	VARCHAR	Device identifier
temperature	FLOAT	Temperature reading
humidity	FLOAT	Humidity reading
timestamp	TIMESTAMP	Time of reading
📬 Postman Collection

Included as:
📁 postman/SmartHome.postman_collection.json

Collection includes:

Login request

Retrieve sensor data

Insert manual data

Send MQTT commands

🧭 Business Context & User Stories
Target Users

Smart home owners

Developers

System administrators

User Stories

1️⃣ As a user, I want to monitor real-time sensor updates so I can understand conditions at home.
2️⃣ As a user, I want to control home devices remotely so I can turn lights on/off from anywhere.
3️⃣ As a business owner, I want historical data stored so I can analyze trends.
4️⃣ As a developer, I want clear API documentation for integrations.

💰 Cost Calculation (Task Completed)

The repository includes:

📄 cost_calculation.md
→ Contains estimated Azure cost for 1000 devices and 300 users, using:

Azure App Service

Azure VM (MQTT Broker)

Azure PostgreSQL

Outbound network traffic

🧪 Testing Tools

✔ Cloud Swagger UI
✔ Postman
✔ IoT device simulator (Python)

👨‍💻 Authors

Deniz Utku Çelebi
Utku Deniz Duman
Collegium Da Vinci – IoT & Cloud Computing Project (2025)