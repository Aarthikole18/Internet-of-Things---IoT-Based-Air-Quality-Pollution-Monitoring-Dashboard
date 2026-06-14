import streamlit as st
import pandas as pd

st.title("📊 Live Monitoring")

df = pd.read_csv("../data/air_quality_data.csv")

latest = df.iloc[-1]

c1,c2,c3,c4 = st.columns(4)

c1.metric("AQI", latest["AQI"])
c2.metric("Temperature", latest["Temperature"])
c3.metric("Humidity", latest["Humidity"])
c4.metric("Status", latest["Status"])

st.subheader("Latest Readings")

st.dataframe(df.tail(20))