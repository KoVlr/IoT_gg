import time
import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid, reason_code, properties):
    # reason_code and properties will only be present in MQTTv5. It's always unset in MQTTv3
    print("on_publish")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_publish = on_publish
mqttc.connect("127.0.0.1")

mqttc.loop_start()
msg_info = mqttc.publish("iot_gg", "weather temperature=7")
msg_info.wait_for_publish()
mqttc.disconnect()
mqttc.loop_stop()