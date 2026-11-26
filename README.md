# Meshwave – Peer-to-Peer Resource Monitoring System

## Project Overview
Meshwave is a Python-based project exploring peer-to-peer communication, task sharing, data serialization, and system resource monitoring.

## Features
- Peer-to-peer communication using Python sockets.
- Data serialization using Cloudpickle.
- CPU usage monitoring.
- RAM usage monitoring.
- Asynchronous task communication using asyncio.
- Resource information exchange between components.

## Technologies Used
- Python
- Socket Programming
- Asyncio
- Cloudpickle
- Psutil
- Git and GitHub

## Project Files
- `main.py` – Main project entry point.
- `peer_a.py` – Peer A communication.
- `peer_b.py` – Peer B communication.
- `cpu_ram.py` – CPU and RAM monitoring.
- `resource_monitor.py` – System resource monitoring.
- `serialization.py` – Data serialization.
- `meshwave_project.py` – Asynchronous task communication.

## Installation

Install the required libraries:

```bash
pip install psutil cloudpickle
```

## Run Resource Monitor

```bash
python resource_monitor.py
```

## Project Objective
The objective of Meshwave is to explore distributed computing concepts through peer communication, task exchange, serialization, and resource monitoring.

## Future Enhancements
- Improved peer communication.
- Better error handling.
- Resource usage alerts.
- Automated testing.
- Improved logging.

## Author
Developed as a college/internship project.
