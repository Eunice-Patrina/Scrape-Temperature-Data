import streamlit as st
import plotly.express as px
import sqlite3
#import pandas as pd

connection = sqlite3.connect("data.db")

def plot_from_textfile():
    data = pd.read_csv("data.txt")
    fig = px.line(x=data['date'], y=data['temperature'], labels={"x": "Dates", "y": "Temperature(C)"})
    st.plotly_chart(fig)

def read():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM temperature")
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    values = read()
    dates = []
    temperatures = []
    for value in values:
        date, temperature = value
        dates.append(date)
        temperatures.append(temperature)

    fig = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature(C)"})
    st.plotly_chart(fig)


