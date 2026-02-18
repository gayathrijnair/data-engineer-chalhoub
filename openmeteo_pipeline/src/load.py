def append_df(con, df_weather, df_air, df_location ):
        con.register("df_weather", df_weather)
        con.execute("INSERT INTO fct_weather SELECT p_id,ts, temp, wind_ms FROM df_weather;")
        con.unregister("df_weather")
        con.register("df_air", df_air)
        con.execute("INSERT INTO  fct_air SELECT p_id, ts, pm_10, pm25, ozone, uv_index FROM df_air;")
        con.unregister("df_air")
        con.register("df_location", df_location)
        con.execute("INSERT INTO dim_location  SELECT id, name, country, latitude, longitude, timezone, elevation FROM df_location WHERE id NOT IN (SELECT id FROM dim_location);")
        con.unregister("df_location")

