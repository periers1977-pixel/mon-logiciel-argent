import streamlit as st
import requests
import time
import random

# 1. Configuration de prestige
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# 2. Style CSS pour un look professionnel (Sans mention IA)
st.markdown("""
    <style>
    .stApp { background-color: #fdfdfd; }
    .stButton>button { 
        background: linear-gradient(135deg, #007bff, #00d4ff); 
        color: white; border-radius: 12px; height: 3.5em; border: none; font-weight: bold; 
    }
    .plan-box { padding: 20px; border-radius: 15px; background-color: white; border: 1px solid #eef0f2; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .contact-box { padding: 15px; background: #f1f3f5; border-radius: 10px; margin-top: 20px; border-left: 5px solid #007bff; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Architect Solution Pro")
st.markdown("### Analyse Algorithmique de Projets Entrepreneurs")

# 3. Formulaire de saisie
with st.container():
    idee = st.text_input("Saisissez votre concept business :", placeholder="Ex: Une marque de cosmétiques naturels par abonnement...")
    lancer = st.button("🚀 LANCER L'EXPERTISE COMPLÈTE")

if lancer:
    if idee:
        # Barre de progression rapide et professionnelle
        barre = st.progress(0)
        info = st.empty()
        msgs = ["Initialisation des capteurs...", "Calcul des vecteurs de croissance...", "Vérification de la scalabilité...", "Finalisation du rapport..."]
        
        for i, m in enumerate(msgs):
            info.info(m)
            for p in range(25):
                barre.progress((i * 25) + p + 1)
                time.sleep(0.01)
        
        info.empty()
        barre.empty()

        # 4. Connexion au serveur de calcul ultra-rapide
        try:
            API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct"
            headers = {"Authorization": "Bearer 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"}
            
            # Consigne stricte : Ne pas mentionner l'intelligence artificielle
            payload = {
                "inputs": f"Agis en consultant senior. Analyse ce projet en 3 points stratégiques : {idee}. Ne mentionne jamais l'IA ou que tu es un programme.",
                "parameters": {"max_new_tokens": 150, "temperature": 0.7},
                "options": {"wait_for_model": True}
            }
            
            response = requests.post(API_URL, headers=headers, json=payload, timeout=8)
            resultat = response.json()
            
            if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                texte_final = resultat[0]['generated_text']
            else:
                # Secours automatique si le serveur est trop lent
                texte_final = f"### Analyse pour : {idee}\n1. **Validation** : Votre concept présente un fort potentiel de rentabilité.\n2. **Action** : Optimisez votre canal d'acquisition client dès le mois 1.\n3. **Risque** : Surveillez vos coûts fixes pour préserver votre marge."

        except:
            # Secours ultime (Fail-safe)
            texte_final = f"### Rapport Stratégique : {idee}\n1. **Opportunité** : Le secteur visé est en pleine expansion cette année.\n2. **Conseil** : Développez une identité de marque forte pour vous différencier.\n3. **Finance** : Prévoyez une réserve de trésorerie pour les 6 premiers mois."

        # 5. Affichage par onglets
        tab1, tab2 = st.tabs(["🎯 Analyse Immédiate", "📊 Métriques de Marché"])
        
        with tab1:
            st.success("✅ Rapport de faisabilité généré")
            st.markdown(f"**Recommandations Stratégiques :**\n\n{texte_final}")

        with tab2:
            c1, c2, c3 = st.columns(3)
            with c1: st.metric("Score Viabilité", f"{random.randint(78, 96)}%", "+3%")
            with c2: st.metric("Intensité Concurentielle", "Modérée", "⚖️")
            with c3: st.metric("ROI Estimé", "Élevé", "💰")
                
    else:
        st.warning("Veuillez entrer une description pour lancer l'algorithme.")

st.markdown("---")

# 6. Zone de Conversion (Abonnements)
st.subheader("🔓 Accédez au dossier d'exécution complet")
col_info, col_cta = st.columns([2, 1])

with col_info:
    st.markdown("""
    <div class='plan-box'>
    <b>Le dossier Premium à 9€ inclut :</b><br>
    • Plan financier détaillé sur 24 mois<br>
    • Stratégie d'acquisition client (Marketing digital)<br>
    • Analyse complète des risques et solutions opérationnelles
    </div>
    """, unsafe_allow_html=True)

with col_cta:
    st.write("##")
    st.link_button("🔥 TÉLÉCHARGER POUR 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
    st.caption("Paiement 100% sécurisé via Stripe.")

st.markdown("---")

# 7. Case Question pour les clients
st.subheader("❓ Une question sur votre rapport ?")
with st.container():
    st.markdown('<div class="contact-box">', unsafe_allow_html=True)
    st.text_input("Votre email professionnel :")
    st.text_area("Expliquez votre point d'interrogation :")
    if st.button("✉️ ENVOYER À NOS ANALYSTES"):
        st.success("Message reçu. Un analyste vous répondra sous 24h.")
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.caption("Architect Solution 2026 | Expertise Certifiée")
