import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forcast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forcast days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)

dates = ["2025-25-10", "2025-26-11", "2025-27-10"]
temperatures = [10, 11, 15]
temperatures = [days * i for i in temperatures]

figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Dates", "y": "Temperature °C"})

st.plotly_chart(figure)