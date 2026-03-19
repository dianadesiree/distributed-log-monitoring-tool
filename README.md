# Distributed Log Monitoring Tool

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📊 Overview

A lightweight, RESTful log monitoring solution built with **Python** and **Flask**. This tool was developed during my software engineering coursework at **DeVry University** to demonstrate distributed systems concepts, API design, and containerization. It collects, processes, and analyzes system logs, exposing key metrics through a clean API interface.

**Why this project?** In production environments, logs contain critical information for debugging and monitoring. This tool simulates a real-world log aggregation service that helps identify patterns and anomalies in system behavior—a fundamental skill for any **Data Scientist** or **DevOps** professional.

---

## ✨ Key Features

- **📝 Log Collection**: REST API endpoint to receive logs from multiple sources
- **🔍 Log Retrieval**: Query logs by date, level, and source with filtering
- **📈 Metrics Generation**: Real-time statistics on log levels and error rates
- **🗑️ Log Management**: Delete logs by date for data retention control
- **🐳 Containerized**: Docker support for easy deployment across any platform
- **⚡ Lightweight**: Minimal dependencies, perfect for learning and prototyping

---

## 🏗️ Architecture

## Architecture Flow

    ┌──────────┐         ┌──────────┐         ┌──────────┐
    │  Client  │ ──────▶│Collector │ ──────▶ │ Storage  │
    │ (App/CLI)│         │ (Flask)  │         │(JSON)    │
    └──────────┘         └──────────┘         └──────────┘
                               │                    │
                               │                    │
                               ▼                    ▼
                         ┌─────────────────────────────┐
                         │       API Endpoints         │
                         │  • POST /logs               │
                         │  • GET /logs                │
                         │  • GET /metrics             │
                         │  • DELETE /logs/<date>      │
                         └─────────────────────────────┘
---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **Flask** | Web framework for REST API |
| **Docker** | Containerization and deployment |
| **Git** | Version control |
| **JSON** | Log storage format |

---

## 📁 Project Structure

```
distributed-log-monitoring-tool/
├── app/
│   ├── __init__.py          # Makes app a Python package
│   ├── collector.py          # Log collection logic
│   ├── api.py                # Flask API endpoints
│   ├── logs/                 # Stored log files (auto-generated)
│   └── tests/                # Unit tests (coming soon)
├── .gitignore                # Files ignored by Git
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
├── docker-compose.yml        # Docker Compose setup
├── LICENSE                   # MIT License
└── README.md                 # This file
```
---

## 🚀 Getting Started (Windows Instructions)

### Prerequisites

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/download/win))
- **Docker Desktop** (optional, [Download](https://www.docker.com/products/docker-desktop/))

### Installation & Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dianadesiree/distributed-log-monitoring-tool.git
   cd distributed-log-monitoring-tool

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run the application**
   ```bash
   python -m app.api

4. **Test the API**
   ```bash
   # Health check
   curl http://localhost:5000/api/health

   # Send a test log
   curl -X POST http://localhost:5000/api/logs \
   -H "Content-Type: application/json" \
   -d '{"level": "INFO", "message": "Service started", "source": "test"}'

   # Retrieve logs
   curl http://localhost:5000/api/logs

   # Get metrics
   curl http://localhost:5000/api/metrics

## 🐳 Docker Deployment

1. **Build the Docker image**
    ```bash
    docker build -t log-monitor .
    ```

2. **Run with Docker**
   ```bash
   docker run -p 5000:5000 -v $(pwd)/logs:/app/logs log-monitor

3. **Or use Docker Compose (recommended)**
   ```bash
   docker-compose up -d

## 📚 API Documentation

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| **/api/health** | GET | Service health check | None |
| **/api/logs** | POST | Submit a new log | JSON body with log data |
| **/api/logs** | GET | Retrieve logs | date, level, limit (query params) |
| **/api/metrics** | GET | Get log statistics | None |
| **/api/logs/{date}** | DELETE | Delete logs for a date | Date in YYYY-MM-DD format |


---

## 📥 Example Log Format

"level": "ERROR",
  "message": "Database connection timeout",
  "source": "payment-service",
  "context": {
    "user_id": 12345,
    "retry_count": 3
  },
  "timestamp": "2026-03-18T15:30:45.123Z"
