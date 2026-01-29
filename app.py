import streamlit as st
import time

# 1. Configuration Pro
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

st.title("💎 Architect Solution Pro")

# 2. Entrée utilisateur
idee = st.text_input("Saisissez votre concept business :")
lancer = st.button("🚀 LANCER L'EXPERTISE")

if lancer:
    if idee:
        barre = st.progress(0, text="Génération de l'expertise...")
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        st.success("✅ Expertise terminée")
        
        # Ce que tout le monde voit (Aperçu gratuit)
        st.markdown(f"### 🎯 Analyse pour : {idee}")
        st.write("Votre projet est viable. Pour accéder aux 25 pages de détails, veuillez procéder au paiement.")

st.sidebar.markdown("---")
# 3. LE COFFRE-FORT DÉVELOPPEUR (Seul vous avez le code)
st.sidebar.subheader("🔒 Accès Administrateur")
code_secret = st.sidebar.text_input("Entrez votre code secret :", type="password")

if code_secret == "23111977": # Changez ce mot de passe
    st.sidebar.success("Accès Développeur Activé")
    st.markdown("---")
    st.header("📂 ZONE DE TÉLÉCHARGEMENT PROPRIÉTAIRE")
    st.write("Voici le dossier de 25 pages réservé au créateur du logiciel.")
    
    # Le dossier complet s'affiche ici uniquement pour vous
    st.download_button(
        label="📄 TÉLÉCHARGER LE DOSSIER DE 25 PAGES",
        data=f"DOSSIER COMPLET - PROJET {idee}\n\n[Contenu des 25 pages de stratégie financière et marketing...]",
        file_name=f"Dossier_Premium_{idee}.txt",
        mime="text/plain"
    )
else:
    if code_secret != "":
        st.sidebar.error("Code incorrect")

st.markdown("---")
# Bouton Stripe pour les clients (Eux n'ont pas votre code)
st.subheader("💳 Espace Client")
st.link_button("🔥 ACHETER LE DOSSIER COMPLET (9€)", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
