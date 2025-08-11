# MQTT Subscriber — listens for IP, date, and time messages on given topics.
# Uses paho-mqtt to connect to a public broker and handle messages via custom callbacks.

import paho.mqtt.client as mqtt

# Called when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected to broker with result code {rc}")

    # Subscribe to the topics of interest
    client.subscribe("surpreet/ipinfo")
    client.subscribe("surpreet/dateinfo")
    client.subscribe("surpreet/timeinfo")

    # Assign specific callbacks for each topic
    client.message_callback_add("surpreet/ipinfo", on_message_from_ipinfo)
    client.message_callback_add("surpreet/dateinfo", on_message_from_dateinfo)
    client.message_callback_add("surpreet/timeinfo", on_message_from_timeinfo)

# Default callback for messages without a custom handler
def on_message(client, userdata, msg):
    print(f"Default callback - topic: {msg.topic}   msg: {msg.payload.decode()}")

# Custom callbacks for each subscribed topic
def on_message_from_ipinfo(client, userdata, message):
    print(f"IP Message: {message.payload.decode()}")

def on_message_from_dateinfo(client, userdata, message):
    print(f"Date: {message.payload.decode()}")

def on_message_from_timeinfo(client, userdata, message):
    print(f"Time: {message.payload.decode()}")

if __name__ == '__main__':
    # Create the MQTT client instance
    client = mqtt.Client()

    # Attach callbacks
    client.on_message = on_message
    client.on_connect = on_connect

    # Connect to public Mosquitto broker
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)

    # Enter the network loop and process incoming messages indefinitely
    client.loop_forever()

