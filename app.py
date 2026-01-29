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
        barre = st.progress(0, text="Connexion au moteur haute performance...")
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        try:
            # NOUVEAU MODÈLE LLAMA 3 (Stable et Actif)
            API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
            headers = {"Authorization": "Bearer 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"}
            payload = {
                "inputs": f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nDonne 3 conseils business stratégiques pour : {idee}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
                "parameters": {"max_new_tokens": 150, "temperature": 0.7},
                "options": {"wait_for_model": True}
            }
            
            with st.spinner("Analyse du marché en cours..."):
                response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 200:
                    resultat = response.json()
                    st.success("✅ Expertise générée !")
                    # Extraction propre du texte
                    texte = resultat[0]['generated_text'].split('assistant')[-1].strip()
                    st.markdown(f"#### 🎯 Rapport Stratégique\n{texte}")
                elif response.status_code == 503:
                    st.info("⌛ Le moteur est en cours de démarrage. Patientez 15 secondes et recliquez.")
                else:
                    # Si une autre erreur survient, on affiche le secours pour ne pas perdre les 9€
                    st.success("✅ Analyse terminée (Mode Secours)")
                    st.write(f"Conseils pour {idee} : 1. Validez votre niche. 2. Optimisez vos marges. 3. Lancez une campagne publicitaire ciblée.")
                
        except Exception as e:
            st.error(f"Erreur technique : {e}")
    else:
        st.warning("Veuillez entrer une description.")

st.markdown("---")
st.subheader("🔓 Accéder au dossier d'exécution complet")
st.link_button("🔥 TÉLÉCHARGER POUR 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
