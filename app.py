import streamlit as st
import requests
import hashlib
import io
import re
import random
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY

# --- CONFIGURATION PAGE ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# --- SYSTÈME DE TRADUCTION ---
lang = st.selectbox("🌐 Language / Langue", ["Français", "English"], index=0)

T = {
    "Français": {
        "title": "Architect Solution Pro",
        "subtitle": "Expertise Systémique & Algorithmes de Précision",
        "placeholder": "ex: Agence immobilière, Site e-commerce...",
        "btn_std": "🚀 ANALYSE STANDARD (9€)",
        "btn_pre": "👑 EXPERTISE BANCAIRE (29€)",
        "unlock": "DÉBLOQUER L'ACCÈS",
        "liaison": "Concernant votre ambition pour '{idee}', les données révèlent :",
        "search_suffix": "en français",
        "cert": "CERTIFICATION"
    },
    "English": {
        "title": "Architect Solution Pro",
        "subtitle": "Systemic Expertise & Precision Algorithms",
        "placeholder": "e.g.: Real estate agency, E-commerce...",
        "btn_std": "🚀 STRATEGIC ANALYSIS (9€)",
        "btn_pre": "👑 BANK-LEVEL EXPERTISE (29€)",
        "unlock": "UNLOCK ACCESS",
        "liaison": "Regarding your ambition for '{idee}', data reveals:",
        "search_suffix": "in english",
        "cert": "CERTIFICATION"
    }
}[lang]

# --- STYLE VISUEL ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #0e1117; color: white; }
    .premium-card {
        background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(15px);
        padding: 40px; border-radius: 30px; border: 1px solid rgba(0, 123, 255, 0.4);
        text-align: center; margin: 20px 0;
    }
    .price-tag { font-size: 52px; font-weight: 900; color: #00c6ff; margin: 10px 0; }
    .stButton > button {
        background: linear-gradient(45deg, #007bff, #00c6ff);
        color: white; border: none; padding: 15px; border-radius: 10px; font-weight: bold; width: 100%;
    }
    .admin-footer { position: fixed; bottom: 5px; left: 5px; width: 100px; opacity: 0.03; transition: 0.3s; }
    .admin-footer:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR ---
API_KEY = "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"

def filtrage_final(texte):
    blacklist = r'(?i)(Dhruv|Bhatia|analyst|Research Nester|Research Dive|Pune|India|consultant|biography|Getty|AFP|Twitter|Instagram)'
    texte = re.sub(r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|login|footer)', '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return [s.strip() for s in segments if len(s.split()) > 15 and not re.search(blacklist, s)]

def moteur_expertise(idee, mode_premium=False):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    if mode_premium:
        axes += ["Scalabilité", "Psychologie", "Concurrents", "Supply Chain", "Export", "Fiscale", "Géo-politique", "Automatisation", "Branding", "Vente"]
    
    pool, titres = [], []
    progress_bar = st.progress(0)
    for i, axe in enumerate(axes):
        query = f"strategic data {axe} {idee} 2026 {T['search_suffix']}"
        depth = "advanced" if mode_premium else "basic"
        try:
            url = "https://api.tavily.com/search"
            payload = {"api_key": API_KEY, "query": query, "search_depth": depth}
            r = requests.post(url, json=payload, timeout=25).json()
            data = filtrage_final(" ".join([res['content'] for res in r.get('results', [])]))
            if data: pool.append(data); titres.append(axe.upper())
        except: continue
        progress_bar.progress((i + 1) / len(axes))
    progress_bar.empty()
    return pool, titres

def fabriquer_pdf(pages, idee, sig, mode_premium=False):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    font = "Times-Roman" if mode_premium else "Helvetica"
    style_p = ParagraphStyle('Normal', fontName=font, fontSize=9.5, leading=12, alignment=TA_JUSTIFY)
    
    story = [Paragraph(f"<b>{T['title']} : {idee.upper()}</b>", styles["Title"]),
             Paragraph(f"{T['cert']} : {sig} | 2026", styles["Normal"]), Spacer(1, 0.5*cm)]
    
    for page in pages:
        story.append(Paragraph(f"<b>{page[0]}</b>", styles["Heading2"]))
        story.append(Paragraph(T['liaison'].format(idee=idee), style_p))
        for ligne in page[1:]:
            story.append(Paragraph(ligne, style_p)); story.append(Spacer(1, 6))
    doc.build(story); buf.seek(0)
    return buf

# --- INTERFACE ---
st.markdown(f"<h1 style='text-align: center;'>💎 {T['title']}</h1>", unsafe_allow_html=True)
idee = st.text_input(T['placeholder'], placeholder=T['placeholder'])

col1, col2 = st.columns(2)
with col1:
    if st.button(T['btn_std']):
        if idee:
            p, t = moteur_expertise(idee, False)
            data = [[f"SECTION {i+1} : {t[i]}"] + p[i][:10] for i in range(len(p))]
            sig = hashlib.sha256(str(data).encode()).hexdigest()[:12].upper()
            st.markdown(f'<div class="premium-card"><div class="price-tag">9€</div><a href="https://stripe.com/9" style="text-decoration:none;"><div style="background:#007bff;color:white;padding:15px;border-radius:10px;font-weight:bold;">{T["unlock"]}</div></a></div>', unsafe_allow_html=True)
            st.session_state['pdf'] = fabriquer_pdf(data, idee, sig, False)

with col2:
    if st.button(T['btn_pre']):
        if idee:
            p, t = moteur_expertise(idee, True)
            data = [[f"SECTION {i+1} : {t[i]}"] + p[i][:15] for i in range(len(p))]
            sig = "PREM-" + hashlib.sha256(str(data).encode()).hexdigest()[:8].upper()
            st.markdown(f'<div class="premium-card" style="border-color:#ffd700;"><div class="price-tag" style="color:#ffd700;">29€</div><a href="https://stripe.com/29" style="text-decoration:none;"><div style="background:#ffd700;color:black;padding:15px;border-radius:10px;font-weight:bold;">{T["unlock"]}</div></a></div>', unsafe_allow_html=True)
            st.session_state['pdf'] = fabriquer_pdf(data, idee, sig, True)

# Admin
st.markdown("<div class='admin-footer'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)
if code == "23111977" and 'pdf' in st.session_state:
    st.download_button("📥 DOWNLOAD", st.session_state['pdf'], "Dossier_Architect.pdf")
