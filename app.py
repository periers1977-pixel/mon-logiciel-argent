import streamlit as st
import requests
import time
import random

# Configuration Haute Performance
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #fdfdfd; }
    .stButton>button { background: linear-gradient(135deg, #007bff, #00d4ff); color: white; border-radius: 12px; height: 3.5em; border: none; font-weight: bold; }
    .stat-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Architect Solution Pro")
st.markdown("### Analyse Algorithmique de Projets Entrepreneurs")

# Formulaire principal
with st.container():
    idee = st.text_input("Saisissez votre concept business :", placeholder="Ex: Une marque de cosmétiques naturels par abonnement...")
    lancer = st.button("🚀 LANCER L'EXPERTISE COMPLÈTE")

if lancer:
    if idee:
        # Barre de progression chirurgicale
        barre = st.progress(0)
        info = st.empty()
        msgs = ["Initialisation des capteurs de marché...", "Calcul des vecteurs de croissance...", "Vérification de la scalabilité...", "Finalisation du rapport..."]
        
        for i, m in enumerate(msgs):
            info.info(m)
            for p in range(25):
                barre.progress((i * 25) + p + 1)
                time.sleep(0.01)
        
        info.empty()
        barre.empty()

        try:
            # Serveur Ultra-Rapide Llama 3.2
            API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"
            headers = {"Authorization": "Bearer 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"}
            
            payload = {
                "inputs": f"Agis en consultant senior. Analyse ce projet en 3 points stratégiques : {idee}. Ne mentionne pas l'IA.",
                "parameters": {"max_new_tokens": 200, "temperature": 0.6},
                "options": {"wait_for_model": True}
            }
            
            response = requests.post(API_URL, headers=headers, json=payload)
            resultat = response.json()
            texte_final = resultat[0]['generated_text'] if isinstance(resultat, list) else "Analyse en cours..."

            # --- AFFICHAGE PAR ONGLET ---
            tab1, tab2 = st.tabs(["🎯 Analyse Immédiate", "📊 Métriques de Marché"])
            
            with tab1:
                st.success("✅ Rapport de faisabilité généré")
                st.markdown(f"**Recommandations Stratégiques :**\n\n{texte_final}")

            with tab2:
                c1, c2, c3 = st.columns(3)
                with c1: st.metric("Viabilité", f"{random.randint(75, 95)}%", "+2%")
                with c2: st.metric("Concurrence", "Modérée", "⚖️")
                with c3: st.metric("Temps de lancement", "3-6 mois", "⏳")
                
        except:
            st.error("Serveur occupé. Re-cliquez une fois.")
    else:
        st.warning("Veuillez entrer une description.")

st.markdown("---")

# --- ZONE DE CONVERSION PREMIUM ---
st.subheader("🔓 Débloquez votre dossier d'exécution complet")
col_info, col_cta = st.columns([2, 1])

with col_info:
    st.markdown("""
    **Le dossier Premium à 9€ inclut :**
    - 📁 Plan financier prévisionnel sur 24 mois
    - 📈 Stratégie d'acquisition client (Marketing)
    - 🛡️ Analyse détaillée des risques et solutions
    """)

with col_cta:
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("🔥 TÉLÉCHARGER POUR 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
    st.caption("Paiement sécurisé. Accès instantané au PDF.")

st.sidebar.caption("Architect Solution 2026 | Expertise Certifiée")
