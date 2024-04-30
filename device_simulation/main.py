import paho.mqtt.client as mqtt
from time import sleep
from room import Room
from datetime import datetime

room = Room(15, -5)
room.start()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("mosquitto")

room.start()
while True:
    timestamp = datetime.now().timestamp()
    mqttc.publish("iot_gg", f"room temperature={room.temperature}")
    mqttc.publish("iot_gg", f"heater temperature={room.heater.temperature},fuel_amount={room.heater.fuel_amount},state={1 if room.heater.is_on else 0}")
    sleep(10)

room.stop()
mqttc.disconnect()