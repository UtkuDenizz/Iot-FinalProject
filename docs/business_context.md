🏠 Smart Home IoT System — Business Context (Cloud Version)
1. Project Overview

The Smart Home IoT System is a cloud-based IoT architecture enabling real-time monitoring and remote control of smart home devices such as sensors and smart lights.

The system operates using a combination of Azure cloud services, MQTT messaging, and a FastAPI backend deployed with Docker containers.

🔧 System Components
Component	Platform	Purpose
IoT Device Simulator	Local Python script	Sends sensor data & receives MQTT commands
MQTT Broker (Mosquitto)	Azure Virtual Machine	Handles real-time publish/subscribe communication
FastAPI Backend (Docker)	Azure Web App for Containers	REST API, authentication, command publishing
PostgreSQL Database	Azure Database for PostgreSQL	Persistent cloud data storage
Swagger UI	Built into FastAPI	Cloud interface to test all API endpoints

This system represents a realistic IoT cloud pipeline where devices communicate through MQTT, data flows into a cloud backend, and users interact from anywhere.

2. Stakeholders
👤 Homeowner (Primary User)

Monitors sensor values and controls home devices via the cloud.

🛠️ System Administrator

Maintains Azure resources and ensures reliability, performance, and uptime.

👥 Guest Users

Limited access features such as toggling smart lights.

👨‍💻 Developers / Integrators

Add new IoT devices or integrate external applications via REST API.

3. Use Cases
Use Case	Description	Actor
UC1 – Device Monitoring	View real-time sensor data	Home User
UC2 – Smart Device Control	Send commands like light_on / light_off	Home User
UC3 – Cloud Automation Rules	Auto-trigger actions (e.g., >30°C → fan on)	Home User / Admin
UC4 – Cloud Storage	Persist sensor readings in Azure PostgreSQL	System
UC5 – Alerts & Notifications	MQTT alerts for unsafe values	User
UC6 – API Extensibility	Add new endpoints or devices easily	Developer
UC7 – Remote Accessibility	System usable from anywhere in the world	All
4. User Stories

✔ As a home user, I want to monitor temperature and humidity remotely, so that I can track home conditions in real time.

✔ As a home user, I want to control devices from anywhere, so that I can manage my home while away.

✔ As a user, I want to see immediate feedback, so that I know device state instantly.

✔ As a developer, I want an API with JWT authentication, so that integrations remain secure.

✔ As a system owner, I need cloud storage for historical data analysis.

✔ As an IoT integrator, I require MQTT communication for reliable device interaction.

5. System Architecture (Cloud-Based Final Version)
🔌 IoT Device Layer

Python-based device simulator that:

Publishes sensor readings every 5 seconds

Subscribes to MQTT command topics

Executes actions (e.g., turning lights on/off)

☁️ MQTT Communication Layer (Azure VM)

Mosquitto Broker hosted on an Azure Linux VM

Manages device communication in real time

Acts as the messaging backbone of the entire IoT system

🌐 Backend Layer — FastAPI on Azure

Running inside Azure Web App for Containers:

Endpoints include:

POST /login → JWT token generation

GET /data → Retrieve sensor data

POST /data → Save sensor readings

POST /command/{device_id} → Send MQTT commands

Also:

Subscribes to MQTT sensor topic

Saves incoming messages directly to PostgreSQL

🗄️ Database Layer — Azure PostgreSQL

Stores:

Device ID

Temperature

Humidity

Timestamp

Supports long-term analytics and monitoring.

🧪 Interaction Layer

Swagger UI included for cloud-based testing

Postman Collection for automated validation

Device Terminal shows real-time commands & data

6. Value Proposition
⭐ Full Cloud IoT Pipeline

Covers every step:

Device → MQTT Broker → Cloud API → PostgreSQL → User Interface

🔐 Secure & Production-Oriented

JWT authentication

Cloud VM firewall configuration

Scalable API hosting

📊 Real-Time & Historical Insights

Live readings via MQTT

Persistent sensor logs stored in Azure DB

🔌 Remote Smart Home Control

Control devices from anywhere in the world through the API.

🎓 Educational Excellence

Demonstrates:

MQTT fundamentals

Cloud VM deployments

Dockerized API hosting

Database management in Azure

Real IoT system behavior

Perfect for IoT & Cloud Computing coursework and real-world prototypes.

👨‍💻 Authors

Deniz Utku Çelebi
Utku Deniz Duman
Collegium Da Vinci — IoT & Cloud Computing Final Project (2025)