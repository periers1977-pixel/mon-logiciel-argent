import streamlit as st
import requests

# Configuration
st.set_page_config(page_title="Business Master AI", page_icon="🚀")

st.title("🚀 Mon Générateur de Business")
st.markdown("Tapez votre idée, je vous donne la stratégie pour réussir.")

# Saisie utilisateur
idee = st.text_input("Votre projet (ex: Vendre des cookies)", placeholder="Entrez votre idée ici...")

if st.button("Obtenir mon plan"):
    if idee:
        try:
            API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
            headers = {"Authorization": "Bearer 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"}
            
            payload = {
                "inputs": f"Donne 3 étapes pour lancer : {idee}",
                "parameters": {"max_new_tokens": 500},
                "options": {"wait_for_model": True}
            }
            
            with st.spinner("L'IA réfléchit..."):
                response = requests.post(API_URL, headers=headers, json=payload)
                resultat = response.json()
            
            if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                st.success("Voici votre plan :")
                st.write(resultat[0]['generated_text'])
            else:
                st.error("L'IA est occupée, réessayez dans quelques secondes.")
        except Exception as e:
            st.error("Erreur de connexion.")
    else:
        st.warning("Veuillez entrer une idée.")

st.markdown("---")
st.write("💰 **Pour le plan complet à 9€ :**")
st.link_button("CLIQUEZ ICI POUR PAYER", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
