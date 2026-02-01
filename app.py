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

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# --- DESIGN IMMERSIF (CSS) ---
st.markdown("""
    <style>
    /* Masquage total des menus natifs Streamlit pour le client */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;} /* On supprime la sidebar qui pose problème */
    
    .main { background-color: #0e1117; }
    
    .payment-card {
        background: linear-gradient(135deg, #1c1f26 0%, #0e1117 100%);
        padding: 30px; border-radius: 20px; border: 1px solid #333; text-align: center; margin-bottom: 30px;
    }
    
    .admin-box {
        margin-top: 100px;
        padding: 20px;
        border-top: 1px solid #222;
        opacity: 0.5;
    }
    .admin-box:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR DE GÉNÉRATION ---
API_KEY = "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"

def purger_donnees(texte):
    bruit = r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu)'
    texte = re.sub(bruit, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return list(dict.fromkeys([p.strip() for p in segments if len(p.split()) > 15]))

def moteur_furtif(idee):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision"]
    pool, titres = [], []
    with st.spinner("💎 Élaboration de votre expertise en cours..."):
        for axe in axes:
            try:
                url = "https://api.tavily.com/search"
                payload = {"api_key": API_KEY, "query": f"expertise stratégique {axe} {idee} 2026", "search_depth": "advanced"}
                r = requests.post(url, json=payload, timeout=12).json()
                data = purger_donnees(" ".join([res['content'] for res in r.get('results', [])]))
                if data:
                    pool.append(data); titres.append(axe.upper())
            except: continue
    return pool, titres

def fabriquer_pdf(pages, idee, sig):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
    styles = getSampleStyleSheet()
    style_p = styles["Normal"]
    style_p.alignment, style_p.fontSize, style_p.leading = TA_JUSTIFY, 10.5, 15
    story = [Paragraph(f"<b>DOSSIER D'EXPERTISE : {idee.upper()}</b>", styles["Title"]), Paragraph(f"Signature : {sig}", styles["Normal"]), Spacer(1, 1*cm)]
    for page in pages:
        for ligne in page:
            story.append(Paragraph(ligne, styles["Heading2"] if "CHAPITRE" in ligne else style_p))
            story.append(Spacer(1, 12))
        story.append(PageBreak())
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE CLIENT ---
st.markdown("<h1 style='text-align: center; color: white;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)

st.markdown(f"""
    <div class="payment-card">
        <h2 style="color: #007bff !important;">DOSSIER D'EXPERTISE INTÉGRAL</h2>
        <p style="color: #ccc;">Analyse multisectorielle basée sur 24 sources web mondiales.</p>
        <p style="font-size: 24px; font-weight: bold; color: white;">9.00 €</p>
        <a href="https://buy.stripe.com/votre_lien" target="_blank" style="text-decoration: none;">
            <div style="background: #007bff; color: white; padding: 15px; border-radius: 10px; font-weight: bold;">
                DÉBLOQUER MON ACCÈS SÉCURISÉ
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

idee = st.text_input("Saisissez votre ambition pour 2026 :", placeholder="ex: Agence immobilière...")

# --- ZONE D'ACCÈS CONCEPTEUR (Directement sur la page) ---
st.markdown("<div class='admin-box'>", unsafe_allow_html=True)
col_a, col_b = st.columns([2,1])
with col_b:
    code_admin = st.text_input("Accès Admin :", type="password")
st.markdown("</div>", unsafe_allow_html=True)

# LOGIQUE DE DÉVERROUILLAGE
if code_admin == "23111977":
    st.success("✅ Mode Concepteur Activé")
    if st.button("🚀 GÉNÉRER L'EXPERTISE MAINTENANT"):
        if idee:
            pool, titres = moteur_furtif(idee)
            pages = []
            for i in range(len(pool)):
                chap = [f"CHAPITRE {i+1} : {titres[i]}"]
                for segment in pool[i][:5]: chap.append(segment)
                pages.append(chap)
            sig = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
            pdf = fabriquer_pdf(pages, idee, sig)
            st.download_button("📥 TÉLÉCHARGER LE PDF GÉNÉRÉ", pdf, f"Expertise_{idee}.pdf")
else:
    if idee:
        st.info("🎯 L'intelligence analyse votre projet. Le téléchargement s'activera après votre règlement.")

st.markdown("<div style='text-align:center; color:#333; font-size:0.7em; margin-top:50px;'>Architect Solution Pro © 2026</div>", unsafe_allow_html=True)
