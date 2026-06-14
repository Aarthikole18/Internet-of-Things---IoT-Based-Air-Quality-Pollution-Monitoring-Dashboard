import serial
import pandas as pd
from datetime import datetime
import os

PORT = "COM5"      # CHANGE THIS
BAUD = 115200

ser = serial.Serial(PORT, BAUD)

csv_file = "../data/air_quality_data.csv"

if not os.path.exists(csv_file):

    pd.DataFrame(
        columns=[
            "Time",
            "Temperature",
            "Humidity",
            "AQI",
            "Status"
        ]
    ).to_csv(csv_file, index=False)

while True:

    line = ser.readline().decode().strip()

    temp, hum, aqi = line.split(",")

    aqi = int(aqi)

    if aqi <= 50:
        status = "Good"
    elif aqi <= 100:
        status = "Moderate"
    elif aqi <= 150:
        status = "Poor"
    else:
        status = "Hazardous"

    row = pd.DataFrame([{
        "Time": datetime.now(),
        "Temperature": temp,
        "Humidity": hum,
        "AQI": aqi,
        "Status": status
    }])

    row.to_csv(
        csv_file,
        mode="a",
        header=False,
        index=False
    )

    print("Saved:", temp, hum, aqi)