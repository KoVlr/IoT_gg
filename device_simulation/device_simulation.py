from random import randint
import paho.mqtt.client as mqtt

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("127.0.0.1")

mqttc.loop_start()
msg_info = mqttc.publish("iot_gg", f"weather temperature={randint(20, 25)}")
msg_info.wait_for_publish()
mqttc.disconnect()
mqttc.loop_stop()