import streamlit as st 
import pandas as pd 
import folium
from streamlit_folium import st_folium, folium_static
import streamlit as st

st.set_page_config(page_title="BIS Alumni Locator")

st.title(""" # BIS Alumni Locator """)

user_loc = {"Dinuka":[6.8649,79.8997], "Pramuk":[6.7106,79.9074], "Ishara":[7.2906, 80.6337],
            "Chamalka":[6.9122,79.8829], "Malith":[7.2906, 80.6337],"Dulan":[7.9403,81.0188],
            "Indunil":[8.3114,80.4037],"Anuradha":[6.8433,80.0032], "Achowshan":[43.6532,-79.3832],
            "Chalitha":[6.8018,79.9227]
            }

tooltip = ["Dinuka","Pramuk","Ishara","Chamalka","Malith","Dulan","Indunil","Anuradha","Achowshan","Chalitha"]
m = folium.Map()

dinuka = folium.features.CustomIcon('immgs/dinuka.jpg', icon_size=(25,25))
chamlka = folium.features.CustomIcon('immgs/chamlka.jpg', icon_size=(25,25))
dulan = folium.features.CustomIcon('immgs/dulan.jpg', icon_size=(25,25))
indnil = folium.features.CustomIcon('immgs/indunil.jpg', icon_size=(25,25))
pramuk = folium.features.CustomIcon('immgs/pramuk.jpg', icon_size=(25,25))
acowshan = folium.features.CustomIcon('immgs/acowshan.jpg', icon_size=(25,25))

folium.Marker(
    user_loc['Dinuka'], popup="<i>Dinuka</i>", tooltip=tooltip[0],icon=dinuka
).add_to(m)

folium.Marker(
    user_loc['Pramuk'], popup="<b>Pramuk</b>", tooltip=tooltip[1],icon=pramuk
).add_to(m)

folium.Marker(
    user_loc['Ishara'], popup="<b>Ishara</b>", tooltip=tooltip[2], #icon=pushpin
).add_to(m)

folium.Marker(
    user_loc['Chamalka'], popup="<b>Chamalka</b>", tooltip=tooltip[3], icon=chamlka
).add_to(m)

folium.Marker(
    user_loc['Malith'], popup="<b>Malith</b>", tooltip=tooltip[4], #icon=pushpin
).add_to(m)

folium.Marker(
    user_loc['Dulan'], popup="<b>Dulan</b>", tooltip=tooltip[5], icon=dulan
).add_to(m)

folium.Marker(
    user_loc['Indunil'], popup="<b>Indunil</b>", tooltip=tooltip[6], icon=indnil
).add_to(m)

folium.Marker(
    user_loc['Anuradha'], popup="<b>Anuradha</b>", tooltip=tooltip[7], #icon=pushpin
).add_to(m)

folium.Marker(
    user_loc['Achowshan'], popup="<b>Achowshan</b>", tooltip=tooltip[8], icon=acowshan
).add_to(m)

folium.Marker(
    user_loc['Chalitha'], popup="<b>Chalitha</b>", tooltip=tooltip[9], #icon=pushpin
).add_to(m)


st_data = st_folium(m, width=700)