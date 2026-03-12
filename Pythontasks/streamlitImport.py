import streamlit as st
import requests

# ----------------------------------------------------
# 1. TYÖNTEKIJÄ (Tämä on TISMALLEEN sun eilen tekemä koodi!)
# ----------------------------------------------------
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


# ----------------------------------------------------
# 2. WEB-KÄYTTÖLIITTYMÄ (Nettisivun ulkoasu ja napit)
# ----------------------------------------------------

# Iso otsikko
st.title("🔮 Nimiennustaja Web 2.0")
st.write("Tekoäly arvaa kansallisuutesi pelkän etunimen perusteella!")

# Tekstikenttä (Kuin input, mutta selaimessa!)
syote = st.text_input("Syötä haluamasi nimi:")

# Nappi
if st.button("Ennusta!"):
    
    # Tarkistetaan, että käyttäjä oikeasti kirjoitti jotain (ettei kenttä ole tyhjä)
    if syote != "":
        
        # 1. Kutsutaan TYÖNTEKIJÄÄ aivan kuten eilen!
        raportti = hae_kansallisuus(syote.strip())
        st.success(raportti)
        
        
        st.balloons()
        
    else:
        st.warning("Hei, unohdit kirjoittaa nimen!")