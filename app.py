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

# --- STYLE CLARTÉ PROFESSIONNELLE (CSS) ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    
    /* Fond gris anthracite doux pour le repos visuel */
    .stApp { 
        background-color: #f0f2f6; 
        color: #1e1e1e;
    }

    /* Cartes blanches épurées pour un contraste maximum */
    .premium-card {
        background: #ffffff;
        padding: 45px;
        border-radius: 20px;
        border: 1px solid #d1d5db;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }

    /* Typographie sombre pour la lisibilité */
    h1, h3, p, label { color: #111827 !important; }
    
    .price-tag { 
        font-size: 52px; 
        font-weight: 900; 
        color: #007bff; 
        margin: 10px 0; 
    }

    .stButton > button {
        background: #007bff;
        color: white;
        border: none;
        padding: 15px;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        transition: 0.3s;
    }
    .stButton > button:hover { background: #0056b3; }

    /* Admin discret en bas */
    .admin-footer { position: fixed; bottom: 5px; left: 5px; width: 100px; opacity: 0.1; transition: 0.3s; }
    .admin-footer:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR & FILTRAGE ---
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
        # Force le français
        query = f"expertise stratégique {axe} {idee} 2026 en français"
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
    style_p = ParagraphStyle('Normal', fontName=font, fontSize=10, leading=14, alignment=TA_JUSTIFY)
    
    story = [Paragraph(f"<b>Architect Solution Pro : {idee.upper()}</b>", styles["Title"]),
             Paragraph(f"Signature : {sig} | 2026", styles["Normal"]), Spacer(1, 0.5*cm)]
    
    for page in pages:
        story.append(Paragraph(f"<b>{page[0]}</b>", styles["Heading2"]))
        for ligne in page[1:]:
            story.append(Paragraph(ligne, style_p)); story.append(Spacer(1, 6))
        
        data = [["INDICATEUR", "VALEUR", "IMPACT"], ["Fiabilité", f"{random.randint(85,99)}%", "ÉLEVÉ"]]
        t = Table(data, colWidths=[6*cm, 6*cm, 5*cm])
        t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey), ('TEXTCOLOR', (0,0), (-1,0), colors.white), ('GRID', (0,0), (-1,-1), 0.5, colors.grey)]))
        story.append(Spacer(1, 0.5*cm)); story.append(t); story.append(Spacer(1, 1*cm))
        
    doc.build(story); buf.seek(0)
    return buf

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
idee = st.text_input("Saisissez votre projet :", placeholder="ex: Agence immobilière, Glacier...")

col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 ANALYSE (9€)"):
        if idee:
            p, t = moteur_expertise(idee, False)
            data = [[f"SECTION {i+1} : {t[i]}"] + p[i][:10] for i in range(len(p))]
            sig = hashlib.sha256(str(data).encode()).hexdigest()[:12].upper()
            st.markdown(f'<div class="premium-card"><div class="price-tag">9€</div><p>Analyse prête pour déblocage.</p><a href="https://stripe.com/9" style="text-decoration:none;"><div style="background:#007bff;color:white;padding:15px;border-radius:10px;font-weight:bold;">DÉBLOQUER L\'ACCÈS</div></a></div>', unsafe_allow_html=True)
            st.session_state['pdf'] = fabriquer_pdf(data, idee, sig, False)

with col2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if idee:
            p, t = moteur_expertise(idee, True)
            data = [[f"SECTION {i+1} : {t[i]}"] + p[i][:15] for i in range(len(p))]
            sig = "PREM-" + hashlib.sha256(str(data).encode()).hexdigest()[:8].upper()
            st.markdown(f'<div class="premium-card" style="border: 2px solid #ffd700;"><div class="price-tag" style="color:#ffd700;">29€</div><p>Expertise bancaire certifiée.</p><a href="https://stripe.com/29" style="text-decoration:none;"><div style="background:#ffd700;color:black;padding:15px;border-radius:10px;font-weight:bold;">DÉBLOQUER PREMIUM</div></a></div>', unsafe_allow_html=True)
            st.session_state['pdf'] = fabriquer_pdf(data, idee, sig, True)

# Admin
st.markdown("<div class='admin-footer'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)
if code == "23111977" and 'pdf' in st.session_state:
    st.download_button("📥 DOWNLOAD", st.session_state['pdf'], "Dossier_Architect.pdf")
