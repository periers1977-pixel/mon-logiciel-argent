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

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# Clé API en dur pour éviter les erreurs de lecture de "secrets"
API_KEY = "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"

if 'pdf_binaire' not in st.session_state:
    st.session_state['pdf_binaire'] = None
if 'nom_projet' not in st.session_state:
    st.session_state['nom_projet'] = ""

# --- 2. DESIGN ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    .admin-bar {
        background-color: #1e1e1e; color: #00ff00; padding: 15px;
        border-radius: 10px; border: 2px solid #00ff00; margin-bottom: 20px;
        text-align: center; font-weight: bold;
    }
    .prix-tag { font-size: 50px; font-weight: 900; color: #007bff; text-align: center; }
    .stTextInput input { border: 2px solid #000 !important; color: black !important; }
    .stButton button { background: #007bff; color: white; font-weight: bold; height: 50px; border-radius: 8px; width: 100%; }
    .trigger-secret { position: fixed; bottom: 10px; left: 10px; width: 60px; opacity: 0.1; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MOTEUR D'ANALYSE ---
def moteur_expertise(idee, premium=False):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Risques"]
    if premium: 
        axes += ["Scalabilité", "Concurrents", "Logistique", "Digital", "Vente"]
    
    resultats = []
    barre = st.progress(0)
    for i, axe in enumerate(axes):
        try:
            query = f"expertise approfondie {axe} {idee} 2026 en français"
            r = requests.post("https://api.tavily.com/search", 
                             json={"api_key": API_KEY, "query": query, "search_depth": "advanced" if premium else "basic"},
                             timeout=20).json()
            
            # Extraction brute sans filtres trop agressifs pour éviter les pages vides
            textes = [res['content'] for res in r.get('results', []) if len(res['content']) > 50]
            if textes:
                resultats.append((axe.upper(), textes))
        except:
            continue
        barre.progress((i + 1) / len(axes))
    barre.empty()
    return resultats

def generer_pdf(data, projet):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    style_p = ParagraphStyle('Corps', fontName='Helvetica', fontSize=10, leading=14, alignment=TA_JUSTIFY)
    
    elements = [Paragraph(f"<b>Architect Solution Pro : {projet.upper()}</b>", styles["Title"]), Spacer(1, 1*cm)]
    
    # Boucle d'écriture forcée pour remplir le document
    for titre, paragraphes in data:
        elements.append(Paragraph(f"<b>{titre}</b>", styles["Heading2"]))
        for p in paragraphes:
            p_clean = re.sub('<[^<]+?>', '', p)
            elements.append(Paragraph(p_clean, style_p))
            elements.append(Spacer(1, 6))
        elements.append(Spacer(1, 0.5*cm))
        
    doc.build(elements)
    buf.seek(0)
    return buf

# --- 4. ACCÈS CONCEPTEUR ---
st.markdown("<div class='trigger-secret'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code == "23111977":
    st.markdown("<div class='admin-bar'>🔓 ACCÈS CONCEPTEUR ACTIVÉ</div>", unsafe_allow_html=True)
    if st.session_state['pdf_binaire']:
        st.download_button("📥 TÉLÉCHARGER LE DOSSIER", st.session_state['pdf_binaire'], "Expertise_Solution_Pro.pdf")
    else:
        st.info("Lancez une analyse ci-dessous.")

# --- 5. INTERFACE ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
input_idee = st.text_input("Saisissez votre projet :", placeholder="ex: Agence immobilière...")

c1, c2 = st.columns(2)
with c1:
    if st.button("🚀 ANALYSE STANDARD (9€)"):
        if input_idee:
            res = moteur_expertise(input_idee, False)
            if res:
                st.session_state['pdf_binaire'] = generer_pdf(res, input_idee)
                st.session_state['nom_projet'] = input_idee
                st.rerun()

with c2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if input_idee:
            res = moteur_expertise(input_idee, True)
            if res:
                st.session_state['pdf_binaire'] = generer_pdf(res, input_idee)
                st.session_state['nom_projet'] = input_idee
                st.rerun()

if st.session_state['pdf_binaire']:
    st.success("✅ ANALYSE TERMINÉE : VOTRE DOSSIER EST PRÊT")
    st.markdown(f'<div class="prix-tag">9.00 €</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://buy.stripe.com/9" style="text-decoration:none;"><div style="background:#007bff;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;">ACCÉDER AU DOSSIER</div></a>', unsafe_allow_html=True)
