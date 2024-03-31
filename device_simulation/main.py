import paho.mqtt.client as mqtt
from time import sleep

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("mosquitto")

for i in range(60):
    mqttc.publish("iot_gg", f"weather temperature={i}")
    sleep(10)

mqttc.disconnect()