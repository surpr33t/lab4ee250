# MQTT Pub/Sub Examples (Python)  
**Partners:** Surpreet Kaur  
## Overview  
This project demonstrates simple MQTT publish/subscribe communication using the `paho-mqtt` Python library. It includes three scripts:  
1. **`vm_pub.py`** — Publishes the device's IP address, current date, and current time to MQTT topics on a public broker.  
2. **`vm_sub.py`** — Subscribes to those topics and handles messages with custom callbacks for each type of data.  
3. **`ping_pub.py`** — Minimal publisher that sends an incrementing counter to a topic on a local broker.  
The examples show how MQTT can be used for lightweight, real-time message exchange between devices, with one script acting as the publisher and another as the subscriber.  
## How it Works  
- The publisher connects to an MQTT broker (either a public one like `test.mosquitto.org` or a local broker IP) and sends messages to specific topics.  
- The subscriber connects to the same broker, listens for messages on those topics, and triggers custom callback functions whenever a message arrives.  
- For the public broker example, the subscriber will display the device's IP, date, and time in real-time.  
- For the local broker example, the subscriber can receive a simple numeric counter to verify connectivity.  
## Instructions  
1. **Clone the project:**  
```bash
git clone https://github.com/<your-username>/mqtt-examples.git
cd mqtt-examples
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the public broker example:
Terminal 1 — Start the subscriber:

bash
Copy
Edit
python vm_sub.py
Terminal 2 — Start the publisher:

bash
Copy
Edit
python vm_pub.py
Example output (subscriber):

sql
Copy
Edit
Connected to broker with result code 0
IP Message: 192.168.1.10
Date: 2025-08-11
Time: 11:02:03
Run the local broker ping example:
Update the broker IP in ping_pub.py to your local MQTT broker's IP.
Publisher:

bash
Copy
Edit
python ping_pub.py
Subscriber (using Mosquitto CLI):

bash
Copy
Edit
mosquitto_sub -h <local-broker-ip> -t surpreet/ping -v
Rules / Notes
The public broker (test.mosquitto.org) is shared — don’t send sensitive data.

Topics should be unique to you (e.g., prefix with your name or project) to avoid collisions.

You must have outbound TCP access to port 1883.

For local testing, ensure Mosquitto or another MQTT broker is installed and running.

Resources
Eclipse Paho MQTT Python Client
Mosquitto MQTT Broker
MQTT Essentials










Ask ChatGPT
