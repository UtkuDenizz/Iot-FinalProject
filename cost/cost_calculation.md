# 💰 Cost Calculation – Smart Home IoT Project

This document presents the estimated monthly cost of running the **Smart Home IoT** system on Microsoft Azure, assuming:

- **1000 IoT devices** sending sensor data  
- **300 customers** accessing the system through the REST API  
- The existing cloud infrastructure used in the project  
  (Azure VM, App Service, PostgreSQL Flexible Server)

---

## 📡 1. MQTT Broker – Azure Virtual Machine

The system uses a **VM-based Mosquitto MQTT Broker** to handle device communication.

| Component | Details |
|----------|---------|
| Azure Service | Virtual Machine (D2 v3) |
| vCPU / RAM | 2 vCPU, 8 GB RAM |
| Region | France Central |
| Pricing Tier | Pay-as-you-go |
| Estimated Load | Handles 1000 IoT devices easily |

**Cost:**  
`$81.76 / month`

---

## 🗄️ 2. Database – Azure Database for PostgreSQL

The project stores sensor data (temperature, humidity, timestamp) in Azure PostgreSQL Flexible Server.

| Component | Details |
|----------|---------|
| Azure Service | PostgreSQL Flexible Server |
| Deployment Mode | Flexible Server |
| Tier | General Purpose |
| Instance Size | D2ds v5 (2 vCPU, 8GB RAM) |
| Storage | Premium SSD (5 GB) |
| Estimated Load | Enough to store millions of sensor records |

**Cost:**  
`$150.38 / month`

---

## 🌐 3. Backend – Azure App Service (REST API)

The FastAPI backend is deployed using Azure App Service.

| Component | Details |
|----------|---------|
| Azure Service | App Service |
| Tier | Basic (B1) |
| Instance Count | 1 |
| Region | France Central |
| Usage | Serves ~300 customers |

**Cost:**  
`$68.62 / month`

---

## 📊 4. Azure Monitor (Logs & Metrics)

Basic application logging and system monitoring.

**Cost:**  
`$2.00 / month`

---

## 🌍 5. Outbound Data Transfer

Estimated outbound traffic for device telemetry + API responses:

- ~20GB outbound per month  

**Cost:**  
`$1.50 / month`

---

# ✅ Total Estimated Monthly Cost

| Service | Monthly Cost |
|---------|--------------|
| MQTT VM | $81.76 |
| PostgreSQL Server | $150.38 |
| App Service | $68.62 |
| Azure Monitor | $2.00 |
| Outbound Data | $1.50 |
| **Total** | **≈ $304.26 / month** |

---

# 📌 Summary

This cost estimation reflects a realistic cloud architecture capable of supporting:

- **1000 IoT devices** sending telemetry  
- **300 active customers** accessing historical and real-time data  
- A scalable backend and secure database

The infrastructure was intentionally kept minimal while ensuring reliability and performance.

---

# 📎 Azure Pricing Calculator Links (Optional)

- Virtual Machine: https://azure.microsoft.com/en-us/pricing/calculator/
- PostgreSQL Flexible Server: https://azure.microsoft.com/en-us/pricing/calculator/
- App Service: https://azure.microsoft.com/en-us/pricing/calculator/
