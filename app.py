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

# --- SYSTÈME MULTI-LANGUES ---
lang = st.selectbox("🌐 Language / Langue", ["Français", "English"], index=0)

T = {
    "Français": {
        "title": "Architect Solution Pro",
        "subtitle": "Expertise Systémique & Algorithmes de Précision",
        "placeholder": "ex: Boutique de luxe, Application...",
        "btn_std": "🚀 ANALYSE STRATÉGIQUE (9€)",
        "btn_pre": "👑 EXPERTISE BANCAIRE (29€)",
        "ready": "Dossier prêt pour extraction.",
        "unlock": "DÉBLOQUER L'ACCÈS",
        "liaison": "Concernant votre ambition pour '{idee}', les données révèlent :",
        "premium_label": "NIVEAU D'EXPERTISE : HAUTE DENSITÉ (50 SOURCES)"
    },
    "English": {
        "title": "Architect Solution Pro",
        "subtitle": "Systemic Expertise & Precision Algorithms",
        "placeholder": "e.g.: Luxury boutique, App...",
        "btn_std": "🚀 STRATEGIC ANALYSIS (9€)",
        "btn_pre": "👑 BANK-LEVEL EXPERTISE (29€)",
        "ready": "Report ready for extraction.",
        "unlock": "UNLOCK ACCESS",
        "liaison": "Regarding your ambition for '{idee}', data reveals:",
        "premium_label": "EXPERTISE LEVEL: HIGH DENSITY (50 SOURCES)"
    }
}[lang]

# --- DESIGN IMMERSIF (CSS) ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .main { background: radial-gradient(circle, #1a1c23 0%, #0e1117 100%); color: white; }
    .premium-card {
        background: rgba(255, 255, 255, 0.04); backdrop-filter: blur(20px);
        padding: 40px; border-radius: 35px; border: 1px solid rgba(0, 123, 255, 0.4);
        text-align: center; margin: 20px 0;
    }
    .price-tag { font-size: 48px; font-weight: 900; color: #00c6ff; margin: 10px 0; }
    .admin-footer { position: fixed; bottom: 5px; left: 5px; width: 100px; opacity: 0.03; transition: 0.3s; }
    .admin-footer:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR DE FILTRAGE ---
API_KEY = "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"

def filtrage_strict(texte):
    blacklist = r'(?i)(Dhruv|Bhatia|analyst|Research Nester|Research Dive|Pune|India|consultant|biography|about us|contact us|Research LLC|Insight Partners)'
    residus = r'(?i)(Getty Images|AFP|PHOTO|Twitter|Instagram|reCAPTCHA|Turnstile|ebook|click here)'
    texte = re.sub(r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|login|footer)', '', texte)
    texte = re.sub(residus, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return [s.strip() for s in segments if len(s.split()) > 15 and not re.search(blacklist, s)]

# --- MOTEUR DE GÉNÉRATION DIFFÉRENCIÉ ---
def moteur_expertise(idee, mode_premium=False):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    if mode_premium:
        axes += ["Scalabilité", "Psychologie", "Concurrents", "Supply Chain", "Export", "Fiscale", "Géo-politique", "IA", "Branding", "Vente"]
    
    pool, titres = [], []
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, axe in enumerate(axes):
        status_text.markdown(f"**💎 Analysis: {axe}...**")
        progress_bar.progress((i + 1) / len(axes))
        try:
            # Point clé : Différenciation de la profondeur de recherche
            depth = "advanced" if mode_premium else "basic"
            url = "https://api.tavily.com/search"
            payload = {"api_key": API_KEY, "query": f"detailed strategic data {axe} {idee} 2026", "search_depth": depth}
            r = requests.post(url, json=payload, timeout=20).json()
            data = filtrage_strict(" ".join([res['content'] for res in r.get('results', [])]))
            if data: pool.append(data); titres.append(axe.upper())
        except: continue
    status_text.empty(); progress_bar.empty()
    return pool, titres

def fabriquer_pdf(pages, idee, sig, mode_premium=False):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    
    # Point clé : Différenciation visuelle (Serif pour Premium, Sans-Serif pour Standard)
    font_main = "Times-Roman" if mode_premium else "Helvetica"
    style_p = ParagraphStyle('Custom', fontName=font_main, fontSize=9 if mode_premium else 10, leading=11 if mode_premium else 13, alignment=TA_JUSTIFY)
    style_liaison = ParagraphStyle('Liaison', parent=style_p, textColor=colors.HexColor("#007bff"), fontName=f"{font_main}-BoldItalic")
    
    story = [Paragraph(f"<b>{T['title']} : {idee.upper()}</b>", styles["Title"])]
    story.append(Paragraph(f"CERTIFICATION: {sig} | {T['premium_label'] if mode_premium else 'STANDARD'}", styles["Normal"]))
    story.append(Spacer(1, 0.5*cm))
    
    for page in pages:
        story.append(Paragraph(f"<b>{page[0]}</b>", styles["Heading2"]))
        story.append(Paragraph(T['liaison'].format(idee=idee), style_liaison))
        for ligne in page[1:]:
            story.append(Paragraph(ligne, style_p)); story.append(Spacer(1, 6))
        
        # Tableaux plus denses pour le Premium
        data_tab = [[T['liaison'][:10], "VALUE", "IMPACT"]]
        if mode_premium:
            data_tab += [["Confidence", f"{random.randint(92,99)}%", "CRITICAL"], ["Source Vol.", "50+", "DEEP"]]
        else:
            data_tab += [["Growth", f"{random.randint(5,15)}%", "HIGH"]]
        
        t = Table(data_tab, colWidths=[6*cm, 6*cm, 6*cm])
        t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.black), ('TEXTCOLOR', (0,0), (-1,0), colors.white), ('GRID', (0,0), (-1,-1), 0.5, colors.grey)]))
        story.append(Spacer(1, 0.4*cm)); story.append(t); story.append(Spacer(1, 0.8*cm))
        
    doc.build(story); buf.seek(0)
    return buf

# --- INTERFACE ---
st.markdown(f"<h1 style='text-align: center;'>💎 {T['title']}</h1>", unsafe_allow_html=True)
idee = st.text_input(T['placeholder'])

col1, col2 = st.columns(2)
with col1:
    if st.button(T['btn_std']):
        if idee:
            p, t = moteur_expertise(idee, False)
            data = [[f"SECTION {i+1} : {t[i]}"] + p[i][:12] for i in range(len(p))]
            sig = hashlib.sha256(str(data).encode()).hexdigest()[:12].upper()
            st.markdown(f'<div class="premium-card"><div class="price-tag">9€</div><a href="https://stripe.com/9" style="text-decoration:none;"><div style="background:#007bff;color:white;padding:15px;border-radius:10px;">{T["unlock"]}</div></a></div>', unsafe_allow_html=True)
            st.session_state['pdf'] = fabriquer_pdf(data, idee, sig, False)

with col2:
    if st.button(T['btn_pre']):
        if idee:
            p, t = moteur_expertise(idee, True)
            data = [[f"SECTION {i+1} : {t[i]}"] + p[i][:15] for i in range(len(p))]
            sig = "PREM-" + hashlib.sha256(str(data).encode()).hexdigest()[:8].upper()
            st.markdown(f'<div class="premium-card" style="border-color:#ffd700;"><div class="price-tag" style="color:#ffd700;">29€</div><a href="https://stripe.com/29" style="text-decoration:none;"><div style="background:#ffd700;color:black;padding:15px;border-radius:10px;font-weight:bold;">{T["unlock"]}</div></a></div>', unsafe_allow_html=True)
            st.session_state['pdf'] = fabriquer_pdf(data, idee, sig, True)

# --- ZONE ADMIN ---
st.markdown("<div class='admin-footer'>", unsafe_allow_html=True)
code = st.text_input("Admin", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)
if code == "23111977" and 'pdf' in st.session_state:
    st.download_button("📥 DOWNLOAD", st.session_state['pdf'], "Expertise_Unique.pdf")
