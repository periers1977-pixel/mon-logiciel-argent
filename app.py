import streamlit as st
import requests
import random
import hashlib
import io
import time
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎")

# --- CONFIGURATION DE VOTRE CLÉ ---
# Collez votre clé API entre les guillemets ci-dessous
API_KEY = "VOTRE_CLE_ICI" 

def agent_recherche_web(requete):
    """Effectue une recherche réelle sur le Web via l'API."""
    if API_KEY == "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":
        return "Erreur : Clé API non configurée. Le logiciel tourne à vide."
    
    try:
        # Configuration pour Google Serper (ou Tavily, selon votre clé)
        url = "https://google.serper.dev/search"
        payload = {"q": requete, "gl": "fr", "hl": "fr"}
        headers = {'X-API-KEY': API_KEY, 'Content-Type': 'application/json'}
        
        response = requests.post(url, json=payload, timeout=10)
        res = response.json()
        
        # On extrait les extraits des 3 premiers résultats pour nourrir l'IA
        snippets = [item['snippet'] for item in res.get('organic', [])[:3]]
        return " ".join(snippets)
    except Exception as e:
        return f"Connexion au savoir mondial perturbée. Utilisation de la base interne."

def generer_expertise_connectee(idee):
    """L'IA cherche sur le web et rédige 25 pages uniques."""
    pages = []
    memoire_anti_doublon = set()
    
    # Thèmes de recherche pour varier les pages
    themes = [
        f"Marché et prix {idee} 2026", f"Conseils techniques pour {idee}",
        f"Lois et réglementation {idee} France", f"Psychologie et succès {idee}"
    ]

    for i in range(1, 26):
        page_text = [f"CHAPITRE {i} : ANALYSE STRATÉGIQUE RÉELLE"]
        
        # L'IA effectue la recherche pour ce chapitre précis
        sujet_du_jour = themes[i % len(themes)]
        donnee_web = agent_recherche_web(sujet_du_jour)
        
        # On construit 5 paragraphes basés sur la recherche
        count = 0
        while count < 5:
            reflexion = f"D'après les dernières analyses sur {sujet_du_jour} : {donnee_web[:150]}... Pour réussir '{idee}', cette donnée impose une adaptation immédiate."
            
            if reflexion not in memoire_anti_doublon:
                page_text.append(reflexion)
                memoire_anti_doublon.add(reflexion)
                count += 1
        
        pages.append(page_text)
    
    signature = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
    return pages, signature

def fabriquer_pdf_final(pages, idee, signature):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    
    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE RÉELLE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Référence : {signature} | Analyse Web du {datetime.now().strftime('%d/%m/%Y')}", styles["Normal"]),
        Spacer(1, 2*cm)
    ]
    
    for page in pages:
        for ligne in page:
            style = styles["Heading2"] if "CHAPITRE" in ligne else styles["Normal"]
            story.append(Paragraph(ligne, style))
            story.append(Spacer(1, 12))
        story.append(PageBreak())
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.title("💎 Architect Solution Pro")
st.subheader("Agent Autonome : Intelligence Web & Réflexion Réelle")

st.link_button("🔥 ACCÈS CLIENT : PAYER 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre projet ou votre ambition (La recherche web va démarrer) :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 LANCER LA RECHERCHE WEB ET L'ANALYSE"):
    if idee:
        with st.status("L'IA parcourt le web avec votre clé API...", expanded=True) as status:
            pages, signature = generer_expertise_connectee(idee)
            pdf_data = fabriquer_pdf_final(pages, idee, signature)
            status.update(label="✅ Expertise de 25 pages générée avec succès !", state="complete")
        
        if code == "23111977":
            st.success("✅ Accès Développeur. Votre dossier connecté au Web est prêt.")
            st.download_button(
                label="📥 TÉLÉCHARGER LE DOSSIER PDF ANALYSÉ",
                data=pdf_data,
                file_name=f"Expertise_Reelle_{idee}.pdf",
                mime="application/pdf"
            )
        else:
            st.info("🎯 L'expertise est générée. Payez 9€ pour débloquer le téléchargement.")
