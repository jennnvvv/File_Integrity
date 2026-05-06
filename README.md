# File Integrity Checker

## Overview

The File Integrity Checker is a DevOps and Security-focused CLI tool designed to monitor files and detect unauthorized modifications. The application generates SHA-256 hashes for files, stores them securely, and later compares them to identify changes.

This project demonstrates:

* File Integrity Monitoring (FIM)
* SHA-256 hashing
* CLI tool development
* Docker containerization
* Logging and alerting
* DevOps-oriented deployment practices

---

# Features

* Detect modified files
* Detect newly added files
* Detect deleted files
* CLI-based workflow
* SHA-256 hashing
* JSON-based hash storage
* Email alerts for detected changes
* Dockerized deployment
* Logging support

---

# Tech Stack

| Component        | Technology            |
| ---------------- | --------------------- |
| Language         | Python                |
| Hashing          | SHA-256 (`hashlib`)   |
| CLI              | Click                 |
| Storage          | JSON                  |
| Containerization | Docker                |
| Logging          | Python Logging Module |
| Alerts           | SMTP Email            |

---

# Project Structure

```text
File_Integrity_Checker/
│
├── main.py
├── cli.py
├── checker.py
├── hasher.py
├── storage.py
├── logger.py
├── alerts.py
├── requirements.txt
├── Dockerfile
├── db.json
├── logs/
│   └── integrity.log
└── test_folder/
```

---

# How the Project Works

## Step 1: Initialization

The tool scans a directory and generates SHA-256 hashes for every file.

These hashes are stored inside:

```text
db.json
```

Example:

```json
{
    "test_folder/hello.txt": "3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"
}
```

---

## Step 2: Integrity Check

The tool scans the directory again and compares:

* Current hashes
* Previously stored hashes

It identifies:

* Modified files
* New files
* Deleted files

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/File_Integrity_Checker.git
cd File_Integrity_Checker
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Initialize Hash Database

```bash
python main.py init test_folder
```

Expected Output:

```text
Hashes stored successfully.
```

---

## Modify a File

Example:

Before:

```text
System Log Initialized
User authentication successful
```

After:

```text
System Log Initialized
Unauthorized access detected
```

---

## Run Integrity Check

```bash
python main.py check test_folder
```

Example Output:

```text
⚠ hello.txt → Modified

Summary:
Modified: 1
New: 0
Deleted: 0
Unchanged: 0
```

---

## Update File Hash

```bash
python main.py update test_folder/hello.txt
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t integrity-checker .
```

---

## Run Initialization Inside Docker

```bash
docker run -v ${PWD}:/app integrity-checker python main.py init test_folder
```

---

## Run Integrity Check Inside Docker

```bash
docker run -v ${PWD}:/app integrity-checker python main.py check test_folder
```

---

# Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
```

---

# Logging

The application stores logs inside:

```text
logs/integrity.log
```

Example:

```text
2026-05-06 11:20:10 - INFO - CHECK started for test_folder
```

---

# Email Alerts

The tool can send email alerts whenever file changes are detected.

Configuration is stored inside:

```text
alerts.py
```

Example:

```python
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_google_app_password"
EMAIL_RECEIVER = "receiver@gmail.com"
```

Google App Passwords are required for SMTP authentication.

---

# Example Workflow

## 1. Initialize

```bash
python main.py init test_folder
```

## 2. Modify File

Edit:

```text
hello.txt
```

## 3. Run Check

```bash
python main.py check test_folder
```

## 4. Receive Alert

The tool:

* Detects modification
* Logs the event
* Sends email alert

---

# Security Concepts Used

## SHA-256 Hashing

SHA-256 generates a unique fingerprint for every file.

Even a small change in file contents produces a completely different hash.

---

## File Integrity Monitoring (FIM)

FIM systems detect unauthorized or suspicious changes in monitored files.

Common enterprise use cases:

* Log monitoring
* Configuration protection
* Security auditing
* Compliance monitoring

---

# Future Improvements

Potential upgrades:

* SQLite-based storage
* Slack webhook alerts
* Real-time monitoring
* Merkle Tree implementation
* Grafana dashboard integration
* Cron job automation
* Encrypted hash storage
* Ignore rules similar to `.gitignore`

---

# Challenges Faced

* Docker container argument handling
* Volume mounting with Docker
* Gmail SMTP authentication
* CLI argument parsing
* File path consistency during integrity checks

---

# Learning Outcomes

This project helped in understanding:

* Docker fundamentals
* CLI application development
* SHA-256 hashing
* File integrity monitoring
* Python modular architecture
* Logging and alert systems
* DevOps deployment workflows

---

# Contributors

* Jennessa
* Team Member

---

# Conclusion

The File Integrity Checker demonstrates how DevOps and security concepts can be combined to create a practical monitoring tool.

By integrating hashing, containerization, logging, and alerting, the project simulates real-world integrity monitoring systems used in enterprise environments.
