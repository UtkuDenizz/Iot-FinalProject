🏠 Smart Home Project — Business Context Description
1. Project Overview

The Smart Home IoT System is a fully containerized solution that enables users to monitor and control smart devices (temperature sensors, lights, etc.) inside their home.
It includes:

IoT Device (simulated)

MQTT Broker (Mosquitto)

FastAPI Backend

PostgreSQL Database

All modules run inside Docker containers, ensuring scalability, modularity, and real-time communication.
The system demonstrates how IoT devices send sensor data via MQTT, how the backend processes it, and how users control devices remotely.

2. Stakeholders

👤 Homeowner (Primary User) – Monitors and controls IoT devices.

🛠️ System Administrator – Manages configuration and maintenance.

👥 Guest Users – Limited control (e.g., turn lights on/off).

👨‍💻 Developers – Extend system functionality using the API.

3. Use Cases
Use Case	Description	Actors
UC1 – Device Monitoring	View real-time temperature & humidity.	Home User
UC2 – Device Control	Send commands like turning lights on/off.	Home User
UC3 – Automation Rules	System reacts automatically (e.g., fan on at >30°C).	Home User
UC4 – Local Data Storage	Sensor data stored in PostgreSQL for history & analysis.	User
UC5 – Alerts & Notifications	MQTT alerts when safety thresholds are exceeded.	Home User
UC6 – API Access	Developers can add new IoT devices using REST API.	Developer
4. User Stories

✔️ As a home user, I want to monitor temperature and humidity in real time.

✔️ As a home user, I want to remotely control my home lights.

✔️ As a home user, I want to receive alerts when sensor values exceed safe limits.

✔️ As a developer, I want a clear, documented REST API to add new devices.

✔️ As a system owner, I want all data stored locally for reliability and insights.

5. System Overview
🏷️ Components

IoT Layer – Simulated device that generates readings and receives commands.

Communication Layer – MQTT Broker (Mosquitto) enabling fast device/backend messaging.

Backend Layer – FastAPI handling REST API, token auth, MQTT commands, and data processing.

Database Layer – PostgreSQL storing all sensor data.

Frontend/Test Layer – Swagger UI and Postman for interaction.

🔗 Architecture

All services run as separate Docker containers connected through an isolated virtual network: iot_network.

This structure improves isolation, flexibility, and scalability, while supporting real-time IoT communication.

6. Value Proposition

The Smart Home IoT System provides:

⭐ Automation & Control

Remote device control and automatic rule execution.

📊 Data Insights

Real-time & historical monitoring through persistent storage.

🧱 Scalability

Supports adding new sensors or devices easily.

🔌 Local First Design

Works 100% locally — no cloud required.

🎓 Educational Purpose

Demonstrates real-world IoT architecture using:

MQTT

FastAPI

PostgreSQL

Docker Compose

Perfect for teaching or expanding into a full smart home product.

👨‍💻 Authors

Deniz Utku Çelebi, Utku Deniz Duman
Collegium Da Vinci — IoT & Cloud Computing Project