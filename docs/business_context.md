# 🏠 Smart Home – Business Context Description

## 1. Project Overview
The **Smart Home IoT System** provides users with a modern, containerized solution to monitor, control, and automate smart home devices such as lights and temperature sensors.  
The project integrates **IoT devices**, an **MQTT communication layer**, a **FastAPI backend**, and a **PostgreSQL database**, all running locally in **Docker containers** to ensure scalability, modularity, and real-time performance.

The system simulates a realistic IoT ecosystem that demonstrates how devices communicate through MQTT, send data to the backend, and respond to user commands.

---

## 2. Business Goals
- Enhance **comfort and convenience** for home users through automation.
- Improve **energy efficiency** by monitoring temperature and humidity trends.
- Increase **home security** through real-time monitoring and remote control.
- Ensure **data reliability** with persistent local storage.
- Provide a **developer-friendly API** for easy integration of new smart devices.
- Ensure **reliable operation even without external cloud services**.

---

## 3. Use Cases

| Use Case | Description | Actors |
|----------|-------------|--------|
| **UC1 – Device Monitoring** | The user can monitor real-time temperature and humidity data from IoT devices. | Home User |
| **UC2 – Device Control** | The user can send commands (e.g., turn lights on/off) remotely via REST API or MQTT. | Home User |
| **UC3 – Automation Rules** | The system can automatically trigger actions (e.g., turn on the fan when temperature > 30°C). | Home User |
| **UC4 – Local Data Storage** | The backend stores all device data in PostgreSQL for analysis and visualization. | User |
| **UC5 – Alerts & Notifications** | The backend can publish MQTT alerts if sensor values exceed safety thresholds. | Home User |
| **UC6 – API Access** | Developers can extend functionality or connect new IoT devices using the documented FastAPI interface. | Developer |

---

## 4. User Stories
- As a **home user**, I want to **monitor my home's temperature and humidity** to maintain comfort.
- As a **home user**, I want to **turn lights on and off remotely** to save energy and increase convenience.
- As a **home user**, I want to **receive alerts** when sensor readings exceed safe levels.
- As a **developer**, I want to **use a documented REST API** to integrate new IoT devices easily.
- As a **system owner**, I want to **store all sensor data locally** for analysis and reliability.

---

## 5. System Overview
- **IoT Layer:** Simulated devices (Python scripts) that generate and send sensor readings (temperature, humidity) and receive control commands.
- **Communication Layer:** MQTT Broker (**Eclipse Mosquitto**) that enables message exchange between devices and backend.
- **Backend Layer:** **FastAPI** service that exposes REST API endpoints, processes sensor data, and communicates with the MQTT broker.
- **Database Layer:** **PostgreSQL** database used to store and retrieve sensor data for historical tracking and analysis.
- **Frontend Layer:** Swagger UI and Postman Collection for API testing and system interaction.

All components are deployed as separate **Docker containers**, communicating within a shared virtual network (`iot_network`) for seamless integration.

---

## 6. Value Proposition
The **Smart Home IoT Project** offers a lightweight, scalable, and fully containerized environment that provides:
- **Automation and Control:** Remote management of smart devices.
- **Data-Driven Insights:** Real-time monitoring and historical data storage.
- **Scalability:** Modular design for adding new sensors or devices.
- **Local Reliability:** Works independently without requiring external cloud connectivity.
- **Educational Value:** Demonstrates real-world IoT architecture using modern technologies like MQTT, FastAPI, and Docker.

This project represents a foundation for future smart home ecosystems — adaptable for cloud deployment or on-premises operation.

---

👨‍💻 **Author:**  
**Deniz Utku Celebi,Utku Deniz Duman*
Collegium Da Vinci – IoT & Cloud Computing Project  

