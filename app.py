import streamlit as st
import requests

st.set_page_config(page_title="Business Master AI", page_icon="🚀")
st.title("🚀 Mon Générateur de Business")

idee = st.text_input("Votre projet", placeholder="Entrez votre idée...")

if st.button("Obtenir mon plan"):
    if idee:
        try:
            # Passage sur un modèle 10x plus rapide
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
            headers = {"Authorization": "Bearer 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"}
            
            # Prompt ultra-court pour une réponse instantanée
            payload = {
                "inputs": f"Donne 3 conseils rapides pour : {idee}",
                "parameters": {"max_new_tokens": 100},
                "options": {"wait_for_model": True}
            }
            
            with st.spinner("Réponse immédiate en cours..."):
                response = requests.post(API_URL, headers=headers, json=payload)
                resultat = response.json()
                
                if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                    st.success("Succès !")
                    st.write(resultat[0]['generated_text'])
                else:
                    st.info("Serveur en cours d'accélération... Re-cliquez une fois.")
        except:
            st.error("Erreur. Réessayez.")
    else:
        st.warning("Entrez une idée.")

st.markdown("---")
st.link_button("🔥 PAYER 9€ POUR LE PLAN COMPLET", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
