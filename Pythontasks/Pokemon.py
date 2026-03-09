import requests

def hae_pokemon(nimi):
    url = f"https://pokeapi.co/api/v2/pokemon/{nimi.lower()}"
    vastaus = requests.get(url)
    
    
    try:
        data = vastaus.json()
        
        return {
            "nimi": nimi.capitalize(),
            "pituus": data["height"],
            "paino": data["weight"],
            "kuva_url": data["sprites"]["front_default"]
        }
        
    except:
        return f"Hups! Pokemonia nimeltä '{nimi}' ei löytynyt."

# -----------------------------------------

kohde = input("Kirjoita haluamasi Pokemon: ")
print(hae_pokemon(kohde))