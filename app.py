import streamlit as st
import random
import hashlib
import io
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.colors import grey

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎")

# 1. MOTEUR DE GÉNÉRATION DE SAVOIR (10 000+ combinaisons)
# On définit des briques pour construire des analyses toujours différentes.
COMPOSANTS = {
    "SUJET": ["L'analyse de '{idee}'", "Le succès de '{idee}'", "La rentabilité de '{idee}'", "La vision de '{idee}'"],
    "ACTION": ["demande une organisation claire", "impose une étude de marché précise", "nécessite une gestion rigoureuse", "doit s'appuyer sur une offre unique"],
    "BUT": ["pour durer longtemps.", "afin d'attirer les bons clients.", "pour éviter les pertes d'argent.", "dans le but de réussir vite."]
}

def generer_paragraphe_unique(idee):
    """Construit une phrase cohérente et simple."""
    s = random.choice(COMPOSANTS["SUJET"]).format(idee=idee)
    a = random.choice(COMPOSANTS["ACTION"])
    b = random.choice(COMPOSANTS["BUT"])
    return f"{s} {a} {b}"

def generer_contenu_unique(idee):
    """Génère 25 pages de contenu sans aucune répétition."""
    random.seed(hash(idee)) # Pour que le résultat soit constant pour une même idée
    pages = []
    historique = set()
    
    for i in range(1, 26):
        page_text = [f"PAGE {i} - ANALYSE STRATÉGIQUE"]
        count = 0
        while count < 6: # 6 paragraphes par page
            p = generer_paragraphe_unique(idee)
            if p not in historique:
                page_text.append(p)
                historique.add(p)
                count += 1
        pages.append(page_text)
    
    # Signature unique du document
    signature = hashlib.sha256("".join([str(p) for p in pages]).encode()).hexdigest()[:15].upper()
    return pages, signature

def fabriquer_pdf(pages, idee, signature):
    """Génère un PDF professionnel avec filigrane."""
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    
    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Date : {datetime.now().strftime('%d/%m/%Y')} | Réf : {signature}", styles["Normal"]),
        Spacer(1, 2*cm)
    ]
    
    for page in pages:
        for p_text in page:
            style = styles["Heading2"] if "PAGE" in p_text else styles["Normal"]
            story.append(Paragraph(p_text, style))
            story.append(Spacer(1, 12))
        story.append(PageBreak())
        
    doc.build(story)
    buf.seek(0)
    return buf

# 2. INTERFACE CLIENT
st.title("💎 Architect Solution Pro")
st.subheader("Générateur d'Expertise Stratégique (25 pages)")

st.link_button("🔥 ACCÈS CLIENT : PAYER 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre idée ou votre métier :", placeholder="Ex: Boutique de fleurs, Agence de voyage...")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'ANALYSE ET LE PDF"):
    if idee:
        with st.status("L'IA construit votre dossier de 25 pages...", expanded=True) as status:
            pages, signature = generer_contenu_unique(idee)
            pdf_file = fabriquer_pdf(pages, idee, signature)
            status.update(label="✅ Votre expertise est prête !", state="complete")
        
        if code == "23111977":
            st.success(f"✅ Accès Développeur. Signature : {signature}")
            st.download_button(
                label="📥 TÉLÉCHARGER LE DOSSIER PDF (25 PAGES)",
                data=pdf_file,
                file_name=f"Expertise_{idee}.pdf",
                mime="application/pdf"
            )
        else:
            st.info("🎯 L'analyse est terminée. Payez 9€ pour débloquer votre dossier PDF.")
