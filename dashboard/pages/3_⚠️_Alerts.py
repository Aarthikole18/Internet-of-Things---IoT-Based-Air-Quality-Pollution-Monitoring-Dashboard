import streamlit as st
import pandas as pd

st.title("⚠️ Pollution Alerts")

df = pd.read_csv("../data/air_quality_data.csv")

alerts = df[df["Status"] == "Hazardous"]

st.dataframe(alerts)

if len(alerts) > 0:
    st.error(
        f"{len(alerts)} Hazardous Pollution Events Detected"
    )
else:
    st.success("No Hazardous Pollution Events")