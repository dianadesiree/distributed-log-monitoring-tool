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

The application follows a modular design:
