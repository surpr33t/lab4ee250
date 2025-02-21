import paho.mqtt.client as mqtt
import time

BROKER = "172.20.10.3"  
TOPIC_PING = "surpreet/ping"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

num = 1

while True:
    print(f"Publishing {num} to {TOPIC_PING}")
    client.publish(TOPIC_PING, num)  
    time.sleep(1)  
    num += 1  


