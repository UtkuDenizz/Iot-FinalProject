# 🏠 Smart Home Project — Business Context Description

## 1. Project Overview
The **Smart Home System** aims to provide users with an easy way to monitor and control their home environment using connected devices such as lights, temperature sensors, and smart plugs.

The goal is to increase **comfort, energy efficiency, and security** through automation and remote access via a mobile or web interface.

---

## 2. Stakeholders
- **Homeowner (Primary User):** Controls and monitors home devices.
- **System Administrator:** Manages configuration and maintenance.
- **Guest Users:** Limited access (e.g., turning lights on/off).

---

## 3. Use Cases

| Use Case ID | Title | Description | Actor | Precondition | Outcome |
|--------------|--------|-------------|--------|---------------|----------|
| UC1 | Turn on/off lights | User turns lights on or off via the app | Homeowner | Device connected | Light status updated |
| UC2 | Adjust temperature | User changes thermostat setting remotely | Homeowner | Sensor connected | Room temperature adjusts |
| UC3 | Security alert | System notifies user of unusual movement | System | Sensors active | Notification sent |
| UC4 | Energy monitoring | User checks daily energy consumption | Homeowner | Devices recording data | Report displayed |

---

## 4. User Stories

1. As a homeowner, I want to turn my lights on and off remotely so I can make it look like someone is home when I’m away.  
2. As a user, I want to see the current temperature and adjust it to stay comfortable.  
3. As a user, I want to receive alerts when motion is detected for security.  
4. As an admin, I want to add and remove devices to maintain the system.

---

## 5. Non-Functional Requirements
- **Usability:** Simple, intuitive interface  
- **Security:** Encrypted communication  
- **Scalability:** Easy to add more devices  
- **Reliability:** Continues operating even if one device fails

---

## 6. Future Enhancements
- Voice control (Alexa, Google Home)
- AI-based automation
- Energy-saving recommendations

---

## 7. Tools and Technologies
- **Backend:** Python (Flask / FastAPI)
- **Frontend:** React.js / HTML-CSS
- **Database:** SQLite / Firebase
- **Hardware (optional):** ESP32 / Raspberry Pi / Arduino
