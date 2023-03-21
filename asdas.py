import streamlit as st
import requests

st.title("ISS INFORMATION")

posicion_iss = requests.get("http://api.open-notify.org/iss-now.json")

json_iss = posicion_iss.json()
st.json(json_iss)

st.table(json_iss)

latitud = json_iss["iss_position"]["latitude"]
longitud = json_iss["iss_position"]["longitude"]

st.write(f"http://maps.google.com/?q={latitud},{longitud}")

st.title("ASTROUNATS IN SPACE")

astronautas = requests.get("http://api.open-notify.org/astros.json")

astronautas_inspace = astronautas.json()
st.json(astronautas_inspace)

st.table(astronautas_inspace["people"])
