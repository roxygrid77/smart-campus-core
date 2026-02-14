from fastapi import FastAPI



from typing import List
app = FastAPI()

devices = []
sensor_data = []
alerts = []

@app.get("/")
def home():
    return {"message":"Smart campus core is running"}

@app.post("/devices")
def add_device(device: dict):
    devices.append(device)
    return {"status": "Device added","device": device}

@app.get("/devices")
def get_devices():
    return devices

#sensor data
@app.post("/sensor-data")
def add_sensor_data(data: dict):
    sensor_data.append(data)

    if data.get("temperature", 0) > 40:
        alerts.append({
            "alert": "High temperature detected!",
            "data": data
        })

    return {"status": "Data received"}

@app.get("/sensor-data")
def get_sensor_data():
    return sensor_data

#alerts
@app.get("/alerts")
def get_alerts():
    return alerts