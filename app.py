import streamlit as st
import requests

st.set_page_config(page_title="Business Master AI", page_icon="🚀")
st.title("🚀 Mon Générateur de Business")

idee = st.text_input("Votre projet", placeholder="Entrez votre idée...")

if st.button("Obtenir mon plan"):
    if idee:
        try:
            # Utilisation du modèle 'Mistral-7B-v0.3' qui est ultra-réactif
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
            headers = {"Authorization": "Bearer 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"}
            
            # Paramètres optimisés pour la vitesse (max_new_tokens réduit)
            payload = {
                "inputs": f"Donne 3 conseils éclairs pour : {idee}",
                "parameters": {"max_new_tokens": 80, "temperature": 0.7},
                "options": {"wait_for_model": True}
            }
            
            with st.spinner("Analyse ultra-rapide..."):
                response = requests.post(API_URL, headers=headers, json=payload)
                resultat = response.json()
                
                if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                    st.success("Plan prêt !")
                    st.write(resultat[0]['generated_text'])
        except:
            st.error("Petit bug de vitesse, recliquez une fois !")
    else:
        st.warning("Veuillez entrer une idée.")

st.markdown("---")
st.link_button("🔥 PAYER 9€ POUR LE PLAN COMPLET", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
