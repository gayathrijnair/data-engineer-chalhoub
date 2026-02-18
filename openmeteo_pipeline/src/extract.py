import requests

def geocode(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    r = requests.get(url).json()
    if not r.get("results"):
        return None
    if r["results"][0]:
        d = r["results"][0]
        keys = ["id", "name", "country", "latitude", "longitude", "timezone", "elevation"]
        country_json = {k: d.get(k) for k in keys}
    else:
        country_json = {}

    return(country_json)

def fetch_weather_data(city):
    loc = geocode(city)
    if not loc:
        print(f"No geocode results for {city}")
        return None
    lat, lon = loc['latitude'], loc['longitude']

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,wind_speed_10m"
    air_url     = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=pm10,pm2_5,ozone,uv_index"

    w = requests.get(weather_url).json()
    a = requests.get(air_url).json()

    return {"location" : loc,"weather": w, "air": a}

