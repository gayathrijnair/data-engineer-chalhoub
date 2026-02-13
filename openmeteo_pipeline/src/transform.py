import pandas as pd

def normalize_weather(city, raw):
    w = raw["weather"]["hourly"]
    a = raw["air"]["hourly"]

    df_w = pd.DataFrame({
        "ts": pd.to_datetime(w["time"]),
        "temp": w["temperature_2m"]
    })
    df_a = pd.DataFrame({
        "ts": pd.to_datetime(a["time"]),
        "pm25": a["pm2_5"]
    })

    df = df_w.merge(df_a, on="ts", how="left")
    df["city"] = city
    return df
