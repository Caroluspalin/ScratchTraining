import streamlit as st

st.title("📦 Varastonhallinta")
st.write("Siirretään tavarat listasta nopeaan sanakirjaan!")

# Meillä on lista tavaroita. Niiden indeksi (0, 1, 2...) on niiden "hyllynumero".
tavarat = ["Kultakolikot", "Taikajuoma", "Miekka", "Lohikäärmeen muna"]

# 1. Luodaan täysin tyhjä sanakirja (meidän "muistivihko")
hyllypaikat = {}

# 2. Käydään lista läpi enumeratella
for hylly_numero, esine in enumerate(tavarat):
    
    # TEHTÄVÄ:
    # Tallenna 'esine' sanakirjaan AVAIMEKSI, ja sen 'hylly_numero' ARVOKSI.
    # Muistatko miten botin aivoihin tallennettiin uusi sana? Tismalleen samalla logiikalla!
    # aivot[kysymys] = vastaus ---> hyllypaikat[???] = ???
    
    pass # Poista tämä ja iske koodi tähän!


# ---------------------------------------------------------
# LOPPUTESTI (Tämä koodi testaa, onnistuitko!)
st.write("Koko varaston kirjanpito näyttää nyt tältä:")
st.json(hyllypaikat) # st.json on hieno komento, joka piirtää sanakirjat visuaalisesti!

st.markdown("---")
# Kokeillaan hakea Miekka suoraan sanakirjasta (tämän pitäisi tulostaa numero 2)
if "Miekka" in hyllypaikat:
    st.success(f"Miekka löytyi heti hyllyltä numero: {hyllypaikat['Miekka']}")