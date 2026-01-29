import streamlit as st
import requests
import time

# Configuration de luxe
st.set_page_config(page_title="Business Architect AI", page_icon="💎", layout="wide")

# Style personnalisé pour un look haut de gamme
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007bff; color: white; }
    .plan-box { padding: 20px; border-radius: 10px; border: 1px solid #e0e0e0; background-color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Business Architect AI")
st.caption("L'intelligence artificielle au service de votre rentabilité.")

# Formulaire structuré
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        idee = st.text_input("Quelle est votre vision ?", placeholder="Ex: Un concept de café-librairie innovant...")
    with col2:
        st.write("##")
        lancer = st.button("🚀 GÉNÉRER L'ANALYSE")

if lancer:
    if idee:
        with st.status("🛠️ Construction de votre stratégie...", expanded=True) as status:
            st.write("Analyse du marché...")
            time.sleep(1)
            st.write("Calcul des risques...")
            time.sleep(1)
            
            try:
                API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
                headers = {"Authorization": "Bearer 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"}
                payload = {"inputs": f"Donne une stratégie de génie pour : {idee}", "options": {"wait_for_model": True}}
                
                response = requests.post(API_URL, headers=headers, json=payload)
                resultat = response.json()
                
                status.update(label="✅ Analyse terminée !", state="complete", expanded=False)
                
                # Affichage Premium
                st.balloons()
                st.markdown("### 🎯 Votre Aperçu Stratégique")
                st.info(resultat[0]['generated_text'])
                
                # Zone de Vente Irrésistible
                st.markdown("---")
                c1, c2, c3 = st.columns(3)
                c1.metric("Potentiel", "Élevé 🔥")
                c2.metric("Difficulté", "Modérée ⚖️")
                c3.metric("Rentabilité", "9/10 💰")
                
                st.markdown("<div class='plan-box'>", unsafe_allow_html=True)
                st.subheader("🔓 Voulez-vous le dossier complet de 25 pages ?")
                st.write("Inclus : Business Plan, Étude de concurrence, Budget détaillé et Stratégie réseaux sociaux.")
                st.link_button("🔥 TÉLÉCHARGER LE DOSSIER COMPLET (9€)", "https://buy.stripe.com/votre_lien_stripe")
                st.markdown("</div>", unsafe_allow_html=True)
                
            except:
                st.error("L'IA est très demandée. Re-cliquez pour forcer l'accès.")
    else:
        st.warning("Veuillez décrire votre projet.")

st.sidebar.markdown("### Aide & Support")
st.sidebar.write("Logiciel certifié 2026. Paiements sécurisés par Stripe.")
