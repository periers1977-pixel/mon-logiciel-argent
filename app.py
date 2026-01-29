import streamlit as st
import requests
import time

# 1. Configuration Développeur
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# Style Pro (Aucune mention IA pour les clients)
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
st.markdown("### Interface de Développement & Analyse Stratégique")

# 2. Saisie du concept
idee = st.text_input("Saisissez votre concept business :", placeholder="Ex: Boutique e-commerce de montres...")
lancer = st.button("🚀 LANCER L'EXPERTISE")

if lancer:
    if idee:
        # Barre de progression pour l'utilisateur final
        barre = st.progress(0, text="Initialisation des protocoles...")
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        # 3. Connexion Prioritaire au Serveur
        try:
            # Utilisation du modèle le plus réactif
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
            headers = {"Authorization": "Bearer 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"}
            payload = {
                "inputs": f"Agis en consultant senior. Donne 3 conseils stratégiques pour : {idee}",
                "parameters": {"max_new_tokens": 150, "temperature": 0.7},
                "options": {"wait_for_model": True}
            }
            
            # On laisse 30 secondes au serveur pour répondre à votre demande
            with st.spinner("Récupération des données du serveur..."):
                response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
                resultat = response.json()
            
            # 4. AFFICHAGE DES RÉSULTATS (Onglet Développeur)
            st.success("✅ Expertise générée avec succès")
            
            if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                st.markdown("#### 🎯 Rapport Stratégique")
                st.write(resultat[0]['generated_text'])
            else:
                # Si le serveur répond autre chose que du texte, on affiche l'erreur ici
                st.error(f"⚠️ Alerte Développeur - Réponse inattendue : {resultat}")
                
        except Exception as e:
            # Si la connexion échoue (Internet, Clé bloquée, etc.)
            st.error(f"❌ Erreur de connexion au serveur : {e}")
            st.info("Astuce Développeur : Vérifiez votre connexion internet ou la validité de votre clé Hugging Face.")
    else:
        st.warning("Veuillez entrer une description de projet.")

st.markdown("---")

# 5. Zone de Conversion Client (9€)
st.subheader("🔓 Accéder au dossier d'exécution complet")
col_info, col_cta = st.columns([2, 1])

with col_info:
    st.markdown("""
    <div class='plan-box'>
    <b>Le dossier Premium à 9€ inclut :</b><br>
    • Plan financier prévisionnel sur 24 mois<br>
    • Stratégie d'acquisition client détaillée<br>
    • Analyse complète des risques sectoriels
    </div>
    """, unsafe_allow_html=True)

with col_cta:
    st.write("##")
    st.link_button("🔥 TÉLÉCHARGER POUR 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.sidebar.caption("Architect Solution 2026 | Mode Développeur Actif")
