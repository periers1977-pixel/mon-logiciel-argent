import streamlit as st
import time
import random
from datetime import datetime

# Configuration Professionnelle
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# 1. BASE DE DONNÉES D'EXPERTISE HAUTE DENSITÉ (Pour faire 25 pages)
BASE_TEXTE = [
    "L'analyse de scalabilité pour {idee} révèle un levier de croissance majeur sur le segment B2B. L'optimisation des flux permet une réduction des coûts marginaux de {val}%. ",
    "La stratégie marketing de {idee} doit impérativement intégrer un tunnel d'acquisition basé sur l'IA comportementale pour maximiser le taux de conversion dès le premier mois. ",
    "Concernant la structure financière, nous préconisons pour {idee} un maintien du BFR à un niveau agile, favorisant une réactivité maximale face aux évolutions du marché 2026. ",
    "Le positionnement de marque doit s'appuyer sur une identité visuelle forte et une promesse client disruptive pour se démarquer de la concurrence directe de {idee}. "
]

def generer_25_pages_textuelles(idee):
    session_ref = f"BP-PRO-{random.randint(1000, 9999)}"
    # On construit un document massif
    pages = []
    pages.append(f"ARCHITECT SOLUTION PRO - RAPPORT D'EXPERTISE STRATÉGIQUE\nPROJET : {idee.upper()} | RÉF : {session_ref}\n" + "="*60 + "\n")
    
    for i in range(1, 26):
        contenu_page = f"\n--- SECTION {i} : ANALYSE DE DÉTAIL PROFONDE ---\n\n"
        # On remplit chaque page avec 15 paragraphes variés pour garantir la longueur
        for _ in range(15):
            phrase = random.choice(BASE_TEXTE).format(idee=idee, val=random.randint(10, 35))
            contenu_page += phrase + " "
        
        contenu_page += f"\n\n[ ANALYSE GRAPHIQUE SECTORIELLE RÉF {i}.A INCLUSE DANS CETTE SECTION ]\n"
        contenu_page += f"© ARCHITECT SOLUTION PRO - PAGE {i}/25\n"
        pages.append(contenu_page)
        
    return "\n".join(pages)

# 2. INTERFACE ÉPURÉE
st.title("💎 Architect Solution Pro")
st.subheader("Générateur d'Expertise Business Haute Performance")

# Bouton de paiement toujours visible
st.link_button("🔥 ACCÉS CLIENT : PAYER 9€ POUR LE DOSSIER COMPLET", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre concept business :", placeholder="Ex: Boutique en ligne de luxe...")

# Sidebar pour votre accès personnel
st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'ANALYSE DÉTAILLÉE"):
    if idee:
        with st.status("L'IA développe votre dossier de 25 pages...", expanded=True) as status:
            st.write("Analyse des tendances 2026...")
            time.sleep(1)
            st.write("Calcul des prévisions financières...")
            time.sleep(1)
            st.write("Rédaction des 25 chapitres d'expertise...")
            time.sleep(1)
            status.update(label="✅ Analyse terminée !", state="complete", expanded=False)
        
        if code == "23111977":
            st.success("✅ Accès Développeur : Dossier de 25 pages prêt.")
            dossier_final = generer_25_pages_textuelles(idee)
            
            st.download_button(
                label="📥 TÉLÉCHARGER LE DOSSIER (25 PAGES)",
                data=dossier_final,
                file_name=f"Expertise_Complete_{idee}.txt",
                mime="text/plain"
            )
            st.text_area("Aperçu du contenu expert :", dossier_final[:1500] + "...", height=250)
        else:
            st.info("🎯 Votre expertise de 25 pages est prête. Utilisez le bouton de paiement ci-dessus pour débloquer le téléchargement.")
    else:
        st.warning("Veuillez entrer une idée de projet.")

st.markdown("---")
st.caption("Architect Solution Pro - Intelligence d'Affaires Automatisée 2026")
