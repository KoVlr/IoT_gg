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
    timestamp = str(int(datetime.now().timestamp())) + "0" * 9
    mqttc.publish("iot_gg", f"room "
                  f"temperature={room.temperature},"
                  f"humidity={room.humidity},"
                  f"voltage={room.voltage} {timestamp}",)
    mqttc.publish("iot_gg", f"heater "
                  f"temperature={room.heater.temperature},"
                  f"fuel_amount={room.heater.fuel_amount},"
                  f"state={1 if room.heater.is_on() else 0},"
                  f"preset_temperature={room.heater.preset_temperature},"
                  f"battery_charge={room.heater.battery_charge} {timestamp}")
    sleep(10)

room.stop()
mqttc.disconnect()