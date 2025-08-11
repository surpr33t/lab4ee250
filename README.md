# MQTT Pub/Sub Examples

**Author:** Surpreet Kaur  

## Overview
A set of simple Python scripts demonstrating MQTT publish/subscribe messaging using the `paho-mqtt` library. Includes:
- `vm_pub.py` — Publishes the device's IP address, date, and time to a public MQTT broker.
- `vm_sub.py` — Subscribes to those topics and prints incoming messages using custom callbacks.
- `ping_pub.py` — Sends an incrementing counter to a local broker for quick connectivity testing.

## How It Works
The publisher sends messages to specific topics on an MQTT broker (either public or local). The subscriber listens to the same topics and processes messages in real time. This setup is useful for IoT applications, status updates, or lightweight data exchange between devices.

## Quick Start  
Clone the repository:  
```bash
git clone https://github.com/<your-username>/mqtt-examples.git
cd mqtt-examplest
```
## Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
## Install dependencies:
```bash
pip install -r requirements.txt
```
## Run the public broker example:
```bash
# Terminal 1 — Subscriber
python vm_sub.py

# Terminal 2 — Publisher
python vm_pub.py
```

## Example Output: 
```bash
Connected to broker with result code 0
IP Message: 192.168.1.10
Date: 2025-08-11
Time: 11:02:03
```

## Notes 
```bash
The public broker test.mosquitto.org is shared — avoid sending sensitive data.
Use unique topic prefixes to prevent collisions.
Requires TCP access to port 1883.
```

## Resources 
```bash
Paho MQTT Python Client
Mosquitto MQTT Broker
MQTT Essentials
```







