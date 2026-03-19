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
distributed-log-monitoring-tool/
├── app/
│ ├── init.py # Makes app a Python package
│ ├── collector.py # Log collection logic
│ └── api.py # Flask API endpoints
├── logs/ # Stored log files (auto-generated)
├── tests/ # Unit tests (coming soon)
├── .gitignore # Files ignored by Git
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── docker-compose.yml # Docker Compose setup
├── LICENSE # MIT License
└── README.md # This file

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
