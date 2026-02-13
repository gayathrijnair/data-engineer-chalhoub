import streamlit as st, duckdb, pandas as pd

con=duckdb.connect("../simple-openmeteo-pipeline/weather.duckdb")
df=con.execute("SELECT * FROM weather").fetchdf()

st.title("Simple Weather Dashboard")
if df.empty:
    st.write("No data yet.")
else:
    city=st.selectbox("City", df.city.unique())
    st.line_chart(df[df.city==city].set_index("ts")[["temp","pm25"]])
