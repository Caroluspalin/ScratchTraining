# Tässä on meidän feikki-API:n palauttama data:
suomen_tilastot = [
    {
        "kaupunki": "Vantaa",
        "vuodet": {
            "2018": 228166,
            "2023": 247375
        }
    },
    {
        "kaupunki": "Espoo",
        "vuodet": {
            "2018": 283632,
            "2023": 314024
        }
    },
    {
        "kaupunki": "Tampere",
        "vuodet": {
             "2018": 251943,
             "2023": 291753
        }
    }
]

def laske_kasvu(tilastot, kaupungin_nimi):
            for tilasto in tilastot:
                    if tilasto["kaupunki"] == kaupungin_nimi:
                            kasvu = tilasto["vuodet"]["2023"] - tilasto["vuodet"]["2018"]
                            return f"Kaupungin väestö {kaupungin_nimi}lla kasvoi {kasvu} viimeisen 5 vuoden aikana"
            
            return "Kaupunkia ei löytynyt."

print(laske_kasvu(suomen_tilastot, "Vantaa"))
print(laske_kasvu(suomen_tilastot, "Espoo"))
print(laske_kasvu(suomen_tilastot, "Tampere")) # Tämän pitäisi tulostaa "Kaupunkia ei löytynyt."