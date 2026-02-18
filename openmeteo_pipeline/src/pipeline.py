import duckdb
from extract import fetch_weather_data
from transform import normalize_weather
from load import append_df
import os
from datetime import datetime,timedelta

con = duckdb.connect("data/weather.duckdb")
def get_time(city,table_name) :


    max_ts = con.execute("""SELECT  MAX(ts_utc) as max_ts FROM {} fct  left join dim_location dl on fct.place_id= dl.place_id where name = '{}'""".format(table_name,city)).fetchone()[0]
    #print("MAX",max_ts)
    return((max_ts))





def main():
    db_path = r"c:\users\gayathrii\data-engineer\openmeteo_pipeline\src\data\weather.duckdb"

    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    #con = duckdb.connect("data/weather.duckdb")


    con.execute("CREATE TABLE IF NOT EXISTS dim_location(place_id TEXT, name TEXT , country TEXT , lat DOUBLE, lon DOUBLE, timezone TEXT, elevation_m DOUBLE);")
    con.execute("CREATE TABLE IF NOT EXISTS fct_weather(place_id TEXT , ts_utc TIMESTAMP, temp_c DOUBLE, wind_ms DOUBLE);")
    con.execute("CREATE TABLE IF NOT EXISTS fct_air(place_id TEXT, ts_utc TIMESTAMP, pm10 DOUBLE , pm2_5 DOUBLE , ozone DOUBLE , uv_index DOUBLE);")

    cities = ["Dubai", "Riyadh"]
    city_list = []
    for city in cities:
        raw = fetch_weather_data(city)
        if raw is None:
            continue

        loc, df_weather, df_air = normalize_weather(city, raw)

        #Filter out only new timestamps



        watermark_weather = get_time(city,"fct_weather")
        watermark_air = get_time(city,"fct_air")
        if watermark_weather is not None :
                filtered_df_weather = df_weather[df_weather["ts"] > watermark_weather]
        else :
                filtered_df_weather = df_weather


        if watermark_air is not None :
                filtered_df_air = df_air[df_weather["ts"] > watermark_weather]
        else :
                filtered_df_air = df_air


        append_df(con, filtered_df_weather, filtered_df_air, loc)

    print("Done.")


if __name__ == "__main__":
    main()
