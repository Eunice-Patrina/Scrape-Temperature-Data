import streamlit as st
import plotly.express as px
import pandas as pd

data = pd.read_csv("data.txt")

fig = px.line(x=data['date'], y=data['temperature'], labels={"x": "Dates", "y": "Temperature(C)"})
st.plotly_chart(fig)

