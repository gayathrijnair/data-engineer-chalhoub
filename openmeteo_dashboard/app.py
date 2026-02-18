import streamlit as st, duckdb, pandas as pd


db_path = r"c:\users\gayathrii\data-engineer\openmeteo_pipeline\src\data\weather.duckdb"
con=duckdb.connect(db_path)
df=con.execute("SELECT * FROM mv_env_analytics").fetchdf()

st.title("Simple Weather Dashboard")
st.title("Environment Dashboard")


median_temp = df["temp_c"].median()
pm25_p95 = df["pm2_5"].quantile(0.95)


col1, col2 = st.columns(2)

col1.metric("Median Temp (°C)", round(median_temp,2))
col2.metric("PM2.5 P95", round(pm25_p95,2))



st.subheader("Temperature Trend by City")

chart_df = df.pivot(
    index="ts_utc",
    columns="city_name",
    values="temp_c"
)

st.line_chart(chart_df)


st.subheader("PM2.5 Trend")
chart_df_pm = df.pivot(
    index="ts_utc",
    columns="city_name",
    values="pm2_5"
)

st.line_chart(chart_df_pm)


st.subheader("Recent Records")
st.dataframe(df.tail(20))
