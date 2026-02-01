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

# --- 1. INITIALISATION CRITIQUE (NE PAS MODIFIER) ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# Cette zone garde le PDF en mémoire même si la page se rafraîchit
if 'pdf_binaire' not in st.session_state:
    st.session_state['pdf_binaire'] = None
if 'nom_projet' not in st.session_state:
    st.session_state['nom_projet'] = ""

# --- 2. DESIGN HAUTE VISIBILITÉ ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    
    .bandeau-admin {
        background-color: #1e1e1e; color: #00ff00; padding: 20px;
        border-radius: 12px; border: 2px solid #00ff00; margin-bottom: 25px;
        text-align: center; font-weight: bold; font-family: monospace;
    }
    
    .confirmation-paiement {
        background-color: #007bff; color: white; padding: 25px;
        border-radius: 15px; text-align: center; font-weight: bold; margin: 20px 0;
        border: 2px solid #0056b3;
    }

    .card-stripe {
        background: white; padding: 40px; border-radius: 20px;
        border: 1px solid #dee2e6; text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    .big-price { font-size: 55px; font-weight: 900; color: #007bff; margin: 15px 0; }
    .stTextInput input { border: 2px solid #000 !important; height: 50px !important; }
    .stButton button { background: #007bff; color: white; font-weight: bold; height: 55px; border-radius: 12px; font-size: 1.1em; }
    .admin-key { position: fixed; bottom: 10px; left: 10px; width: 80px; opacity: 0.1; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIQUE TECHNIQUE ---
API_KEY = "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"

def extraire_donnees(idee, premium=False):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Risques"]
    if premium: axes += ["Scalabilité", "Logistique", "Digital", "Concurrents", "Vente"]
    
    contenu_final = []
    progression = st.progress(0)
    for i, axe in enumerate(axes):
        try:
            query = f"expertise stratégique {axe} {idee} 2026 en français"
            r = requests.post("https://api.tavily.com/search", json={"api_key": API_KEY, "query": query, "search_depth": "advanced" if premium else "basic"}).json()
            texte = " ".join([res['content'] for res in r.get('results', [])])
            if len(texte) > 100:
                contenu_final.append((axe.upper(), texte))
        except: continue
        progression.progress((i + 1) / len(axes))
    progression.empty()
    return contenu_final

def generer_pdf_officiel(data, idee):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    style_texte = ParagraphStyle('Corps', fontName='Helvetica', fontSize=10, leading=14, alignment=TA_JUSTIFY)
    
    elements = [Paragraph(f"<b>Architect Solution Pro : {idee.upper()}</b>", styles["Title"]), Spacer(1, 1*cm)]
    for titre, corps in data:
        elements.append(Paragraph(f"<b>{titre}</b>", styles["Heading2"]))
        elements.append(Paragraph(corps, style_texte))
        elements.append(Spacer(1, 0.5*cm))
    doc.build(elements)
    buffer.seek(0)
    return buffer

# --- 4. MODE CONCEPTEUR (ACCÈS DIRECT) ---
st.markdown("<div class='admin-key'>", unsafe_allow_html=True)
cle_concepteur = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if cle_concepteur == "23111977":
    st.markdown("<div class='bandeau-admin'>🔓 MODE CONCEPTEUR : ACCÈS AU FICHIER GÉNÉRÉ</div>", unsafe_allow_html=True)
    if st.session_state['pdf_binaire']:
        st.download_button("📥 TÉLÉCHARGER LE DOSSIER ICI", st.session_state['pdf_binaire'], "Expertise_Final.pdf")
    else:
        st.warning("Aucune analyse en mémoire. Saisissez un projet et lancez le moteur ci-dessous.")

# --- 5. INTERFACE CLIENT ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
input_user = st.text_input("Saisissez votre idée business :", placeholder="ex: Agence immobilière, Glacier ambulant...")

c1, c2 = st.columns(2)
with c1:
    if st.button("🚀 ANALYSE STANDARD (9€)"):
        if input_user:
            res = extraire_donnees(input_user, False)
            if res:
                st.session_state['pdf_binaire'] = generer_pdf_officiel(res, input_user)
                st.session_state['nom_projet'] = input_user
                st.rerun()

with c2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if input_user:
            res = extraire_donnees(input_user, True)
            if res:
                st.session_state['pdf_binaire'] = generer_pdf_officiel(res, input_user)
                st.session_state['nom_projet'] = input_user
                st.rerun()

# --- 6. AFFICHAGE APRÈS GÉNÉRATION ---
if st.session_state['pdf_binaire']:
    st.markdown("<div class='confirmation-paiement'>✅ ANALYSE TERMINÉE : VOTRE DOSSIER EST SÉCURISÉ ET PRÊT</div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="card-stripe">
            <h3>PROJET : {st.session_state['nom_projet'].upper()}</h3>
            <p>Le moteur d'expertise a fini de compiler les données mondiales. Votre rapport complet est prêt pour téléchargement immédiat après régularisation.</p>
            <div class="big-price">9.00 €</div>
            <a href="https://buy.stripe.com/votre_lien" style="text-decoration:none;">
                <div style="background:#007bff; color:white; padding:18px; border-radius:10px; font-weight:bold; font-size:1.2em; margin-top:15px;">
                    ACCÉDER À MON EXPERTISE COMPLÈTE
                </div>
            </a>
            <p style="font-size:0.8em; color:#666; margin-top:15px;">🔒 Transaction cryptée SSL - Accès immédiat au fichier PDF</p>
        </div>
    """, unsafe_allow_html=True)
