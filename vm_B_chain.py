import paho.mqtt.client as mqtt
import time

BROKER = "172.20.10.3"  
TOPIC_PING = "surpreet/ping"
TOPIC_PONG = "surpreet/pong"

def on_message(client, userdata, msg):
    num = int(msg.payload.decode()) + 1  
    print(f"Received {msg.payload.decode()}, publishing {num} to {TOPIC_PON>
    client.publish(TOPIC_PONG, num)  
    time.sleep(1)  

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)

client.subscribe(TOPIC_PING)  
client.loop_forever()

