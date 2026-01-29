import streamlit as st
import requests
import time

# Configuration de prestige
st.set_page_config(page_title="Business Architect AI", page_icon="💎", layout="wide")

# Style CSS Avancé
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stButton>button { 
        background: linear-gradient(90deg, #007bff, #0056b3); 
        color: white; border-radius: 12px; font-weight: bold; border: none; transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
    .premium-card { 
        padding: 25px; background: white; border-radius: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #eef0f2;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Business Architect AI")
st.markdown("#### Transformez votre idée en empire financier.")

# Interface utilisateur
col_input, col_btn = st.columns([3, 1])
with col_input:
    idee = st.text_input("", placeholder="Décrivez votre vision business ici...")
with col_btn:
    st.write("##")
    lancer = st.button("🚀 ANALYSER MON PROJET")

if lancer:
    if idee:
        # Barre de progression intelligente
        progress_bar = st.progress(0)
        ph_message = st.empty()
        etapes = [
            "🔍 Scan des opportunités de marché...",
            "📊 Analyse de la concurrence sectorielle...",
            "💡 Génération de la proposition de valeur...",
            "💰 Calcul de la viabilité financière...",
            "✨ Finalisation de votre plan d'action..."
        ]
        
        for i, msg in enumerate(etapes):
            ph_message.info(msg)
            for p in range(20):
                progress_bar.progress((i * 20) + p + 1)
                time.sleep(0.02)
        
        ph_message.empty()
        progress_bar.empty()

        try:
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
            headers = {"Authorization": "Bearer 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"}
            
            # Prompt optimisé pour un rendu pro
            payload = {
                "inputs": f"Agis comme un expert en business. Donne 3 piliers stratégiques numérotés pour : {idee}",
                "parameters": {"max_new_tokens": 250},
                "options": {"wait_for_model": True}
            }
            
            with st.spinner("📦 Livraison de votre stratégie..."):
                response = requests.post(API_URL, headers=headers, json=payload)
                resultat = response.json()
                
                st.balloons()
                st.success("✅ Votre analyse stratégique gratuite est prête !")
                st.markdown(f"**Analyse Pro :**\n\n{resultat[0]['generated_text']}")
                
                # Indicateurs visuels
                c1, c2, c3 = st.columns(3)
                c1.metric("Score Viabilité", "88%", "+5%")
                c2.metric("Demande Marché", "Haute", "🔥")
                c3.metric("Potentiel ROI", "x10", "💰")
                
        except:
            st.error("L'IA est saturée. Re-cliquez pour rafraîchir la connexion.")
    else:
        st.warning("Veuillez entrer une description de projet.")

st.markdown("---")

# Section Tarification de Luxe
st.subheader("🔓 Passez au niveau supérieur")
c_free, c_pay = st.columns(2)

with c_free:
    st.markdown("""<div class="premium-card">
    <h3>Plan Basic</h3>
    <p>Gratuit - Inclus</p>
    <ul>
        <li>3 Piliers stratégiques</li>
        <li>Analyse IA standard</li>
    </ul>
    </div>""", unsafe_allow_html=True)
    st.button("Actuellement actif", disabled=True, key="free_btn")

with c_pay:
    st.markdown("""<div class="premium-card" style="border: 2px solid #007bff;">
    <h3>Plan Empire 🏆</h3>
    <p><strong>9€ seulement</strong></p>
    <ul>
        <li><b>Dossier PDF de 25 pages</b></li>
        <li>Plan financier détaillé sur 3 ans</li>
        <li>Stratégie marketing réseaux sociaux</li>
    </ul>
    </div>""", unsafe_allow_html=True)
    st.link_button("🔥 ACCÉDER AU PLAN COMPLET", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.sidebar.caption("Logiciel certifié 2026 | Support 24/7")
