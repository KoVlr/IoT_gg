import paho.mqtt.client as mqtt
from time import sleep
from room import Room
from datetime import datetime

room = Room(15, -5)
room.start()

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}.")
    else:
        client.subscribe("iot_gg/control/heater")

def on_message(client, userdata, message):
    if "instruction state=0" in message.payload.decode():
        room.heater.turn_off()
    elif "instruction state=1" in message.payload.decode():
        room.heater.turn_on()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("mosquitto")

mqttc.loop_start()

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

mqttc.loop_stop()
room.stop()
mqttc.disconnect()