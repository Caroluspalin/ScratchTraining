import requests

def hae_koordinaatit(kaupunki):
    sijainnit = {
        "vantaa": {"lat": 60.29, "lon": 25.04},
        "helsinki": {"lat": 60.17, "lon": 24.94},
        "tampere": {"lat": 61.50, "lon": 23.79}
    }
    
    return sijainnit.get(kaupunki.lower()) 


def hae_lampotila(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    vastaus = requests.get(url)
    data = vastaus.json()
    
    return data["current_weather"]["temperature"]
  

def kaupungin_saa_raportti():

    kaupunki = input("Syötä haluamasi kaupunki").strip()

    sijainti = hae_koordinaatit(kaupunki)

    if sijainti != None: 
        lati = sijainti["lat"]
        loni = sijainti["lon"]

        lampotila = hae_lampotila(lati, loni)
        return f"Lämpötila {kaupunki}lla on {lampotila} astetta."

    else: 
        return print("kaupunkia {kaupunki} ei löytynyt")
        

