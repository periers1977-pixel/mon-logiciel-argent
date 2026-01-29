import streamlit as st
import requests

st.set_page_config(page_title="Business Master AI", page_icon="🚀")
st.title("🚀 Mon Générateur de Business")

# Champ de saisie
idee = st.text_input("Votre projet", placeholder="Ex: Vendre des cookies")

# Bouton d'action
if st.button("OBTENIR MON PLAN MAINTENANT"):
    if idee:
        st.info("L'IA prépare votre réponse... veuillez patienter 10 secondes.")
        try:
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
            headers = {"Authorization": "Bearer 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"}
            payload = {"inputs": f"Donne 3 conseils pour : {idee}", "options": {"wait_for_model": True}}
            
            response = requests.post(API_URL, headers=headers, json=payload)
            resultat = response.json()
            
            if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                st.success("Voici votre plan :")
                st.write(resultat[0]['generated_text'])
            else:
                st.warning("L'IA chauffe... Re-cliquez une fois sur le bouton.")
        except:
            st.error("Erreur de connexion. Vérifiez votre internet.")
    else:
        st.error("Veuillez d'abord taper votre idée !")

st.markdown("---")
st.link_button("🔥 PAYER 9€ POUR LE PLAN COMPLET", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
