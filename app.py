import streamlit as st
import requests

st.title("🚀 Mon Générateur de Business")
st.write("Tapez votre idée, je vous donne la stratégie.")

idee = st.text_input("Votre projet (ex: Vendre des cookies)")

if st.button("Obtenir mon plan"):
    if idee:
        try:
            # Connexion à l'IA avec ta clé secrète
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
            headers = {"Authorization": f"Bearer {st.secrets['hf_votre_cle_gratuite']}"}
            
            # Question personnalisée pour l'IA
            prompt = f"Donne 3 étapes différentes et précises pour ce projet : {idee}"
            
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            resultat = response.json()
            
            st.success(f"Voici le plan pour : {idee}")
            # Affichage de la réponse unique de l'IA
            st.write(resultat[0]['generated_text'])
            
        except Exception:
            st.error("L'IA est occupée, réessayez dans 5 secondes !")
    else:
        st.warning("Écrivez une idée d'abord !")

st.markdown("---")
st.write("💰 Pour le plan complet à 9€ :")
st.markdown("[CLIQUEZ ICI POUR PAYER](https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00)")
