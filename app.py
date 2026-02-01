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

# --- DESIGN IMMERSIF (CSS AVANCÉ) ---
st.markdown("""
    <style>
    /* Masquage des éléments natifs */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Fond dégradé animé */
    .main {
        background: linear-gradient(135deg, #0e1117 0%, #161b22 100%);
        color: #ffffff;
    }
    
    /* Carte de paiement stylisée (Glassmorphism) */
    .premium-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 40px;
        border: 1px solid rgba(0, 198, 255, 0.2);
        text-align: center;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        margin: 20px 0;
    }
    
    /* Boutons personnalisés */
    .stButton > button {
        background: linear-gradient(45deg, #007bff, #00c6ff);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: 0.4s;
    }
    .stButton > button:hover {
        box-shadow: 0 0 20px rgba(0, 198, 255, 0.6);
        transform: translateY(-2px);
    }
    
    /* Badge de succès */
    .status-badge {
        background: linear-gradient(45deg, #28a745, #85e085);
        padding: 8px 20px;
        border-radius: 50px;
        font-size: 0.8em;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 20px;
    }

    /* Admin discret */
    .admin-zone {
        position: fixed;
        bottom: 10px;
        left: 10px;
        width: 100px;
        opacity: 0.05;
        transition: 0.3s;
    }
    .admin-zone:hover { opacity: 0.8; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR D'EXTRACTION ---
API_KEY = "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"

def purger(texte):
    bruit = r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu)'
    texte = re.sub(bruit, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return list(dict.fromkeys([p.strip() for p in segments if len(p.split()) > 12]))

def moteur_expertise(idee):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    pool, titres = [], []
    with st.spinner("💎 Algorithme : Analyse systémique en cours..."):
        for axe in axes:
            try:
                url = "https://api.tavily.com/search"
                payload = {"api_key": API_KEY, "query": f"expertise approfondie {axe} {idee} 2026", "search_depth": "advanced"}
                r = requests.post(url, json=payload, timeout=12).json()
                data = purger(" ".join([res['content'] for res in r.get('results', [])]))
                if data:
                    pool.append(data); titres.append(axe.upper())
            except: continue
    return pool, titres

def fabriquer_pdf(pages, idee, sig):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    style_p = styles["Normal"]; style_p.alignment, style_p.fontSize, style_p.leading = TA_JUSTIFY, 9.5, 12
    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Signature d'Authenticité : {sig} | 2026", styles["Normal"]),
        Spacer(1, 0.5*cm)
    ]
    for page in pages:
        story.append(Paragraph(f"<b>{page[0]}</b>", styles["Heading2"]))
        for ligne in page[1:]:
            story.append(Paragraph(ligne, style_p))
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 0.4*cm))
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center; color: white;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00c6ff; font-weight: bold;'>ANALYSES STRATÉGIQUES DE HAUTE PRÉCISION</p>", unsafe_allow_html=True)

idee = st.text_input("Saisissez votre projet :", placeholder="ex: Cabinet de conseil en luxe, Agence immobilière...")

if st.button("🚀 LANCER L'ANALYSE"):
    if idee:
        pool, titres = moteur_expertise(idee)
        pages = []
        for i in range(len(pool)):
            pages.append([f"SECTION {i+1} : {titres[i]}"] + pool[i][:15])
        sig = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
        
        st.markdown(f"""
            <div class="premium-card">
                <div class="status-badge">GÉNÉRATION TERMINÉE</div>
                <h3 style="color: white; margin-bottom: 5px;">Rapport de Haute Densité</h3>
                <p style="color: #888;">ID unique : {sig}</p>
                <div style="margin: 25px 0; border-top: 1px solid rgba(255,255,255,0.1);"></div>
                <p style="font-size: 36px; font-weight: bold; color: white; margin-bottom: 10px;">9.00 €</p>
                <a href="https://buy.stripe.com/votre_lien" target="_blank" style="text-decoration: none;">
                    <div style="background: linear-gradient(45deg, #007bff, #00c6ff); color: white; padding: 18px; border-radius: 12px; font-weight: bold; font-size: 1.2em; box-shadow: 0 4px 15px rgba(0,198,255,0.3);">
                        DÉBLOQUER ET TÉLÉCHARGER LE DOSSIER
                    </div>
                </a>
                <p style="font-size: 0.8em; color: #555; margin-top: 15px;">🔒 Document certifié - Accès sécurisé SSL</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.session_state['current_pdf'] = fabriquer_pdf(pages, idee, sig)
        st.session_state['current_idee'] = idee

# --- ZONE ADMIN ---
st.markdown("<div class='admin-zone'>", unsafe_allow_html=True)
code_admin = st.text_input("Accès", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code_admin == "23111977" and 'current_pdf' in st.session_state:
    st.download_button("📥 TÉLÉCHARGER (ADMIN)", st.session_state['current_pdf'], f"Expertise_{st.session_state['current_idee']}.pdf")
