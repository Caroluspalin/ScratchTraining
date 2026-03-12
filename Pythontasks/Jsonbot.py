import streamlit as st
import json
import os 



def lataa_aivot():
    
    if os.path.exists("aivot.json"):
       
        with open("aivot.json", "r", encoding="utf-8") as tiedosto:
            return json.load(tiedosto)
    else:
        
        return {"moro": "No morjesta pöytään!", "kuka olet": "Olen sun koodaama JSON-botti."}

def tallenna_aivot(data):
    
    with open("aivot.json", "w", encoding="utf-8") as tiedosto:
        json.dump(data, tiedosto, indent=4)


st.title("🤖 Oma JSON-Botti")
st.write("Tämä botti ei käytä nettiä, vaan lukee vastaukset omista JSON-aivoistaan!")


aivot = lataa_aivot()


st.subheader("💬 Juttele botille")
kysymys = st.text_input("Kysy jotain (esim. 'moro'):").strip().lower()

if st.button("Kysy"):
    if kysymys != "":
        if kysymys in aivot:
            st.success(aivot[kysymys])
        else:
            st.error("En tiedä vastausta, opeta minulle!")
        

st.markdown("---") 

st.subheader("🧠 Opeta botille uusi asia")
uusi_kysymys = st.text_input("Mihin kysymykseen haluat botin vastaavan?").strip().lower()
uusi_vastaus = st.text_input("Mitä botin pitäisi vastata?")

if st.button("Tallenna uusi tieto"):
    if uusi_kysymys != "" and uusi_vastaus != "":
        aivot[uusi_kysymys] = uusi_vastaus
        tallenna_aivot(aivot)
        st.success("uusi tieto tallennetu aivoihin!")
        
       
    else:
        st.warning("Täytä molemmat kentät!")