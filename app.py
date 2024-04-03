import streamlit as st 
import pandas as pd 
import folium
from streamlit_folium import st_folium
import streamlit as st

st.set_page_config(page_title="BIS Alumni Locator")

st.title(""" # BIS Alumni Locator """)

x = 0
close = False

#Initialize session state
if "load_state" not in st.session_state:
    st.session_state.load_state = False

data = pd.read_excel("New Microsoft Excel Worksheet.xlsx")

m = folium.Map()

while True:
    for i in range(0, len(data)):
        url = data.iloc[i]["Linkedin URL"]
        icon = data.iloc[i]["images"]
        isnan = pd.isna(icon)
        if isnan:
            ic = folium.Icon(color="green")
        else:
            ic = folium.features.CustomIcon(icon, icon_size=(30,30))
            folium.Marker([data.iloc[i]["Coordinate"], data.iloc[i]["Coordinate.1"]], popup='<a href='+url+' target="_blank"> Linkedin Profile </a>', tooltip=data.iloc[i]["Name on Screen"], icon=ic).add_to(m)

    st_data = st_folium(m,width=700)
