import streamlit as st
import requests
import time

# Configuration Développeur
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #fdfdfd; }
    .stButton>button { 
        background: linear-gradient(135deg, #007bff, #00d4ff); 
        color: white; border-radius: 12px; height: 3.5em; font-weight: bold; 
    }
    .plan-box { padding: 20px; border-radius: 15px; background-color: white; border: 1px solid #eef0f2; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Architect Solution Pro")

idee = st.text_input("Saisissez votre concept business :", placeholder="Ex: Boutique e-commerce...")
lancer = st.button("🚀 LANCER L'EXPERTISE")

if lancer:
    if idee:
        barre = st.progress(0, text="Connexion au nouveau routeur...")
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        try:
            # NOUVELLE URL DU ROUTEUR (Correction de l'erreur)
            API_URL = "https://router.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
            headers = {"Authorization": "Bearer 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"}
            payload = {
                "inputs": f"Agis en consultant senior. Donne 3 conseils stratégiques pour : {idee}",
                "parameters": {"max_new_tokens": 150},
                "options": {"wait_for_model": True}
            }
            
            with st.spinner("Analyse en cours via le routeur sécurisé..."):
                response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
                resultat = response.json()
            
            if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                st.success("✅ Expertise générée avec succès")
                st.markdown("#### 🎯 Rapport Stratégique")
                st.write(resultat[0]['generated_text'])
            else:
                st.error(f"Détail technique : {resultat}")
                
        except Exception as e:
            st.error(f"Erreur de connexion : {e}")
    else:
        st.warning("Veuillez entrer une description.")

st.markdown("---")
st.subheader("🔓 Accéder au dossier d'exécution complet")
st.link_button("🔥 TÉLÉCHARGER POUR 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
