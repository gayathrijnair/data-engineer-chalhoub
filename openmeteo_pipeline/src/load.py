def append_df(con, df):
    con.register("df", df)
    con.execute("INSERT INTO weather SELECT city, ts, temp, pm25 FROM df;")
    con.unregister("df")
