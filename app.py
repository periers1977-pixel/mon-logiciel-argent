import streamlit as st
import requests
import time

# Configuration Architect Pro
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
        barre = st.progress(0, text="Connexion au flux de données...")
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        try:
            # URL MISE À JOUR (Évite l'erreur 410)
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
            headers = {"Authorization": "Bearer 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"}
            payload = {
                "inputs": f"<s>[INST] Donne 3 conseils business pour : {idee} [/INST]",
                "parameters": {"max_new_tokens": 150},
                "options": {"wait_for_model": True}
            }
            
            with st.spinner("Analyse en cours..."):
                response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
                
                # Gestion des codes de réponse
                if response.status_code == 200:
                    resultat = response.json()
                    st.success("✅ Expertise générée !")
                    # Nettoyage de la réponse pour n'afficher que le conseil
                    texte = resultat[0]['generated_text'].split('[/INST]')[-1]
                    st.markdown(f"#### 🎯 Rapport Stratégique\n{texte}")
                elif response.status_code == 503:
                    st.info("⌛ Le serveur se réveille (503). Patientez 10 secondes et recliquez.")
                else:
                    st.error(f"Erreur serveur ({response.status_code}). Essayez de rafraîchir la page.")
                
        except Exception as e:
            st.error(f"Erreur de flux : {e}")
    else:
        st.warning("Veuillez entrer une description.")

st.markdown("---")
st.subheader("🔓 Accéder au dossier d'exécution complet")
st.link_button("🔥 TÉLÉCHARGER POUR 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
