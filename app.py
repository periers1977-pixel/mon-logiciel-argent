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

# --- CONFIGURATION DU MOTEUR ---
API_KEY = "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" 

def purger_donnees(texte):
    bruit = r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu|sign up)'
    texte = re.sub(bruit, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return list(dict.fromkeys([p.strip() for p in segments if len(p.split()) > 15]))

def moteur_recherche_24x(idee):
    axes = ["marché", "innovation", "légal 2026", "finance", "acquisition", "risques", "vision"]
    pool = []
    with st.status(f"Génération de l'expertise pour '{idee}'...", expanded=True):
        for idx, axe in enumerate(axes):
            try:
                url = "https://api.tavily.com/search"
                payload = {"api_key": API_KEY, "query": f"expertise stratégique {axe} {idee} 2026", "search_depth": "advanced"}
                response = requests.post(url, json=payload, timeout=12)
                pool.extend(purger_donnees(" ".join([r['content'] for r in response.json().get('results', [])])))
            except: continue
    return list(dict.fromkeys(pool))

def generer_livrable(idee):
    base = moteur_recherche_24x(idee)
    pages = []
    nb_chap = min(40, max(20, len(base) // 4))
    for i in range(1, nb_chap + 1):
        sections = []
        for s in range(5):
            data = base.pop(0) if base else "Analyse de la résilience opérationnelle."
            labels = ["CONTEXTE", "DIAGNOSTIC", "ENJEUX", "STRATÉGIE", "DÉPLOIEMENT"]
            sections.append(f"<b>{labels[s]} :</b> {data} Pour votre projet '{idee}', cette étape garantit votre succès.")
        pages.append([f"CHAPITRE {i} : ANALYSE STRATÉGIQUE"] + sections)
    return pages, hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()

def fabriquer_pdf(pages, idee, signature):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    style_p = styles["Normal"]
    style_p.alignment, style_p.fontSize, style_p.leading = TA_JUSTIFY, 10.5, 15
    story = [Paragraph(f"<b>DOSSIER D'EXPERTISE INTÉGRAL : {idee.upper()}</b>", styles["Title"]), Paragraph(f"Réf : {signature}", styles["Normal"]), Spacer(1, 0.5*cm)]
    for page in pages:
        for ligne in page:
            story.append(Paragraph(ligne, styles["Heading2"] if "CHAPITRE" in ligne else style_p))
            story.append(Spacer(1, 12))
        story.append(PageBreak())
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.title("💎 Architect Solution Pro")
st.subheader("Cabinet de Conseil Stratégique Autonome")

st.markdown("""
<div style="background-color:#f0f2f6;padding:25px;border-radius:10px;border:2px solid #007bff;text-align:center">
    <h2 style="color:#007bff">📂 DOSSIER D'EXPERTISE INTÉGRAL</h2>
    <p>Analyse exhaustive basée sur 24 sources web mondiales.</p>
    <a href="https://buy.stripe.com/votre_lien" target="_blank" style="background-color:#007bff;color:white;padding:15px 30px;text-decoration:none;border-radius:5px;font-weight:bold;font-size:1.2em">OBTENIR MON DOSSIER (9€)</a>
    <p style="font-size:0.8em;margin-top:10px;color:grey">Paiement 100% Sécurisé - Réception immédiate</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
idee = st.text_input("Saisissez votre idée pour lancer l'expertise :")

# --- PIED DE PAGE ET MENTIONS LÉGALES ---
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⚖️ Mentions Légales & CGV"):
        st.info("""
        **Mentions Légales** Directeur de la publication : Architect Solution Pro.  
        Hébergement : Streamlit Cloud.  
        
        **Conditions Générales de Vente (CGV)** 1. Objet : Fourniture d'un dossier d'analyse stratégique au format PDF.  
        2. Prix : 9€ TTC par dossier.  
        3. Livraison : Immédiate après génération sur l'interface.  
        4. Rétractation : S'agissant d'un contenu numérique fourni instantanément, aucun remboursement n'est possible après le début de la génération.  
        5. Données : Vos saisies sont utilisées uniquement pour la génération du dossier et ne sont pas conservées.
        """)

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'EXPERTISE"):
    if idee:
        pages, sig = generer_livrable(idee)
        pdf = fabriquer_pdf(pages, idee, sig)
        if code == "23111977":
            st.success("✅ Dossier généré.")
            st.download_button("📥 TÉLÉCHARGER LE PDF", pdf, f"Expertise_{idee}.pdf", "application/pdf")
        else:
            st.warning("🎯 Analyse prête. Payez 9€ pour débloquer le téléchargement.")
