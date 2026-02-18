import pandas as pd

def normalize_weather(city, raw):
    loc_json = raw["location"]
    w = raw["weather"]["hourly"]
    a = raw["air"]["hourly"]

    df_w = pd.DataFrame({
        "p_id" : loc_json['id'],
        "ts": pd.to_datetime(w["time"]),
        "temp": w["temperature_2m"],
        "wind_ms" : w["wind_speed_10m"]
    })
    df_a = pd.DataFrame({
        "p_id": loc_json['id'],
        "ts": pd.to_datetime(a["time"]),
        "pm_10": a["pm10"],
        "pm25": a["pm2_5"],
        "ozone": a["ozone"],
        "uv_index": a["uv_index"]

    })
    loc = pd.DataFrame([loc_json])
    return loc, df_w, df_a

