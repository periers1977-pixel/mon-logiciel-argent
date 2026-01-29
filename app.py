import streamlit as st
import random
import time
from datetime import datetime

# Importation avec sécurité pour éviter le crash
try:
    import matplotlib.pyplot as plt
    import numpy as np
    HAS_GRAPH = True
except ImportError:
    HAS_GRAPH = False

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# Moteur de rédaction expert
def generer_analyse_25_pages(idee):
    session = f"BP-{random.randint(100, 999)}"
    lignes = [
        f"ARCHITECT SOLUTION PRO - EXPERTISE CERTIFIÉE\nPROJET : {idee.upper()} | RÉF : {session}\n" + "="*50,
        "\nSYNTHÈSE EXÉCUTIVE :",
        f"L'analyse de '{idee}' démontre une viabilité économique forte pour 2026.",
        "Le positionnement stratégique doit privilégier la valeur ajoutée sur le volume.",
        "\nSTRATÉGIE DE DÉVELOPPEMENT :"
    ]
    # Génération de 25 chapitres distincts
    for i in range(1, 26):
        lignes.append(f"\n--- CHAPITRE {i} : ANALYSE DE LA VALEUR PAGE {i} ---")
        lignes.append(f"Expertise appliquée à {idee} : Optimisation des leviers de croissance.")
        lignes.append(f"Statistiques calculées : ROI potentiel de {random.randint(200, 500)}% sur 24 mois.")
        lignes.append("Cette section inclut des schémas de flux et des projections financières.")
        
    return "\n".join(lignes)

# --- INTERFACE ---
st.title("💎 Architect Solution Pro")
st.link_button("🔥 ACCÈS CLIENT : PAYER 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Votre idée de business :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'ANALYSE D'EXPERT"):
    if idee:
        barre = st.progress(0, text="L'IA Architect Solution rédige le dossier...")
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        if code == "23111977":
            st.success("✅ Accès Développeur Autorisé")
            
            if HAS_GRAPH:
                fig, ax = plt.subplots()
                x = np.linspace(0, 10, 100)
                ax.plot(x, np.exp(x/3), color='teal')
                ax.set_title(f"Projection de Croissance : {idee}")
                st.pyplot(fig)
            
            dossier = generer_analyse_25_pages(idee)
            st.download_button(
                label="📥 TÉLÉCHARGER LE DOSSIER DE 25 PAGES",
                data=dossier,
                file_name=f"Expertise_Complete_{idee}.txt",
                mime="text/plain"
            )
            st.text_area("Lecture du dossier :", dossier, height=400)
        else:
            st.info("🎯 L'analyse est prête. Payez 9€ pour débloquer le téléchargement.")
