import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Set the page configuration
st.set_page_config(page_title="BIS Alumni Locator")

# Page title
st.title("# BIS Alumni Locator")

# Initialize session state for loading data
if "load_state" not in st.session_state:
    st.session_state.load_state = True
    # Load the data only once
    st.session_state.data = pd.read_excel("New Microsoft Excel Worksheet.xlsx")

# Check if data is loaded to session state
if st.session_state.load_state:
    data = st.session_state.data
    m = folium.Map(location=[20, 0], zoom_start=2)  # Adjusted to show a more global view initially

    # Iterate through the data and add markers
    for i in range(len(data)):
        url = data.iloc[i]["Linkedin URL"]
        icon = data.iloc[i]["images"]
        isnan = pd.isna(icon)
        
        if isnan:
            ic = folium.Icon(color="green")
        else:
            ic = folium.features.CustomIcon(icon, icon_size=(30, 30))
        
        folium.Marker(
            [data.iloc[i]["Coordinate"], data.iloc[i]["Coordinate.1"]],
            popup=f'<a href="{url}" target="_blank">LinkedIn Profile</a>',
            tooltip=data.iloc[i]["Name on Screen"],
            icon=ic
        ).add_to(m)

    # Display the map
    st_folium(m, width=700)
