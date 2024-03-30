import paho.mqtt.client as mqtt

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("mosquitto")
mqttc.publish("iot_gg", "weather temperature=20")
mqttc.disconnect()