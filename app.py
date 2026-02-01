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

# CSS : Interface de Luxe et masquage des menus natifs
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Fond Immersif */
    .main { 
        background: radial-gradient(circle, #1a1c23 0%, #0e1117 100%);
        color: white;
    }
    
    /* Carte de Paiement Premium */
    .payment-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 25px;
        border: 1px solid rgba(0, 123, 255, 0.3);
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.7);
        margin-top: 20px;
    }
    
    .success-badge {
        background-color: #28a745;
        color: white;
        padding: 10px 20px;
        border-radius: 50px;
        display: inline-block;
        margin-bottom: 15px;
        font-weight: bold;
    }
    
    /* Admin ultra-discret */
    .admin-footer {
        position: fixed;
        bottom: 5px;
        left: 5px;
        width: 150px;
        opacity: 0.15;
    }
    .admin-footer:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR INTERNE (SANS TERME IA) ---
API_KEY = "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"

def filtrage_donnees(texte):
    bruit = r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu)'
    texte = re.sub(bruit, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return list(dict.fromkeys([p.strip() for p in segments if len(p.split()) > 12]))

def moteur_expertise(idee):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    pool, titres = [], []
    with st.spinner("💎 Algorithme : Extraction de l'expertise sectorielle..."):
        for axe in axes:
            try:
                url = "https://api.tavily.com/search"
                payload = {"api_key": API_KEY, "query": f"expertise approfondie {axe} {idee} 2026", "search_depth": "advanced"}
                r = requests.post(url, json=payload, timeout=12).json()
                data = filtrage_donnees(" ".join([res['content'] for res in r.get('results', [])]))
                if data:
                    pool.append(data); titres.append(axe.upper())
            except: continue
    return pool, titres

def fabriquer_pdf_expert(pages, idee, sig):
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
        story.append(Spacer(1, 0.3*cm))
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center; color: white;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #777;'>Expertise Systémique & Analyse de Données Mondiales</p>", unsafe_allow_html=True)

idee = st.text_input("Saisissez votre projet pour lancer l'algorithme :", placeholder="ex: Cabinet de consulting, boutique en ligne...")

if st.button("🚀 GÉNÉRER MON EXPERTISE"):
    if idee:
        pool, titres = moteur_expertise(idee)
        pages = []
        for i in range(len(pool)):
            pages.append([f"SECTION {i+1} : {titres[i]}"] + pool[i][:15])
        sig = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
        
        st.markdown(f"""
            <div class="payment-card">
                <div class="success-badge">ANALYSE TERMINÉE</div>
                <h3 style="color: white;">Dossier Réf: {sig}</h3>
                <p style="color: #ccc;">Votre expertise intégrale de haute densité est prête.</p>
                <hr style="border: 0.1px solid #333;">
                <p style="font-size: 28px; font-weight: bold; color: #007bff;">9.00 €</p>
                <a href="https://buy.stripe.com/votre_lien" target="_blank" style="text-decoration: none;">
                    <div style="background: #007bff; color: white; padding: 18px; border-radius: 12px; font-weight: bold; font-size: 1.1em;">
                        DÉBLOQUER ET TÉLÉCHARGER LE DOSSIER
                    </div>
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        st.session_state['current_pdf'] = fabriquer_pdf_expert(pages, idee, sig)
        st.session_state['current_idee'] = idee

# --- ZONE ADMIN ULTRA-DISCRÈTE (FIXÉE EN BAS À GAUCHE) ---
st.markdown("<div class='admin-footer'>", unsafe_allow_html=True)
code_admin = st.text_input("Accès :", type="password")
st.markdown("</div>", unsafe_allow_html=True)

if code_admin == "23111977" and 'current_pdf' in st.session_state:
    st.download_button("📥 TÉLÉCHARGER (ADMIN)", st.session_state['current_pdf'], f"Expertise_{st.session_state['current_idee']}.pdf")
