import requests

def hae_vantaan_saa():
    # Vantaan koordinaatit
    url = "https://api.open-meteo.com/v1/forecast?latitude=60.29&longitude=25.04&current_weather=true"
    
    vastaus = requests.get(url)
    data = vastaus.json()

    
    
    
    # 1. Etsi data-sanakirjasta ensin "current_weather" ja sen sisältä "temperature"
    lampotila = data["current_weather"]["temperature"] # Korvaa nolla oikealla ketjutuksella!
    
    # 2. Palauta f-string, joka yhdistää tekstin ja lämpötilan
    return f"Vantaalla on juuri nyt {lampotila} astetta."

# Kutsutaan funktiota:
print(hae_vantaan_saa())