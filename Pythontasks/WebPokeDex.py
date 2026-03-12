import streamlit as st
import requests

def hae_pokemon(nimi):
    url = f"https://pokeapi.co/api/v2/pokemon/{nimi.lower()}"
    
    try:
        vastaus = requests.get(url)
        data = vastaus.json()
        return {
            "nimi": data["name"],
            "pituus": data["height"],
            "paino": data["weight"],
            "kuva": data["sprites"]["front_default"]
        }

    except Exception:
        return None


# ----------------------------------------------------
# 2. WEB-KÄYTTÖLIITTYMÄ
# ----------------------------------------------------
st.title("🔴 Pokédex Web 1.0 ⚪")
st.write("Etsi suosikkipokemonisi ja katso sen salaiset tiedot!")

# Syöttökenttä
syote = st.text_input("Syötä Pokemonin nimi (esim. pikachu, charizard):")

# Nappi
if st.button("Etsi Pokemon!"):
    
    if syote != "":
        # Kutsutaan työntekijää!
        pokemon_data = hae_pokemon(syote.strip())
        st.success(f"Löytyi! Se on {pokemon_data['nimi']}")
        st.image(pokemon_data['kuva'])
        st.write(f"Pokemonisi pituus on :{pokemon_data['pituus']} kg")
        st.write(f"Pokemonisi paino on : {pokemon_data['paino']} cm")

       
        
    else:
        st.warning("Kirjoita ensin jokin nimi!")