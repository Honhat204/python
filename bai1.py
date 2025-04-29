import requests
import pandas as pd
from datetime import datetime

# 1. Gọi API Open-Meteo để lấy dữ liệu thời tiết
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "past_days": 10,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "auto"
}

response = requests.get(url, params=params)
data = response.json()

# 2. Tạo DataFrame
df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature_2m": data["hourly"]["temperature_2m"],
    "relative_humidity_2m": data["hourly"]["relative_humidity_2m"],
    "wind_speed_10m": data["hourly"]["wind_speed_10m"]
})

df["latitude"] = data["latitude"]
df["longitude"] = data["longitude"]
df = df[["latitude", "longitude", "time", "temperature_2m", "relative_humidity_2m", "wind_speed_10m"]]

# 3. Ghi ra file CSV
df.to_csv("weather_data.csv", index=False)
print(" Đã lưu file weather_data.csv")

# 4. Tính tổng đến ngày 29-04
df["time"] = pd.to_datetime(df["time"])
df_filtered = df[df["time"] <= pd.to_datetime("2025-04-29 23:59:59")]

print(" Tổng đến 29/04:")
print("Nhiệt độ:", df_filtered["temperature_2m"].sum())
print("Độ ẩm:", df_filtered["relative_humidity_2m"].sum())
print("Tốc độ gió:", df_filtered["wind_speed_10m"].sum())
