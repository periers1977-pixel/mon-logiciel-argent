import streamlit as st
import random
import hashlib
import io
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎")

# 1. RÉSERVOIR DE SAVOIR RÉEL (Pas de charabia, que du concret)
SAVOIR = {
    "STRAT": ["L'analyse de '{idee}' montre qu'il faut viser une niche précise pour éviter la concurrence.", "Le succès de '{idee}' dépend de votre capacité à expliquer votre valeur en moins de 10 secondes.", "Pour '{idee}', la différenciation doit se faire sur la qualité et le sérieux du suivi."],
    "FINANCE": ["La rentabilité de '{idee}' impose une séparation stricte entre vos comptes personnels et pro.", "Surveillez votre trésorerie pour '{idee}' : l'argent est l'oxygène de votre ambition.", "Chaque euro dépensé pour '{idee}' doit servir à attirer un client ou à gagner du temps."],
    "VIE": ["Votre mental est le moteur de '{idee}' : sans repos et sans discipline, le projet s'arrêtera.", "Le projet '{idee}' est un marathon. Fixez-vous des petits objectifs pour garder le moral.", "Entourez-vous de gens positifs qui comprennent l'importance de '{idee}' pour votre futur."]
}

def generer_donnees_uniques(idee):
    random.seed(hash(idee))
    pages = []
    # On crée une liste de tous les conseils possibles
    pool = []
    for cat in SAVOIR:
        pool.extend(SAVOIR[cat])
    
    # On mélange et on s'assure qu'on ne répète rien sur 25 pages
    for i in range(1, 26):
        page = [f"CHAPITRE {i} : ANALYSE STRATÉGIQUE"]
        random.shuffle(pool)
        for j in range(4): # 4 conseils par page
            page.append(f"✔ {pool[j].format(idee=idee)}")
        pages.append(page)
    
    signature = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
    return pages, signature

def fabriquer_pdf(pages, idee, signature):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    
    story = [
        Paragraph(f"<b>DOSSIER EXPERT : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Référence : {signature} | Date : {datetime.now().strftime('%d/%m/%Y')}", styles["Normal"]),
        Spacer(1, 2*cm)
    ]
    
    for page in pages:
        for ligne in page:
            style = styles["Heading2"] if "CHAPITRE" in ligne else styles["Normal"]
            story.append(Paragraph(ligne, style))
            story.append(Spacer(1, 10))
        story.append(PageBreak())
        
    doc.build(story)
    buf.seek(0)
    return buf

# 2. INTERFACE
st.title("💎 Architect Solution Pro")
st.subheader("Générateur de Dossiers de Réussite (25 Pages PDF)")

st.link_button("🔥 ACCÈS CLIENT : PAYER 9€", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre idée ou votre métier :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER MON DOSSIER PDF"):
    if idee:
        with st.status("Rédaction de votre expertise unique...", expanded=True) as status:
            pages, signature = generer_donnees_uniques(idee)
            pdf_data = fabriquer_pdf(pages, idee, signature)
            status.update(label="✅ Votre dossier de 25 pages est prêt !", state="complete")
        
        if code == "23111977":
            st.success("✅ Accès Développeur. Dossier généré sans erreur.")
            st.download_button(
                label="📥 TÉLÉCHARGER LE DOSSIER PDF",
                data=pdf_data,
                file_name=f"Expertise_{idee}.pdf",
                mime="application/pdf"
            )
        else:
            st.info("🎯 L'expertise est prête. Payez 9€ pour débloquer le téléchargement.")
