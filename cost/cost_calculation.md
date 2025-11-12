# 💰 Azure Cost Calculator – Smart Home IoT Project

This document presents an approximate monthly cost for running the Smart Home IoT system in Azure with **1000 devices** and **300 users**.

| Component | Azure Service | Description | Est. Monthly Cost (USD) |
|------------|----------------|--------------|--------------------------|
| IoT Hub | Azure IoT Hub (B1 Tier) | Handles MQTT messages | $10 |
| Database | Azure Database for PostgreSQL | Stores sensor data | $30 |
| Web API | Azure App Service (B1) | Hosts FastAPI backend | $13 |
| Blob Storage | Azure Blob Storage (Hot Tier, 50GB) | Logs and backups | $1.50 |
| Monitoring | Azure Monitor | Collects logs | $2 |
| Outbound Data | Data Transfer (20GB) | Network usage | $1.50 |

**Estimated total monthly cost: ≈ $58 USD**

👉 [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)
