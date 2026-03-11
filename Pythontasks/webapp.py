import streamlit as st

st.title("Minun Eka Nettisivu! 🚀")
st.write("Tervetuloa web-koodauksen maailmaan. Tämä ei ole enää mikään musta terminaali!")


nimi = st.text_input("Mikä sun nimi on?")

if st.button("Lähetä"):
    st.success(f"Moro {nimi}! Sä koodasit just toimivan nettisivun.")
    st.balloons()