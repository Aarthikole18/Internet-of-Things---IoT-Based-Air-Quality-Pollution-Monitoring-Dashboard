import random
import time
import pandas as pd
from datetime import datetime

while True:

    temp = round(random.uniform(20,35),1)
    hum = round(random.uniform(40,90),1)
    aqi = random.randint(20,250)

    print(f"ESP32 -> {temp},{hum},{aqi}")

    row = pd.DataFrame([{
        "Time": datetime.now(),
        "Temperature": temp,
        "Humidity": hum,
        "AQI": aqi
    }])

    row.to_csv(
    "../data/air_quality_data.csv",
        mode="a",
        header=False,
        index=False
    )

    time.sleep(2)