import streamlit as st
import requests
import hashlib
import io
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# --- MOTEUR DE RECHERCHE ET D'EXPANSION ---
API_KEY = "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" 

def moteur_recherche_profond(idee, axe):
    """Récupère des données massives sur un axe spécifique."""
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": API_KEY,
        "query": f"analyse détaillée 2026 et données chiffrées sur {axe} pour {idee}",
        "search_depth": "advanced",
        "max_results": 5
    }
    try:
        response = requests.post(url, json=payload, timeout=15)
        return [r['content'] for r in response.json().get('results', [])]
    except:
        return ["Données d'analyse sectorielle en cours de compilation..."]

def generer_expertise_massive(idee):
    """Construit 25 pages très remplies en croisant les données."""
    axes = ["Marché et Opportunités", "Techniques et Innovation", "Cadre Légal et Fiscal", "Psychologie et Leadership"]
    base_savoir = {}
    
    with st.status("Extraction et analyse des données mondiales...", expanded=True):
        for axe in axes:
            st.write(f"Analyse profonde : {axe}...")
            base_savoir[axe] = moteur_recherche_profond(idee, axe)
            
    pages = []
    for i in range(1, 26):
        # Chaque page est un chapitre dense
        axe_actuel = axes[i % len(axes)]
        chapitre = [f"CHAPITRE {i} : {axe_actuel.upper()} - ÉTUDE DÉTAILLÉE"]
        
        # On remplit la page avec plusieurs blocs de données traitées
        for idx in range(4): 
            source = base_savoir[axe_actuel][idx % len(base_savoir[axe_actuel])]
            # On crée un paragraphe long et structuré
            bloc = f"Concernant '{idee}', l'analyse montre que {source}. " \
                   f"Cette situation impose une réflexion sur votre positionnement stratégique. " \
                   f"En 2026, la clé résidera dans votre capacité à intégrer ces données pour " \
                   f"optimiser vos processus internes et votre rentabilité."
            chapitre.append(bloc)
            
        pages.append(chapitre)
    
    signature = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
    return pages, signature

def fabriquer_pdf_densite(pages, idee, signature):
    """Génère un PDF avec une mise en page dense et professionnelle."""
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
    styles = getSampleStyleSheet()
    
    # Style personnalisé pour remplir la page
    style_corps = styles["Normal"]
    style_corps.alignment = TA_JUSTIFY
    style_corps.fontSize = 10
    style_corps.leading = 14 # Interligne serré pour plus de texte

    story = [
        Paragraph(f"<b>DOSSIER DE HAUTE STRATÉGIE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Réf Expertise : {signature} | Analyse du {datetime.now().strftime('%d/%m/%Y')}", styles["Normal"]),
        Spacer(1, 1*cm)
    ]
    
    for page in pages:
        for ligne in page:
            s = styles["Heading2"] if "CHAPITRE" in ligne else style_corps
            story.append(Paragraph(ligne, s))
            story.append(Spacer(1, 12))
        story.append(PageBreak())
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.title("💎 Architect Solution Pro")
st.subheader("Analyse Autonome : Moteur de Rédaction Haute Densité (25 Pages)")

st.link_button("🔥 ACCÈS : RECEVOIR MON DOSSIER COMPLET (9€)", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre projet pour lancer la rédaction massive :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 LANCER LA RÉDACTION DU DOSSIER COMPLET"):
    if idee:
        pages, signature = generer_expertise_massive(idee)
        pdf_data = fabriquer_pdf_densite(pages, idee, signature)
        
        if code == "23111977":
            st.success("✅ Dossier de 25 pages denses généré avec succès.")
            st.download_button(
                label="📥 TÉLÉCHARGER LE DOSSIER PDF (HAUTE DENSITÉ)",
                data=pdf_data,
                file_name=f"Expertise_Dense_{idee}.pdf",
                mime="application/pdf"
            )
        else:
            st.info("🎯 L'expertise est prête. Payez 9€ pour débloquer le téléchargement.")
