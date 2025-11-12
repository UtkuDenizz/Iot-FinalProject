# 🏠 Smart Home IoT System

## 📘 Project Overview
The **Smart Home IoT System** is a cloud-connected solution that allows users to monitor and control home devices such as temperature sensors and lights.  
The project integrates **IoT devices**, an **MQTT broker**, a **FastAPI backend**, and a **PostgreSQL database**, all running in **Docker containers**.

---

## 🧩 System Components

| Component | Description |
|------------|-------------|
| **FastAPI Backend** | Provides REST API endpoints, processes IoT data, and stores it in PostgreSQL. |
| **PostgreSQL Database** | Stores sensor data such as temperature and humidity readings. |
| **MQTT Broker (Mosquitto)** | Handles message communication between IoT devices and the backend. |
| **IoT Device Simulator** | Simulates a smart sensor device that sends temperature and humidity data and can receive control commands. |
| **Postman Collection** | Used to test and verify API endpoints. |

All services run in Docker and communicate through the shared `iot_network`.

---

## ⚙️ Technologies Used
- **Python 3.11**
- **FastAPI**
- **PostgreSQL**
- **Eclipse Mosquitto (MQTT)**
- **paho-mqtt**
- **Docker Compose**

---

## 🧱 System Architecture

### 🗺️ System Context Diagram
![System Context Diagram](docs/System_Context_Diagram.png)

### 🧩 Container Diagram
![Container Diagram](docs/Container_Diagram.png)

---

## 🚀 Setup Guide

```bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/Iot-Final-Project.git
cd Iot-Final-Project

# 2️⃣ Start all containers (API, PostgreSQL, and MQTT broker)
cd api
docker-compose up

# 3️⃣ Access the FastAPI documentation
# Open your browser and go to:
# 👉 http://localhost:8000/docs

# 4️⃣ Run the IoT device simulator
cd ../device
python simple_device.py

# ✅ REST API Endpoints
# -----------------------------------
# Method | Endpoint              | Description
# -----------------------------------
# GET    | /                     | Health check for the API
# POST   | /data                 | Insert new sensor data
# GET    | /data                 | Retrieve stored sensor data
# POST   | /command/{device_id}  | Send command to IoT device via MQTT

# 💾 Database Schema
# -----------------------------------
# Table: sensor_data
#
# Column       | Type              | Description
# -----------------------------------------------
# id           | SERIAL PRIMARY KEY | Unique record ID
# device_id    | VARCHAR(50)        | IoT device identifier
# temperature  | FLOAT              | Temperature reading
# humidity     | FLOAT              | Humidity reading
# timestamp    | TIMESTAMP          | Time of data collection

# 🧭 Business Context
# -----------------------------------
# The Smart Home IoT Project enhances comfort,
# energy efficiency, and security for users through
# automation, real-time monitoring, and cloud data storage.
