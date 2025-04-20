import streamlit as st
import plotly.express as px
from backend import get_data

# Add widgets
st.title("Weather Forcast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Select the number of forcast days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get data
    filtered_data = get_data(place, days)

    # Create a plot
    if option == "Temperature":
        temp = [info["main"]["temp"] / 10 for info in filtered_data]
        dates = [info["dt_txt"] for info in filtered_data]
        figure = px.line(x=dates, y=temp,
                         labels={"x": "Dates", "y": "Temperature °C"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        sky_conditions = [info["weather"][0]["main"] for info in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)
