import streamlit as st
import plotly.express as px

with open("data.txt", 'r') as file:
    contents = file.read()

contents =  contents.split('\n')[1:-1]

dates = []
temperatures = []
for content in contents:
    date, temperature = content.split(',')
    temperatures.append(temperature)
    dates.append(date)

fig = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature(C)"})
st.plotly_chart(fig)

