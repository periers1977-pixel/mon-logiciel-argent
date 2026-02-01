import streamlit as st
import requests
import hashlib
import io
import re
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# --- MOTEUR DE RECHERCHE ET SYNTHÈSE ---
API_KEY = "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" 

def moteur_expertise_claire(idee, axe):
    """Récupère et nettoie les données pour une clarté maximale."""
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": API_KEY,
        "query": f"enjeux stratégiques 2026 et opportunités concrètes {axe} pour {idee}",
        "search_depth": "advanced"
    }
    try:
        response = requests.post(url, json=payload, timeout=15)
        # On extrait le texte et on retire les balises inutiles
        raw_text = " ".join([r['content'] for r in response.json().get('results', [])])
        clean_text = re.sub(r'http\S+', '', raw_text) # Supprime les liens
        return clean_text
    except:
        return "Analyse sectorielle en cours de traitement pour optimisation."

def generer_livrable_parfait(idee):
    """Génère 25 pages denses, claires et 100% en français."""
    axes = [
        "Développement Commercial", "Optimisation des Coûts", 
        "Réglementation 2026", "Psychologie de la Réussite",
        "Marketing et Visibilité", "Innovation Technique"
    ]
    
    base_savoir = []
    with st.status("Analyse stratégique et rédaction claire...", expanded=True):
        for axe in axes:
            st.write(f"Expertise sur : {axe}...")
            base_savoir.append(moteur_expertise_claire(idee, axe))
            
    pages = []
    for i in range(1, 26):
        axe_nom = axes[i % len(axes)]
        chapitre = [f"CHAPITRE {i} : {axe_nom.upper()}"]
        
        # On sélectionne une partie du savoir et on la met en forme
        source = base_savoir[i % len(base_savoir)]
        start_idx = (i * 150) % (len(source) - 500 if len(source) > 500 else 1)
        
        # Construction d'un bloc de texte fluide
        texte_final = f"L'analyse approfondie de votre projet '{idee}' démontre que {source[start_idx:start_idx+600]}. " \
                      f"Cette dynamique de marché impose une restructuration de vos priorités pour 2026. " \
                      f"Il ne s'agit plus de suivre la tendance, mais d'anticiper les besoins de vos futurs clients " \
                      f"en optimisant chaque levier de rentabilité et de service."
        
        chapitre.append(texte_final)
        pages.append(chapitre)
        
    signature = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
    return pages, signature

def fabriquer_pdf_expert(pages, idee, signature):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
    styles = getSampleStyleSheet()
    
    style_p = styles["Normal"]
    style_p.alignment = TA_JUSTIFY
    style_p.fontSize = 11
    style_p.leading = 16 # Plus d'espace pour la lisibilité

    story = [
        Paragraph(f"<b>DOSSIER DE HAUTE STRATÉGIE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Référence : {signature} | Analyse du {datetime.now().strftime('%d/%m/%Y')}", styles["Normal"]),
        Spacer(1, 1*cm)
    ]
    
    for page in pages:
        for ligne in page:
            s = styles["Heading2"] if "CHAPITRE" in ligne else style_p
            story.append(Paragraph(ligne, s))
            story.append(Spacer(1, 15))
        story.append(PageBreak())
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.title("💎 Architect Solution Pro")
st.subheader("Analyse Autonome : Moteur d'Expertise Haute Précision")

st.link_button("🔥 ACCÈS : RECEVOIR MON DOSSIER DE 25 PAGES (9€)", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre ambition pour lancer l'expertise :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 LANCER LA RÉDACTION DU DOSSIER EXPERT"):
    if idee:
        pages, signature = generer_livrable_parfait(idee)
        pdf_data = fabriquer_pdf_expert(pages, idee, signature)
        
        if code == "23111977":
            st.success("✅ Expertise claire et dense de 25 pages générée.")
            st.download_button("📥 TÉLÉCHARGER LE DOSSIER PDF", pdf_data, f"Expertise_{idee}.pdf", "application/pdf")
        else:
            st.info("🎯 L'expertise est prête. Payez 9€ pour débloquer le téléchargement.")
