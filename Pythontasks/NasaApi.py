import streamlit as st
import requests

api = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": "uMRaTMwZJutrhvPpOYu0441jR3SWM1ibbeskye1i"})
data = api.json()


st.image(data["url"])
st.write(data["explanation"])
st.write(data["date"])
st.date_input(DateValue' = 'today')

