import requests

def geocode(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    r = requests.get(url).json()
    if not r.get("results"):
        return None
    d = r["results"][0]
    return d["latitude"], d["longitude"]

def fetch_weather_data(city):
    loc = geocode(city)
    if not loc:
        print(f"No geocode results for {city}")
        return None
    lat, lon = loc

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    air_url     = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=pm2_5"

    w = requests.get(weather_url).json()
    a = requests.get(air_url).json()
    return {"weather": w, "air": a}
