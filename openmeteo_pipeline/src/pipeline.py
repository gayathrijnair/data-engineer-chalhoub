import duckdb
from src.extract import fetch_weather_data
from src.transform import normalize_weather
from src.load import append_df

def main():
    con = duckdb.connect("data/weather.duckdb")
    con.execute("CREATE TABLE IF NOT EXISTS weather (city TEXT, ts TIMESTAMP, temp DOUBLE, pm25 DOUBLE);")

    cities = ["Dubai", "Riyadh"]

    for city in cities:
        raw = fetch_weather_data(city)
        if raw is None:
            continue

        df = normalize_weather(city, raw)
        append_df(con, df)

    print("Done.")

if __name__ == "__main__":
    main()
