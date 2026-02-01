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

# Initialisation des variables de session pour ne rien perdre
if 'pdf_ready' not in st.session_state:
    st.session_state['pdf_ready'] = None
if 'projet_nom' not in st.session_state:
    st.session_state['projet_nom'] = ""

# --- 2. DESIGN CLAIR ET LISIBLE (Haut Contraste) ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    
    .admin-header {
        background-color: #1e1e1e; color: #00ff00; padding: 15px;
        border-radius: 10px; border: 2px solid #00ff00; margin-bottom: 20px;
        text-align: center; font-weight: bold;
    }
    
    .confirmation-box {
        background-color: #007bff; color: white; padding: 20px;
        border-radius: 10px; text-align: center; font-weight: bold; margin: 20px 0;
    }

    .card-paiement {
        background: white; padding: 35px; border-radius: 15px;
        border: 2px solid #dee2e6; text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    .prix { font-size: 50px; font-weight: 900; color: #007bff; margin: 10px 0; }
    .stTextInput input { border: 2px solid #1e1e1e !important; color: black !important; }
    .stButton button { background: #007bff; color: white; font-weight: bold; height: 50px; border-radius: 8px; width: 100%; }
    .trigger-admin { position: fixed; bottom: 10px; left: 10px; width: 60px; opacity: 0.1; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MOTEUR D'EXTRACTION ---
API_KEY = "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"

def executer_analyse(idee, est_premium=False):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Risques"]
    if est_premium: axes += ["Scalabilité", "Concurrents", "Digital", "Logistique", "Vente"]
    
    resultats = []
    barre = st.progress(0)
    for i, axe in enumerate(axes):
        try:
            query = f"expertise stratégique {axe} {idee} 2026 en français"
            r = requests.post("https://api.tavily.com/search", json={"api_key": API_KEY, "query": query, "search_depth": "advanced" if est_premium else "basic"}).json()
            texte = " ".join([res['content'] for res in r.get('results', [])])
            if len(texte) > 100:
                resultats.append((axe.upper(), texte))
        except: continue
        barre.progress((i + 1) / len(axes))
    barre.empty()
    return resultats

def creer_pdf(data, projet):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    style_corps = ParagraphStyle('Corps', fontName='Helvetica', fontSize=10, leading=14, alignment=TA_JUSTIFY)
    
    elements = [Paragraph(f"<b>Architect Solution Pro : {projet.upper()}</b>", styles["Title"]), Spacer(1, 1*cm)]
    for titre, contenu in data:
        elements.append(Paragraph(f"<b>{titre}</b>", styles["Heading2"]))
        elements.append(Paragraph(contenu, style_corps))
        elements.append(Spacer(1, 0.5*cm))
    doc.build(elements)
    buf.seek(0)
    return buf

# --- 4. ACCÈS CONCEPTEUR (SÉCURISÉ ET PRIORITAIRE) ---
st.markdown("<div class='trigger-admin'>", unsafe_allow_html=True)
code_secret = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code_secret == "23111977":
    st.markdown("<div class='admin-header'>🔓 ACCÈS CONCEPTEUR ACTIVÉ</div>", unsafe_allow_html=True)
    if st.session_state['pdf_ready']:
        st.download_button("📥 TÉLÉCHARGER LE DOSSIER", st.session_state['pdf_ready'], "Expertise_Solution_Pro.pdf")
    else:
        st.info("Aucune analyse en mémoire. Veuillez lancer une génération.")

# --- 5. INTERFACE UTILISATEUR ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
input_projet = st.text_input("Saisissez votre idée business :", placeholder="ex: Boutique e-commerce, Service de conciergerie...")

c1, c2 = st.columns(2)
with c1:
    if st.button("🚀 ANALYSE STANDARD (9€)"):
        if input_projet:
            res = executer_analyse(input_projet, False)
            if res:
                st.session_state['pdf_ready'] = creer_pdf(res, input_projet)
                st.session_state['projet_nom'] = input_projet
                st.rerun()

with c2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if input_projet:
            res = executer_analyse(input_projet, True)
            if res:
                st.session_state['pdf_ready'] = creer_pdf(res, input_projet)
                st.session_state['projet_nom'] = input_projet
                st.rerun()

# --- 6. VISUEL DE CONFIRMATION CLIENT ---
if st.session_state['pdf_ready']:
    st.markdown("<div class='confirmation-box'>✅ ANALYSE TERMINÉE : VOTRE DOSSIER EST PRÊT</div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="card-paiement">
            <h3>PROJET : {st.session_state['projet_nom'].upper()}</h3>
            <p>Notre algorithme a fini l'extraction des données stratégiques mondiales. Votre rapport est sécurisé et prêt pour téléchargement.</p>
            <div class="prix">9.00 €</div>
            <a href="https://buy.stripe.com/votre_lien" style="text-decoration:none;">
                <div style="background:#007bff; color:white; padding:18px; border-radius:10px; font-weight:bold; font-size:1.1em; margin-top:20px;">
                    ACCÉDER À MON DOSSIER COMPLET
                </div>
            </a>
            <p style="font-size:0.8em; color:#666; margin-top:15px;">🔒 Paiement sécurisé Stripe - Réception immédiate</p>
        </div>
    """, unsafe_allow_html=True)
