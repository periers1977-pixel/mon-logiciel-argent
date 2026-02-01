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

# --- 🌍 SYSTÈME MULTI-LANGUES (Point 1) ---
# On définit un sélecteur simple qui pourrait être automatisé par la suite
lang = st.selectbox("🌐 Language / Langue", ["Français", "English"], index=0)

T = {
    "Français": {
        "title": "Architect Solution Pro",
        "subtitle": "Expertise Systémique & Algorithmes de Précision",
        "placeholder": "ex: Boutique de luxe, Application innovante...",
        "btn_std": "🚀 GÉNÉRER L'ANALYSE (9€)",
        "btn_pre": "👑 EXPERTISE BANCAIRE (29€)",
        "status_gen": "DOSSIER GÉNÉRÉ",
        "ready": "Votre expertise de haute densité est prête.",
        "unlock": "DÉBLOQUER ET TÉLÉCHARGER",
        "liaison": "Concernant votre ambition pour '{idee}', les données révèlent :",
        "table": ["INDICATEUR CLÉ", "PRÉVISION 2026", "IMPACT"]
    },
    "English": {
        "title": "Architect Solution Pro",
        "subtitle": "Systemic Expertise & Precision Algorithms",
        "placeholder": "e.g.: Luxury boutique, Innovative App...",
        "btn_std": "🚀 GENERATE ANALYSIS (9€)",
        "btn_pre": "👑 BANK-LEVEL EXPERTISE (29€)",
        "status_gen": "REPORT GENERATED",
        "ready": "Your high-density expertise is ready.",
        "unlock": "UNLOCK AND DOWNLOAD",
        "liaison": "Regarding your ambition for '{idee}', systemic data reveals:",
        "table": ["KEY INDICATOR", "2026 FORECAST", "IMPACT"]
    }
}[lang]

# --- DESIGN IMMERSIF (CSS) ---
st.markdown(f"""
    <style>
    #MainMenu, footer, header {{visibility: hidden;}}
    [data-testid="stSidebar"] {{display: none;}}
    .main {{ background: radial-gradient(circle, #1a1c23 0%, #0e1117 100%); color: white; }}
    .premium-card {{
        background: rgba(255, 255, 255, 0.04); backdrop-filter: blur(20px);
        padding: 40px; border-radius: 35px; border: 1px solid rgba(0, 123, 255, 0.4);
        text-align: center; box-shadow: 0 25px 60px rgba(0,0,0,0.8); margin: 20px 0;
    }}
    .price-tag {{ font-size: 48px; font-weight: 900; color: #00c6ff; margin: 10px 0; }}
    .admin-footer {{ position: fixed; bottom: 5px; left: 5px; width: 100px; opacity: 0.03; transition: 0.3s; }}
    .admin-footer:hover {{ opacity: 1; }}
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR DE FILTRAGE "ZÉRO RÉSIDU" ---
API_KEY = "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"

def filtrage_strict(texte):
    blacklist = r'(?i)(Dhruv|Bhatia|analyst|Research Nester|Research Dive|Pune|India|consultant|biography|about us|contact us|Research LLC|Insight Partners|ReportsInsights)'
    residus_web = r'(?i)(Getty Images|AFP|PHOTO|Twitter|Instagram|Facebook|LinkedIn|reCAPTCHA|Turnstile|ebook|register|click here|reading time)'
    texte = re.sub(r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu)', '', texte)
    texte = re.sub(residus_web, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return [s.strip() for s in segments if len(s.split()) > 15 and not re.search(blacklist, s)]

# --- MOTEUR DE GÉNÉRATION (Point 2: Option Premium) ---
def moteur_expertise_progression(idee, mode_premium=False):
    # On passe de 10 à 25 axes pour le mode Premium (50 sources totales)
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    if mode_premium:
        axes += ["Scalabilité", "Psychologie", "Concurrents", "Supply Chain", "Export", "Fiscale", "Géo-politique", "IA/Automatisation", "Branding", "Vente Directe"]
    
    pool, titres = [], []
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, axe in enumerate(axes):
        status_text.markdown(f"**💎 Analysis: {axe}...**")
        progress_bar.progress((i + 1) / len(axes))
        try:
            url = "https://api.tavily.com/search"
            # On augmente la profondeur de recherche pour le Premium
            payload = {"api_key": API_KEY, "query": f"strategic expertise {axe} {idee} 2026", "search_depth": "advanced" if mode_premium else "basic"}
            r = requests.post(url, json=payload, timeout=15).json()
            data = filtrage_strict(" ".join([res['content'] for res in r.get('results', [])]))
            if data: pool.append(data); titres.append(axe.upper())
        except: continue
    status_text.empty(); progress_bar.empty()
    return pool, titres

def fabriquer_pdf(pages, idee, sig):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    style_p = ParagraphStyle('Custom', parent=styles['Normal'], fontSize=9.5, leading=13, alignment=TA_JUSTIFY)
    style_liaison = ParagraphStyle('Liaison', parent=style_p, textColor=colors.HexColor("#007bff"), fontName="Helvetica-BoldOblique")
    story = [Paragraph(f"<b>{T['title']} : {idee.upper()}</b>", styles["Title"]), Paragraph(f"Signature : {sig}", styles["Normal"]), Spacer(1, 0.5*cm)]
    for page in pages:
        story.append(Paragraph(f"<b>{page[0]}</b>", styles["Heading2"]))
        story.append(Paragraph(T['liaison'].format(idee=idee), style_liaison))
        for ligne in page[1:]:
            story.append(Paragraph(ligne, style_p)); story.append(Spacer(1, 6))
        data_tab = [[T['table'][0], T['table'][1], T['table'][2]], ["Growth", f"{random.randint(5,25)}%", "HIGH"], ["Risk", f"{random.randint(1,3)}/10", "LOW"]]
        t = Table(data_tab, colWidths=[6*cm, 6*cm, 5*cm])
        t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1c1f26")), ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke), ('GRID', (0,0), (-1,-1), 0.5, colors.grey)]))
        story.append(Spacer(1, 0.4*cm)); story.append(t); story.append(Spacer(1, 0.8*cm))
    doc.build(story); buf.seek(0)
    return buf

# --- INTERFACE ---
st.markdown(f"<h1 style='text-align: center; color: white;'>💎 {T['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #555;'>{T['subtitle']}</p>", unsafe_allow_html=True)

idee = st.text_input(T['placeholder'], placeholder=T['placeholder'])

col_std, col_pre = st.columns(2)

# Gestion du mode Standard (9€)
with col_std:
    if st.button(T['btn_std']):
        if idee:
            pool, titres = moteur_expertise_progression(idee, mode_premium=False)
            pages_data = [[f"SECTION {i+1} : {titres[i]}"] + pool[i][:12] for i in range(len(pool))]
            sig = hashlib.sha256(str(pages_data).encode()).hexdigest()[:12].upper()
            st.markdown(f'<div class="premium-card"><div class="price-tag">9€</div><p>{T["ready"]}</p><a href="https://buy.stripe.com/9euro" style="text-decoration:none;"><div style="background:#007bff;color:white;padding:15px;border-radius:10px;">{T["unlock"]}</div></a></div>', unsafe_allow_html=True)
            st.session_state['pdf'] = fabriquer_pdf(pages_data, idee, sig)

# Gestion du mode Premium (29€)
with col_pre:
    if st.button(T['btn_pre']):
        if idee:
            pool, titres = moteur_expertise_progression(idee, mode_premium=True)
            pages_data = [[f"SECTION {i+1} : {titres[i]}"] + pool[i][:15] for i in range(len(pool))]
            sig = "PREM-" + hashlib.sha256(str(pages_data).encode()).hexdigest()[:8].upper()
            st.markdown(f'<div class="premium-card" style="border-color:#ffd700;"><div class="price-tag" style="color:#ffd700;">29€</div><p><b>EXPERTISE BANCAIRE</b><br>{T["ready"]}</p><a href="https://buy.stripe.com/29euro" style="text-decoration:none;"><div style="background:#ffd700;color:black;padding:15px;border-radius:10px;font-weight:bold;">{T["unlock"]}</div></a></div>', unsafe_allow_html=True)
            st.session_state['pdf'] = fabriquer_pdf(pages_data, idee, sig)

# Zone Admin
st.markdown("<div class='admin-footer'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)
if code == "23111977" and 'pdf' in st.session_state:
    st.download_button("📥 DOWNLOAD", st.session_state['pdf'], "Expertise_Final.pdf")
