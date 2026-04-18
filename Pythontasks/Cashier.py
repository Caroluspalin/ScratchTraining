def laske_yhteensa(tuotteet):
    yhteensa = 0
    for  tuote in tuotteet:
        hinta = tuote["hinta"]
        maara = tuote["maara"]
        yhteensa = yhteensa + (hinta * maara)
    return round(yhteensa, 2)

 
 
tuotteet = [
    {"nimi": "Maito", "hinta": 1.50, "maara": 2},
    {"nimi": "Leipä", "hinta": 2.80, "maara": 1},
    {"nimi": "Juusto", "hinta": 4.20, "maara": 3},
]



# Tehtävä 2
print("\n--- Tehtävä 2 ---")
print(laske_yhteensa(tuotteet))       # → 18.40