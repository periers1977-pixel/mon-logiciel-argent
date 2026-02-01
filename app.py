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

# --- CONFIGURATION ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# --- DESIGN HAUTE VISIBILITÉ ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    
    /* Panneau Concepteur Prioritaire */
    .admin-panel {
        background-color: #1e1e1e; color: #00ff00; padding: 20px;
        border-radius: 10px; border: 2px solid #00ff00; margin-bottom: 25px;
        text-align: center; font-weight: bold; box-shadow: 0 4px 15px rgba(0,255,0,0.2);
    }
    
    .status-success {
        background-color: #d4edda; color: #155724; padding: 15px;
        border-radius: 10px; border: 1px solid #c3e6cb; margin: 10px 0;
        font-weight: bold; text-align: center;
    }

    .premium-card {
        background: #ffffff; padding: 40px; border-radius: 20px;
        border: 1px solid #dee2e6; text-align: center; margin: 20px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }

    .price-tag { font-size: 52px; font-weight: 900; color: #007bff; margin: 10px 0; }
    .stTextInput > div > div > input { border: 2px solid #1e1e1e !important; color: #000 !important; }
    .stButton > button { background: #007bff; color: white; font-weight: bold; width: 100%; height: 50px; }
    .concepteur-trigger { position: fixed; bottom: 10px; left: 10px; width: 100px; opacity: 0.05; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE MOTEUR ---
API_KEY = "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"

def filtrage_strict(texte):
    blacklist = r'(?i)(Dhruv|Bhatia|analyst|Research Nester|Research Dive|Pune|India|consultant|biography|Getty|AFP|Twitter|Instagram)'
    texte = re.sub(r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|login|footer)', '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return [s.strip() for s in segments if len(s.split()) > 15 and not re.search(blacklist, s)]

def moteur_expertise(idee, mode_premium=False):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    if mode_premium:
        axes += ["Scalabilité", "Psychologie", "Concurrents", "Supply Chain", "Export", "Fiscale", "Géo-politique", "IA", "Branding", "Vente"]
    
    pool, titres = [], []
    progress_bar = st.progress(0)
    for i, axe in enumerate(axes):
        query = f"expertise stratégique {axe} {idee} 2026 en français"
        try:
            r = requests.post("https://api.tavily.com/search", json={"api_key": API_KEY, "query": query, "search_depth": "advanced" if mode_premium else "basic"}).json()
            data = filtrage_strict(" ".join([res['content'] for res in r.get('results', [])]))
            if data:
                pool.append(data); titres.append(axe.upper())
        except: continue
        progress_bar.progress((i + 1) / len(axes))
    progress_bar.empty()
    return pool, titres

def fabriquer_pdf(pages, idee, sig, mode_premium=False):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    style_p = ParagraphStyle('Normal', fontName="Times-Roman" if mode_premium else "Helvetica", fontSize=10, leading=14, alignment=TA_JUSTIFY)
    story = [Paragraph(f"<b>Architect Solution Pro : {idee.upper()}</b>", styles["Title"]), Paragraph(f"CERTIFICATION : {sig} | 2026", styles["Normal"]), Spacer(1, 0.5*cm)]
    for page in pages:
        story.append(Paragraph(f"<b>{page[0]}</b>", styles["Heading2"]))
        for ligne in page[1:]:
            story.append(Paragraph(ligne, style_p)); story.append(Spacer(1, 6))
    doc.build(story); buf.seek(0)
    return buf

# --- ACCÈS CONCEPTEUR PRIORITAIRE ---
st.markdown("<div class='concepteur-trigger'>", unsafe_allow_html=True)
code_input = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code_input == "23111977":
    st.markdown("<div class='admin-panel'>🔓 MODE CONCEPTEUR : ACCÈS TOTAL AUX DOCUMENTS</div>", unsafe_allow_html=True)
    if 'pdf_blob' in st.session_state:
        st.download_button("📥 TÉLÉCHARGER LE DOCUMENT GÉNÉRÉ", st.session_state['pdf_blob'], "Dossier_Final.pdf")
    else:
        st.info("Aucun document n'a été généré pour le moment.")

# --- INTERFACE UTILISATEUR ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
idee = st.text_input("Saisissez votre projet pour analyse :", placeholder="ex: Agence immobilière, Glacier...")

col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 ANALYSE STANDARD (9€)"):
        if idee:
            p, t = moteur_expertise(idee, False)
            if p:
                data = [[t[i]] + p[i][:10] for i in range(len(p))]
                sig = hashlib.sha256(str(data).encode()).hexdigest()[:12].upper()
                st.session_state['pdf_blob'] = fabriquer_pdf(data, idee, sig, False)
                st.markdown("<div class='status-success'>✅ ANALYSE TERMINÉE : VOTRE DOSSIER EST PRÊT</div>", unsafe_allow_html=True)
                st.markdown(f'<div class="premium-card"><div class="price-tag">9€</div><a href="https://stripe.com/9" style="text-decoration:none;"><div style="background:#007bff;color:white;padding:15px;border-radius:10px;font-weight:bold;">PAYER POUR DÉBLOQUER L\'ACCÈS</div></a></div>', unsafe_allow_html=True)

with col2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if idee:
            p, t = moteur_expertise(idee, True)
            if p:
                data = [[t[i]] + p[i][:15] for i in range(len(p))]
                sig = "PREM-" + hashlib.sha256(str(data).encode()).hexdigest()[:8].upper()
                st.session_state['pdf_blob'] = fabriquer_pdf(data, idee, sig, True)
                st.markdown("<div class='status-success'>✅ EXPERTISE BANCAIRE TERMINÉE : DOSSIER PRÊT</div>", unsafe_allow_html=True)
                st.markdown(f'<div class="premium-card" style="border: 2px solid #ffd700;"><div class="price-tag" style="color:#ffd700;">29€</div><a href="https://stripe.com/29" style="text-decoration:none;"><div style="background:#ffd700;color:black;padding:15px;border-radius:10px;font-weight:bold;">DÉBLOQUER L\'EXPERTISE PREMIUM</div></a></div>', unsafe_allow_html=True)
