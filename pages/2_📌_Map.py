import streamlit as st
import pandas as pd
import folium
import ast
import numpy as np
from streamlit_folium import folium_static

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Set the page title
st.title("Air Quality Index (AQI) Stations Map")

# Add a brief introduction
st.write("Welcome to the AQI Stations Map! This interactive map displays the real-time AQI data from all the AQI monitoring stations across India.")

# Load the data from AQIstations.xlsx file
data = pd.read_excel("AQIstations.xlsx")

# Create a new dataframe with latitude and longitude columns
coordinates = pd.DataFrame(columns=["latitude", "longitude"])

# Iterate over the rows of the data dataframe and add the coordinates to the coordinates dataframe
for i, row in data.iterrows():
    coords = eval(row["lat_long"])
    coordinates = coordinates.append({"latitude": coords[0], "longitude": coords[1]}, ignore_index=True)

# Create a folium map centered around India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add markers to the map for each coordinate in the coordinates dataframe
for i, row in coordinates.iterrows():
    folium.Marker(location=[row["latitude"], row["longitude"]]).add_to(m)

# Display the map
st.write("Use the interactive map below to explore the AQI data from different monitoring stations across India. Zoom in and click on a marker to see the AQI data for that location.")
folium_static(m)

# Add more information about AQI and why it is important to monitor
st.write("## What is AQI?")
st.write("The Air Quality Index (AQI) is a numerical scale used to measure air pollution levels. The AQI values range from 0 to 500, with higher values indicating higher levels of air pollution. The AQI is calculated based on several pollutants, including particulate matter, ozone, nitrogen dioxide, and sulfur dioxide.")

st.write("## Why Monitor AQI?")
st.write("Air pollution can have serious health effects, especially for vulnerable populations like children, elderly, and people with pre-existing health conditions. Monitoring the AQI can help individuals and communities take measures to reduce their exposure to air pollution and protect their health.")

st.write("## About Our Data")
st.write("The AQI data displayed on this map is sourced from the Central Pollution Control Board (CPCB), the primary agency responsible for monitoring air pollution in India. The data is updated in real-time, providing you with the most accurate and up-to-date information on air pollution levels in your area.")

# Add a disclaimer
st.write("## Disclaimer")
st.write("While we strive to provide the most accurate and up-to-date information on air pollution levels, the data displayed on this map should be used for informational purposes only. We do not guarantee the accuracy or completeness of the data, and we are not liable for any damages or losses resulting from the use of this map or the data displayed on it.")
