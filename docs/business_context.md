🏠 Smart Home – Business Context Description (Final Version)
1. Project Overview

The Smart Home IoT System is a containerized solution that allows users to monitor and control smart home devices such as temperature sensors and lights.
The project includes IoT devices, an MQTT broker, a FastAPI backend, and a PostgreSQL database, all running inside Docker containers to ensure modularity, scalability, and real-time communication.

The system demonstrates how IoT devices communicate through MQTT, send sensor data to the backend, and respond to commands from users.

2. Business Goals

Improve comfort and convenience through remote control and automation.

Increase energy efficiency by monitoring temperature and humidity values.

Enhance home safety via real-time alerts and sensor monitoring.

Provide stable data storage for historical and analytical purposes.

Offer a simple and extendable API for adding new IoT devices.

Ensure local operation, without depending on external cloud services.

3. Use Cases
Use Case	Description	Actors
UC1 – Device Monitoring	Users can monitor real-time temperature and humidity from IoT devices.	Home User
UC2 – Device Control	Users send control commands (e.g., turn lights on/off) through REST API or MQTT.	Home User
UC3 – Automation Rules	System can trigger automatic actions (e.g., turn on fan when temperature > 30°C).	Home User
UC4 – Local Data Storage	All sensor data is saved to PostgreSQL for later analysis or visualization.	User
UC5 – Alerts & Notifications	System can publish alerts over MQTT if values exceed safety limits.	Home User
UC6 – API Access	Developers can integrate new IoT devices using FastAPI endpoints.	Developer
4. User Stories

As a home user, I want to monitor temperature and humidity so I can keep my home comfortable.

As a home user, I want to control lights remotely to save energy and improve convenience.

As a home user, I want to receive alerts when values exceed safe limits.

As a developer, I want to use a documented REST API to integrate new sensors or devices.

As a system owner, I want to store sensor data locally for reliability and analysis.

5. System Overview

IoT Layer: Simulated Python device scripts that generate temperature/humidity readings and handle incoming commands.

Communication Layer: MQTT Broker (Eclipse Mosquitto) enabling real-time device–backend communication.

Backend Layer: FastAPI service providing REST endpoints, processing device data, and publishing MQTT commands.

Database Layer: PostgreSQL storing all sensor records for historical use.

Frontend/Test Layer: Swagger UI and Postman collections allowing easy interaction with the system.

All these components run as separate Docker containers, connected using a dedicated iot_network to ensure secure and isolated communication.

6. Value Proposition

The Smart Home IoT Project provides a realistic, lightweight, and modular IoT environment. It offers:

Automation & Control: Remote and automatic device management.

Data Insights: Real-time monitoring with persistent storage.

Scalability: Easy integration of additional IoT devices.

Local Operation: Fully functional without cloud dependency.

Educational Benefit: Clear demonstration of modern IoT architecture using MQTT, FastAPI, PostgreSQL, and Docker.

This system serves as a strong base for real smart-home applications, suitable for both local and future cloud deployments.

👨‍💻 Authors:
Deniz Utku Çelebi, Utku Deniz Duman
Collegium Da Vinci – IoT & Cloud Computing Project