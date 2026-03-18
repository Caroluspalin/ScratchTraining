import streamlit as st

st.title("🏅 Koodauksen MM-kisat")


voittajat = ["Santeri", "Linus Torvalds", "Bill Gates"]

st.write("Ja mitalit jaetaan seuraavasti:")


for numero, koodari in enumerate(voittajat):
    
   
    
    if numero == 0:
        st.write(f" Kultaa: {koodari}")
        
    elif numero == 1:
        st.write(f"Hopeaa {koodari}")
        
        
    elif numero == 2:
        st.write(f"Pronssia : {koodari}")