import requests

# 1. TYÖNTEKIJÄ: Hakee nimen tiedot netistä
def hae_kansallisuus(nimi):
    url = f"https://api.nationalize.io/?name={nimi}"
    
    try:
        vastaus = requests.get(url)
        data = vastaus.json()
        return data
        # TEHTÄVÄ 1:
        # A) Tee requests.get(url, timeout=3)
        # B) Pura data .json() komennolla
        # C) Palauta KOKO sanakirja (eli return data)
        
    except Exception:
        # Jos netti pätkii, palautetaan None
        return None


# 2. PÄÄLLIKKÖ: Analysoi datan ja tekee raportin
def analysoi_nimi(nimi):
    # Päällikkö pyytää työntekijältä datan
    data = hae_kansallisuus(nimi)

    # Tarkistetaan, että data löytyi JA että country-listalla on sisältöä!
    if data != None and len(data["country"]) > 0:
        
        # TÄSSÄ ON UUSI JUTTU! Otetaan listan ensimmäinen alkio [0]
        paras_arvaus = data["country"][0]["country_id"]
        
        # Otetaan todennäköisyys ja kerrotaan se 100:lla (esim 0.98 * 100 = 98.0)
        prosentti = data["country"][0]["probability"] * 100

        return f"Nimi {nimi} on {prosentti} % todennäköisyydellä maasta: {paras_arvaus}"
        
        # TEHTÄVÄ 2:
        # Palauta (return) tyylikäs f-string, esim:
        # "Nimi Matti on 98.0 % todennäköisyydellä maasta: FI"
        
        
    else:
        return f"Nimelle '{nimi}' ei löytynyt arvausta tai verkkovirhe."


# 3. PÄÄOHJELMA: Ikuinen silmukka
print("Tervetuloa Nimiennustajaan! (Kirjoita 'lopeta' sammuttaaksesi)")

while True:
    syote = input("\nSyötä haluamasi nimi: ").strip()

    if syote.lower() == "lopeta":
        print("Heippa")
        break

    raportti = analysoi_nimi(syote)
    print(raportti)




# TEHTÄVÄ 3: 
# Rakenna tähän se tuttu 'while True:' -silmukka!
# A) Kysy nimeä (muista \n ja .strip())
# B) Tarkista onko syöte "lopeta" -> break
# C) Printtaa tulos kutsumalla Päällikköä: print(analysoi_nimi(syote))