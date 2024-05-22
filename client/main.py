import paho.mqtt.client as mqtt
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("mosquitto", keepalive=10000)

@app.get("/")
def root():
    return FileResponse("index.html")

@app.post("/heater")
def set_heater_state(state: int):
    mqttc.publish("iot_gg/control/heater", f"instruction state={state}")