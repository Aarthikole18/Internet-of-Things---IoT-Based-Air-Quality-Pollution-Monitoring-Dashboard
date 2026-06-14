import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Analytics")

df = pd.read_csv("../data/air_quality_data.csv")

fig1 = px.line(
    df,
    y="AQI",
    title="AQI Trend"
)

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(
    df,
    y="Temperature",
    title="Temperature Trend"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.line(
    df,
    y="Humidity",
    title="Humidity Trend"
)

st.plotly_chart(fig3, use_container_width=True)