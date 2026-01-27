import streamlit as st

st.title("🚀 Mon Générateur de Business")
st.write("Tapez votre idée, je vous donne la stratégie.")

idee = st.text_input("Votre projet (ex: Vendre des cookies)")

if st.button("Obtenir mon plan"):
    st.success(f"Voici comment réussir dans : {idee}")
    st.write("1. Créez un compte TikTok.")
    st.write("2. Montrez la fabrication en vidéo.")
    st.write("3. Vendez via un lien en bio.")

st.markdown("---")
st.write("💰 Pour le plan complet à 9€ :")
st.markdown("[CLIQUEZ ICI POUR PAYER](https://votre-lien-stripe-ici)")