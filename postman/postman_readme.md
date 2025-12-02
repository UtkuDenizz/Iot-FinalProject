# Smart Home IoT API - Postman Collection

## Overview
This Postman collection is used to test the **Smart Home IoT API**. It includes all endpoints for sending and retrieving sensor data, as well as sending commands to IoT devices. Endpoints included: Check API Status (`GET /`), Insert Sensor Data (`POST /data`), Get Sensor Data (`GET /data`), Send Command to Device (`POST /command/{device_id}`).

## Setup

### 1. Import the collection
Open Postman, click on **Import → Link or File**, and use the shared collection link:
[Smart Home IoT API Postman Collection](https://dcelebi-6074de12-1034402.postman.co/workspace/Deniz-Celebi's-Workspace~3e437c81-5e29-49e6-8622-39dfb4d7b604/collection/50462737-d3643173-6a94-4143-bf4e-eff09cd57920?action=share&creator=50462737&active-environment=50462737-519f4aee-3dc6-40dd-8794-fe168bd86f79)

### 2. Set Environment Variables
`base_url`: The URL where your backend is running (e.g., `https://smart-home-api-fjegf4a9hce4fwcz.francecentral-01.azurewebsites.net/docs#/`)
`jwt_token`: The JWT token obtained from the login endpoint (`POST /login`)

## Using the Collection

### 1. Check API Status
Method: GET, URL: `{{base_url}}/`
Purpose: Verify backend is running
Headers: None
Response: Message confirming API is online

### 2. Insert Sensor Data
Method: POST, URL: `{{base_url}}/data`
Purpose: Insert new sensor readings
Headers: Authorization: `Bearer {{jwt_token}}`, Content-Type: `application/json`
Body example:
```json
{
  "device_id": "device_001",
  "temperature": 24.5,
  "humidity": 50.1,
  "timestamp": "2025-12-02 01:43:07"
}
```
Response: Status of saved data

### 3. Get Sensor Data
Method: GET, URL: `{{base_url}}/data`
Purpose: Retrieve all sensor data
Headers: Authorization: `Bearer {{jwt_token}}`
Response: JSON array of all sensor readings

### 4. Send Command to Device
Method: POST, URL: `{{base_url}}/command/device_001`
Purpose: Send a command to the IoT device via MQTT
Headers: Authorization: `Bearer {{jwt_token}}`, Content-Type: `application/json`
Body example:
```json
{
  "command": "turn_on"
}
```
Response: Status of sent command

## Notes
Always login first to get a valid JWT token. Use environment variables to avoid manually editing each request. The collection allows testing both device-to-cloud and cloud-to-device communication.

