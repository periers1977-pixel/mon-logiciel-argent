import streamlit as st
import requests
import hashlib
import io
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY

# --- 1. CONFIGURATION ET MÉMOIRE ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# Initialisation de la mémoire
if 'pdf_save' not in st.session_state:
    st.session_state['pdf_save'] = None
if 'fini' not in st.session_state:
    st.session_state['fini'] = False

# --- 2. DESIGN PRO ET CONTRASTÉ ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    
    .admin-top-bar {
        background-color: #1e1e1e; color: #00ff00; padding: 15px;
        border-radius: 10px; border: 2px solid #00ff00; margin-bottom: 20px;
        text-align: center; font-weight: bold;
    }
    
    .status-box {
        background-color: #007bff; color: white; padding: 20px;
        border-radius: 10px; text-align: center; font-weight: bold; margin: 20px 0;
    }

    .payment-card {
        background: white; padding: 35px; border-radius: 15px;
        border: 2px solid #dee2e6; text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    .price-big { font-size: 50px; font-weight: 900; color: #007bff; margin: 10px 0; }
    .stTextInput input { border: 2px solid #1e1e1e !important; }
    .stButton button { background: #007bff; color: white; font-weight: bold; height: 50px; border-radius: 8px; }
    .concepteur-trigger { position: fixed; bottom: 10px; left: 10px; width: 60px; opacity: 0.1; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIQUE D'ANALYSE ---
API_KEY = "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"

def moteur_expertise(idee, premium=False):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Risques"]
    if premium: axes += ["Scalabilité", "Logistique", "Digital", "Concurrents", "Vente"]
    
    pool = []
    bar = st.progress(0)
    for i, axe in enumerate(axes):
        try:
            query = f"expertise stratégique {axe} {idee} 2026 en français"
            r = requests.post("https://api.tavily.com/search", json={"api_key": API_KEY, "query": query, "search_depth": "advanced" if premium else "basic"}).json()
            txt = " ".join([res['content'] for res in r.get('results', [])])
            if len(txt) > 100: pool.append((axe.upper(), txt))
        except: continue
        bar.progress((i + 1) / len(axes))
    bar.empty()
    return pool

def generer_pdf(data, idee):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    style_body = ParagraphStyle('Body', fontName='Helvetica', fontSize=10, leading=14, alignment=TA_JUSTIFY)
    
    story = [Paragraph(f"<b>Architect Solution Pro : {idee.upper()}</b>", styles["Title"]), Spacer(1, 1*cm)]
    for tit, txt in data:
        story.append(Paragraph(f"<b>{tit}</b>", styles["Heading2"]))
        story.append(Paragraph(txt, style_body))
        story.append(Spacer(1, 0.5*cm))
    doc.build(story)
    buf.seek(0)
    return buf

# --- 4. ACCÈS CONCEPTEUR (EN HAUT) ---
st.markdown("<div class='concepteur-trigger'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code == "23111977":
    st.markdown("<div class='admin-top-bar'>🔓 ACCÈS CONCEPTEUR ACTIVÉ</div>", unsafe_allow_html=True)
    if st.session_state['pdf_save']:
        st.download_button("📥 TÉLÉCHARGER LE DOSSIER", st.session_state['pdf_save'], "Expertise_Pro.pdf")
    else:
        st.info("En attente d'une analyse...")

# --- 5. INTERFACE UTILISATEUR ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
projet = st.text_input("Saisissez votre projet business :", placeholder="ex: Agence de marketing digital...")

c1, c2 = st.columns(2)
with c1:
    if st.button("🚀 ANALYSE STANDARD (9€)"):
        if projet:
            res = moteur_expertise(projet, False)
            if res:
                st.session_state['pdf_save'] = generer_pdf(res, projet)
                st.session_state['fini'] = True
                st.rerun()

with c2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if projet:
            res = moteur_expertise(projet, True)
            if res:
                st.session_state['pdf_save'] = generer_pdf(res, projet)
                st.session_state['fini'] = True
                st.rerun()

# --- 6. AFFICHAGE RÉSULTAT ---
if st.session_state['fini']:
    st.markdown("<div class='status-box'>✅ ANALYSE TERMINÉE : VOTRE DOSSIER EST PRÊT</div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="payment-card">
            <h3>PROJET : {projet.upper() if projet else "SÉLECTIONNÉ"}</h3>
            <p>L'analyse systémique est terminée. Le rapport est prêt pour téléchargement après régularisation.</p>
            <div class="price-big">9.00 €</div>
            <a href="https://buy.stripe.com/votre_lien" style="text-decoration:none;">
                <div style="background:#007bff; color:white; padding:18px; border-radius:10px; font-weight:bold; font-size:1.1em; margin-top:20px;">
                    ACCÉDER AU DOSSIER COMPLET
                </div>
            </a>
        </div>
    """, unsafe_allow_html=True)
