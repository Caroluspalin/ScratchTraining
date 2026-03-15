import streamlit as st

st.title("🏆 Minun Top 5 Pokemonit")
st.write("Tässä on mun absoluuttinen unelmatiimi, numeroituna tyylillä!")


unelmatiimi = ["Charizard", "Gengar", "Mewtwo", "Snorlax", "Gyarados"]

for numero, poke in enumerate(unelmatiimi): 
    sijoitus = numero + 1
    st.write(f"Sijalla {sijoitus} on {poke}")

