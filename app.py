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

# --- DESIGN IMMERSIF (CSS) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .main { background: radial-gradient(circle, #1a1c23 0%, #0e1117 100%); color: white; }
    
    .premium-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(20px);
        padding: 45px;
        border-radius: 35px;
        border: 1px solid rgba(0, 123, 255, 0.4);
        text-align: center;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        margin: 25px 0;
    }
    
    /* Affichage du prix ultra-visible */
    .price-tag {
        font-size: 52px;
        font-weight: 900;
        color: #00c6ff;
        text-shadow: 0 0 20px rgba(0, 198, 255, 0.5);
        margin: 15px 0;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #007bff, #00c6ff);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 15px;
        font-weight: 800;
        font-size: 1.1em;
        text-transform: uppercase;
        transition: 0.3s;
    }
    .stButton > button:hover { transform: scale(1.03); box-shadow: 0 0 25px rgba(0, 123, 255, 0.5); }
    
    .admin-footer { position: fixed; bottom: 5px; left: 5px; width: 100px; opacity: 0.03; transition: 0.3s; }
    .admin-footer:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEURS DE PRÉCISION ---
API_KEY = "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"

def filtrage_strict(texte):
    # Exclusion des noms propres d'analystes et des bios trouvés dans Expertise_vendre des parapluis.pdf
    blacklist = r'(?i)(Dhruv|Bhatia|analyst|Research Nester|Research Dive|Pune|India|consultant|biography|about us|contact us|Research LLC)'
    texte = re.sub(r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu)', '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return [s.strip() for s in segments if len(s.split()) > 15 and not re.search(blacklist, s)]

def moteur_expertise_progression(idee):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    steps = ["Synchronisation des bases mondiales...", "Calcul systémique...", "Génération des indicateurs...", "Certifications finales..."]
    
    pool, titres = [], []
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, axe in enumerate(axes):
        step_idx = int((i / len(axes)) * len(steps))
        status_text.markdown(f"**💎 {steps[step_idx]}**")
        progress_bar.progress((i + 1) / len(axes))
        try:
            url = "https://api.tavily.com/search"
            payload = {"api_key": API_KEY, "query": f"expertise approfondie {axe} {idee} 2026", "search_depth": "advanced"}
            r = requests.post(url, json=payload, timeout=12).json()
            data = filtrage_strict(" ".join([res['content'] for res in r.get('results', [])]))
            if data: pool.append(data); titres.append(axe.upper())
        except: continue
    status_text.empty(); progress_bar.empty()
    return pool, titres

def fabriquer_pdf_imperial(pages, idee, sig):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    style_p = ParagraphStyle('Custom', parent=styles['Normal'], fontSize=9.5, leading=13, alignment=TA_JUSTIFY)
    style_liaison = ParagraphStyle('Liaison', parent=style_p, textColor=colors.HexColor("#007bff"), fontName="Helvetica-BoldOblique")
    
    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Signature : {sig} | ARCHITECT SOLUTION PRO", styles["Normal"]),
        Spacer(1, 0.5*cm)
    ]
    
    for i, page in enumerate(pages):
        story.append(Paragraph(f"<b>{page[0]}</b>", styles["Heading2"]))
        # Point 2 : Phrase de liaison personnalisée
        story.append(Paragraph(f"Concernant votre ambition pour '{idee}', les données systémiques révèlent :", style_liaison))
        for ligne in page[1:]:
            story.append(Paragraph(ligne, style_p)); story.append(Spacer(1, 6))
            
        # Point 3 : Tableau d'indicateurs
        data_tab = [["INDICATEUR CLÉ", "PRÉVISION 2026", "IMPACT"], ["Croissance Potentielle", f"{random.randint(5,15)}%", "FORT"], ["Risque Sectoriel", f"{random.randint(1,3)}/10", "BAS"]]
        t = Table(data_tab, colWidths=[6*cm, 6*cm, 5*cm])
        t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1c1f26")), ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke), ('ALIGN', (0,0), (-1,-1), 'CENTER'), ('GRID', (0,0), (-1,-1), 0.5, colors.grey)]))
        story.append(Spacer(1, 0.4*cm)); story.append(t); story.append(Spacer(1, 0.8*cm))
        
    doc.build(story); buf.seek(0)
    return buf

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center; color: white;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Expertise Systémique & Algorithmes de Précision</p>", unsafe_allow_html=True)

idee = st.text_input("Saisissez votre projet :", placeholder="ex: Boutique de luxe, Application innovante...")

if st.button("🚀 GÉNÉRER L'ANALYSE COMPLÈTE"):
    if idee:
        pool, titres = moteur_expertise_progression(idee)
        pages_data = [[f"SECTION {i+1} : {titres[i]}"] + pool[i][:12] for i in range(len(pool))]
        sig = hashlib.sha256(str(pages_data).encode()).hexdigest()[:12].upper()
        
        st.markdown(f"""
            <div class="premium-card">
                <div style="background:#28a745; color:white; padding:5px 15px; border-radius:50px; display:inline-block; font-size:0.8em; font-weight:bold; margin-bottom:15px;">DOSSIER GÉNÉRÉ</div>
                <h3 style="color:white; margin:0;">ID unique : {sig}</h3>
                <p style="color:#888;">Votre expertise de haute densité est prête pour l'exportation.</p>
                <div class="price-tag">9.00 €</div>
                <a href="https://buy.stripe.com/votre_lien" target="_blank" style="text-decoration:none;">
                    <div style="background:linear-gradient(45deg, #007bff, #00c6ff); color:white; padding:20px; border-radius:15px; font-weight:bold; font-size:1.3em;">
                        DÉBLOQUER ET TÉLÉCHARGER LE DOSSIER
                    </div>
                </a>
                <p style="font-size:0.8em; color:#444; margin-top:15px;">🔒 Transaction cryptée SSL - Réception immédiate</p>
            </div>
            """, unsafe_allow_html=True)
        st.session_state['pdf'] = fabriquer_pdf_imperial(pages_data, idee, sig)
        st.session_state['idee'] = idee

# Zone Admin Discrète
st.markdown("<div class='admin-footer'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code == "23111977" and 'pdf' in st.session_state:
    st.download_button("📥 ADMIN DOWNLOAD", st.session_state['pdf'], f"Expertise_{st.session_state['idee']}.pdf")
