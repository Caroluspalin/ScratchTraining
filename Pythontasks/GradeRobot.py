import streamlit as st

st.title("🏫 Kokeiden tarkastus-robotti")
st.write("Etsitään huippuoppilaat ja uusintaan joutuvat!")

pisteet = [75, 100, 42, 100, 88, 99, 100, 30]

for indeksi, tulos in enumerate(pisteet):
    
    penkki = indeksi + 1
    
    if tulos == 100:
        st.success(f"Penkki {penkki}: Täydellinen suoritus!")
    
    elif tulos < 50:
        st.error(f"Penkki {penkki} : Uusintaan! Hylätty tuloksesi oli {tulos}")
    
    else:
        st.write(f"Penkki {penkki} : Läpi meni.")
