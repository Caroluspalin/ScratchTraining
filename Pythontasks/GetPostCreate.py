import requests

def hae_kansallisuus(nimi):
    url = f"https://api.nationalize.io/?name={nimi}"
    try:
        data = requests.get(url, timeout=3).json()
        if len(data["country"]) > 0:
            paras_arvaus = data["country"][0]["country_id"]
            prosentti = data["country"][0]["probability"] * 100
            return f"Nimi {nimi.capitalize()} on {prosentti:.1f} % todennäköisyydellä maasta: {paras_arvaus}"
        else:
            return f"Nimelle {nimi} ei löytynyt arvausta."
    except Exception:
        return f"Verkkovirhe etsittäessä nimeä {nimi}."


def tallenna_raportti(teksti):
    with open("nimiloki.txt", "a", encoding="utf-8") as tiedosto:
        tiedosto.write(teksti + "\n")



print("Tervetuloa Ennustaja 2.0:aan! (kirjoita 'lopeta' sulkeaksesi)")

while True:
    syote = input("\nSyötä haluamasi nimi: ")
    
    if syote == "lopeta":
        print("Se on moro")
        break
    raportti = hae_kansallisuus(syote)
    print(raportti)
    tallenna_raportti(raportti)