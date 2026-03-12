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
    
def tallenna_raportti(teksti):
    with open("PokeDexSaved.txt","a", encoding="utf-8") as tiedosto:
        tiedosto.write(teksti + "\n")

def lue_historia() :
    try: 
        with open("PokeDexSaved.txt", "r", encoding="utf-8") as tiedosto:
            return tiedosto.readlines()
    except FileNotFoundError :
        return []


st.title("🔴 Pokédex Web 1.0 ⚪")
st.write("Etsi suosikkipokemonisi ja katso sen salaiset tiedot!")

st.sidebar.title(" Hakuhistoria ")

historia_rivit = lue_historia()

if len(historia_rivit) > 0:
    for rivi in historia_rivit:
        st.sidebar.write(rivi)
else:
    st.sidebar.write("Ei vielä tehtyjä hakuja, tee haku")


syote = st.text_input("Syötä Pokemonin nimi (esim. pikachu, charizard):")


if st.button("Etsi Pokemon!"):
    
    if syote != "":
        # Kutsutaan työntekijää!
        pokemon_data = hae_pokemon(syote.strip())
        st.success(f"Löytyi! Se on {pokemon_data['nimi']}")
        st.image(pokemon_data['kuva'])
        st.write(f"Pokemonisi pituus on :{pokemon_data['pituus']} cm")
        st.write(f"Pokemonisi paino on : {pokemon_data['paino']} kg")

        loki_teksti = f"Pokemon: {pokemon_data['nimi']}, Pituus: {pokemon_data['pituus']}, Paino: {pokemon_data['paino']}"

        tallenna_raportti(loki_teksti)


       
        
    else:
        st.warning("Kirjoita ensin jokin nimi!")