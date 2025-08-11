import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


if __name__ == '__main__':
    # Get IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    """your code here"""
    # Create a client object
    client = mqtt.Client()
    
    # Attach the on_connect() callback function defined above to the MQTT client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in Python.
        
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

    """Ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing MQTT messages."""
    client.loop_start()
    time.sleep(1)

    while True:
        client.publish("surpreet/ipinfo", f"{ip_address}")
        print(f"Publishing IP address: {ip_address}")
        time.sleep(4)

        # Get date and time 
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")

        # Publish date and time in their own topics
        client.publish("surpreet/dateinfo", current_date)
        print(f"Publishing Date: {current_date}")

        client.publish("surpreet/timeinfo", current_time) 
        print(f"Publishing Time: {current_time}")

        time.sleep(4) 
