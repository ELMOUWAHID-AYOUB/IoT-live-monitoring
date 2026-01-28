# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"status": "Backend OK"}


import requests
import paho.mqtt.client as mqtt
import time
from fastapi import FastAPI




app = FastAPI()

GPS_URL = "http://host.docker.internal:5007/gps"
BATTERY_URL = "http://host.docker.internal:5002/battery"
TEMP_URL = "http://host.docker.internal:5003/temperature"



mqtt_client = mqtt.Client()

# Boucle pour attendre que MQTT soit disponible
while True:
    try:
        mqtt_client.connect("mqtt", 1856, 60)
        print("MQTT connecté !")
        break
    except Exception as e:
        print("Impossible de se connecter à MQTT, je réessaie dans 2s...")
        time.sleep(2)


@app.get("/collect")
def collect():
    gps = requests.get(GPS_URL).json()
    battery = requests.get(BATTERY_URL).json()
    temp = requests.get(TEMP_URL).json()


    data = {
        "gps": gps,
        "battery": battery,
        "temperature": temp
    }
    mqtt_client.publish("tracking/session1", str(data))

    return data



# import paho.mqtt.client as mqtt

# mqtt_client = mqtt.Client()
# mqtt_client.connect("mqtt", 1883, 60)
# mqtt_client.publish("tracking/session1", str(data))
