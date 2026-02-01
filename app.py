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

# --- CONFIGURATION PAGE ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# CSS pour masquer les menus Streamlit et styliser l'interface
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .main { background-color: #0e1117; }
    .payment-card {
        background: linear-gradient(135deg, #1c1f26 0%, #0e1117 100%);
        padding: 30px; border-radius: 20px; border: 1px solid #333; text-align: center;
    }
    .admin-box { margin-top: 50px; padding: 10px; opacity: 0.3; }
    .admin-box:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEURS ---
API_KEY = "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"

def purger_donnees(texte):
    bruit = r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu)'
    texte = re.sub(bruit, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return list(dict.fromkeys([p.strip() for p in segments if len(p.split()) > 12]))

def moteur_furtif(idee):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    pool, titres = [], []
    with st.spinner("💎 Compilation d'un dossier de haute densité en cours..."):
        for axe in axes:
            try:
                url = "https://api.tavily.com/search"
                payload = {"api_key": API_KEY, "query": f"expertise approfondie {axe} {idee} 2026", "search_depth": "advanced"}
                r = requests.post(url, json=payload, timeout=12).json()
                data = purger_donnees(" ".join([res['content'] for res in r.get('results', [])]))
                if data:
                    pool.append(data)
                    titres.append(axe.upper())
            except: continue
    return pool, titres

def fabriquer_pdf_dense(pages, idee, sig):
    buf = io.BytesIO()
    # Marges réduites pour mettre plus de texte
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    
    # Style de texte compact
    style_p = styles["Normal"]
    style_p.alignment = TA_JUSTIFY
    style_p.fontSize = 9.5
    style_p.leading = 12  # Interligne serré
    
    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE STRATÉGIQUE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Référence Authentifiée : {sig} | Émis le {datetime.now().strftime('%d/%m/%Y')}", styles["Normal"]),
        Spacer(1, 0.5*cm)
    ]
    
    for page in pages:
        story.append(Paragraph(f"<b>{page[0]}</b>", styles["Heading2"]))
        # On affiche beaucoup plus de segments par chapitre pour remplir les pages
        for ligne in page[1:]:
            story.append(Paragraph(ligne, style_p))
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 0.3*cm)) # Petit espace au lieu d'un saut de page
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center; color: white;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)

st.markdown(f"""
    <div class="payment-card">
        <h2 style="color: #007bff !important;">DOSSIER D'EXPERTISE HAUTE DENSITÉ</h2>
        <p style="color: #ccc;">Analyse technique complète (30+ pages de données brutes).</p>
        <p style="font-size: 24px; font-weight: bold; color: white;">9.00 €</p>
        <a href="https://buy.stripe.com/votre_lien" target="_blank" style="text-decoration: none;">
            <div style="background: #007bff; color: white; padding: 15px; border-radius: 10px; font-weight: bold;">ACCÉDER AU DOSSIER COMPLET</div>
        </a>
    </div>
    """, unsafe_allow_html=True)

idee = st.text_input("Saisissez votre projet :", placeholder="ex: Plateforme de jeux en ligne...")

# Accès Admin en bas
st.markdown("<div class='admin-box'>", unsafe_allow_html=True)
code_admin = st.text_input("Code :", type="password")
st.markdown("</div>", unsafe_allow_html=True)

if code_admin == "23111977":
    if st.button("🚀 GÉNÉRER LE DOSSIER HAUTE DENSITÉ"):
        if idee:
            pool, titres = moteur_furtif(idee)
            pages = []
            for i in range(len(pool)):
                # On prend jusqu'à 15 segments par recherche pour saturer le document
                chapitre = [f"SECTION {i+1} : {titres[i]}"] + pool[i][:15]
                pages.append(chapitre)
            sig = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
            pdf = fabriquer_pdf_dense(pages, idee, sig)
            st.success("✅ Dossier dense généré.")
            st.download_button("📥 TÉLÉCHARGER LE PDF EXPERT", pdf, f"Expertise_Dense_{idee}.pdf")
