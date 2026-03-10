import requests

# Työntekijä 1
def hae_koordinaatit(kaupunki):
    sijainnit = {"vantaa": {"lat": 60.29, "lon": 25.04}, "helsinki": {"lat": 60.17, "lon": 24.94}, "tampere": {"lat": 61.50, "lon": 23.79}}
    return sijainnit.get(kaupunki.lower()) 

# Työntekijä 2
def hae_lampotila(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    vastaus = requests.get(url)
    return vastaus.json()["current_weather"]["temperature"]
  
# Päällikkö
def kaupungin_saa_raportti(kaupunki):
    sijainti = hae_koordinaatit(kaupunki)
    if sijainti != None: 
        lampotila = hae_lampotila(sijainti["lat"], sijainti["lon"])
        return f"Lämpötila {kaupunki.capitalize()}lla on {lampotila} astetta."
    else: 
        return f"Kaupunkia '{kaupunki}' ei löytynyt järjestelmästä."


print("Tervetuloa Sää-automaattiin! (Kirjoita 'lopeta' sammuttaaksesi ohjelman)")

# loputon looppi
while True: 
    
    
    kohde = input("\nSyötä kaupunki: ").strip()
    
    
    if kohde.lower() == "lopeta":
        print("Sammutetaan sää-automaatti. Heippa!")
        break 
    
    print(kaupungin_saa_raportti(kohde))
    