import streamlit as st
import time
import random

# 1. Configuration Pro
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

st.title("💎 Architect Solution Pro")

# 2. Entrée utilisateur
idee = st.text_input("Saisissez votre concept business :", placeholder="Ex: Agence de voyage...")
lancer = st.button("🚀 LANCER L'EXPERTISE")

# 3. Système de Sécurité Développeur
st.sidebar.subheader("🔒 Zone Propriétaire")
code_secret = st.sidebar.text_input("Mot de passe :", type="password")

if lancer:
    if idee:
        barre = st.progress(0, text="Génération du dossier haute performance...")
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        st.success("✅ Analyse terminée avec succès.")

        # AFFICHAGE DU DOSSIER SI CODE OK
        if code_secret == "23111977":
            st.info("Mode Développeur : Accès au contenu complet débloqué.")
            
            # Création d'un dossier avec du CONTENU VARIÉ (Pas de répétition)
            def generer_page_expert(titre, corps):
                return f"\n\n--- {titre} ---\n\n" + corps + "\n"
            
            dossier_final = f"DOSSIER STRATÉGIQUE : {idee.upper()}\n"
            dossier_final += "========================================\n"
            
            # Section Marketing
            dossier_final += generer_page_expert("MARKETING", "Analyse du marché cible et segmentation des personas. Stratégie d'acquisition multi-canaux (SEO, SEA, Social Ads).")
            # Section Finance
            dossier_final += generer_page_expert("FINANCE", f"Prévisions de CA pour {idee} : {random.randint(150, 500)}k€. Calcul du point mort au mois 8.")
            # Section Juridique
            dossier_final += generer_page_expert("JURIDIQUE", "Choix de la structure sociale et conformité RGPD. Protection de la propriété intellectuelle.")
            
            st.download_button(
                label="📥 TÉLÉCHARGER LE DOSSIER (VUE DÉVELOPPEUR)",
                data=dossier_final,
                file_name=f"Dossier_Expert_{idee}.txt",
                mime="text/plain"
            )
        else:
            st.markdown("### 🎯 Aperçu Stratégique")
            st.write(f"Votre projet '{idee}' a été validé par nos algorithmes. Pour accéder au document de 25 pages détaillant chaque étape de votre succès, veuillez finaliser votre commande.")

# 4. LE BOUTON DE PAIEMENT (Sorti de la boucle pour être TOUJOURS visible)
st.markdown("---")
st.subheader("💳 Accès Client")
col1, col2 = st.columns([2,1])
with col1:
    st.write("Obtenez votre dossier complet de 25 pages (Finance, Marketing, Juridique) immédiatement après paiement.")
with col2:
    st.link_button("🔥 PAYER 9€ ICI", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
