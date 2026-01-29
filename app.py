import os
import subprocess
import sys

# ÉTAPE MAGIQUE : Installation automatique de l'outil PDF
try:
    from fpdf import FPDF
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf"])
    from fpdf import FPDF

import streamlit as st
import time

# Configuration du logiciel
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎")

def fabriquer_le_dossier(idee):
    pdf = FPDF()
    for i in range(1, 26): # Crée les 25 pages promises
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"CHAPITRE {i} : ANALYSE STRATEGIQUE", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=f"Analyse pour le projet : {idee}\n" + "Contenu expert..." * 80)
    return pdf.output(dest='S').encode('latin-1', 'replace')

st.title("💎 Architect Solution Pro")
idee = st.text_input("Saisissez votre idée :")
lancer = st.button("🚀 GÉNÉRER MON DOSSIER COMPLET")

if lancer:
    if idee:
        barre = st.progress(0)
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        st.success("✅ Votre dossier de 25 pages est prêt !")
        
        # Création du fichier PDF
        fichier_pdf = fabriquer_le_dossier(idee)
        
        # Bouton de téléchargement
        st.download_button(
            label="📄 TÉLÉCHARGER LE DOSSIER (VUE DÉVELOPPEUR)",
            data=fichier_pdf,
            file_name=f"Dossier_{idee}.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Veuillez écrire une idée.")

st.markdown("---")
st.write("💰 Prix du dossier complet : 9€")
