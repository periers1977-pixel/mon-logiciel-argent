import streamlit as st
import requests
import hashlib
import io
import re
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY

# --- CONFIGURATION ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# --- DESIGN HAUTE VISIBILITÉ ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    
    .admin-box {
        background-color: #1e1e1e; color: #00ff00; padding: 20px;
        border-radius: 10px; border: 2px solid #00ff00; margin-bottom: 25px;
        text-align: center; font-weight: bold;
    }
    
    .success-alert {
        background-color: #28a745; color: white; padding: 20px;
        border-radius: 10px; text-align: center; font-weight: bold; margin: 20px 0;
    }

    .premium-card {
        background: white; padding: 40px; border-radius: 20px;
        border: 1px solid #dee2e6; text-align: center; margin-top: 10px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }

    .price-tag { font-size: 52px; font-weight: 900; color: #007bff; }
    .stTextInput > div > div > input { border: 2px solid #1e1e1e !important; }
    .stButton > button { background: #007bff; color: white; font-weight: bold; width: 100%; height: 50px; }
    .concepteur-key { position: fixed; bottom: 10px; left: 10px; width: 80px; opacity: 0.05; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR ---
API_KEY = "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"

def moteur_expertise(idee, premium=False):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Risques"]
    if premium: axes += ["Scalabilité", "Psychologie", "Concurrents", "Digital", "Vente"]
    
    pool, titres = [], []
    bar = st.progress(0)
    for i, axe in enumerate(axes):
        try:
            query = f"expertise stratégique {axe} {idee} 2026 en français"
            r = requests.post("https://api.tavily.com/search", json={"api_key": API_KEY, "query": query, "search_depth": "advanced" if premium else "basic"}).json()
            content = " ".join([res['content'] for res in r.get('results', [])])
            if len(content) > 100:
                pool.append(content); titres.append(axe.upper())
        except: continue
        bar.progress((i + 1) / len(axes))
    bar.empty()
    return pool, titres

def generer_pdf(data, idee, premium=False):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4)
    styles = getSampleStyleSheet()
    style_p = ParagraphStyle('Normal', fontSize=10, leading=12, alignment=TA_JUSTIFY)
    story = [Paragraph(f"<b>Architect Solution Pro : {idee.upper()}</b>", styles["Title"]), Spacer(1, 1*cm)]
    
    for section in data:
        story.append(Paragraph(f"<b>{section[0]}</b>", styles["Heading2"]))
        story.append(Paragraph(section[1], style_p))
        story.append(Spacer(1, 0.5*cm))
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- ZONE CONCEPTEUR ---
st.markdown("<div class='concepteur-key'>", unsafe_allow_html=True)
cle = st.text_input("Admin", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if cle == "23111977":
    st.markdown("<div class='admin-box'>🔓 ACCÈS CONCEPTEUR : TÉLÉCHARGEMENT LIBRE</div>", unsafe_allow_html=True)
    if 'pdf' in st.session_state:
        st.download_button("📥 TÉLÉCHARGER LE DOSSIER MAINTENANT", st.session_state['pdf'], "Dossier_Concepteur.pdf")
    else:
        st.warning("En attente d'une génération de document...")

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
idee = st.text_input("Saisissez votre projet :", placeholder="ex: Agence de voyage...")

c1, c2 = st.columns(2)
with c1:
    if st.button("🚀 ANALYSE (9€)"):
        if idee:
            p, t = moteur_expertise(idee, False)
            if p:
                st.session_state['pdf'] = generer_pdf(list(zip(t, p)), idee)
                st.session_state['ready'] = True
                st.balloons()

with c2:
    if st.button("👑 EXPERTISE (29€)"):
        if idee:
            p, t = moteur_expertise(idee, True)
            if p:
                st.session_state['pdf'] = generer_pdf(list(zip(t, p)), idee, True)
                st.session_state['ready'] = True
                st.balloons()

# --- AFFICHAGE RÉSULTAT ET PAIEMENT ---
if st.session_state.get('ready'):
    st.markdown("<div class='success-alert'>✅ ANALYSE TERMINÉE AVEC SUCCÈS ! VOTRE DOSSIER EST PRÊT.</div>", unsafe_allow_html=True)
    st.markdown(f'''
        <div class="premium-card">
            <div class="price-tag">PROJET : {idee.upper()}</div>
            <p>Cliquez ci-dessous pour payer et recevoir votre expertise complète par email.</p>
            <a href="https://buy.stripe.com/test" style="text-decoration:none;">
                <div style="background:#007bff;color:white;padding:15px;border-radius:10px;font-weight:bold;margin-top:20px;">
                    DÉBLOQUER MON DOSSIER
                </div>
            </a>
        </div>
    ''', unsafe_allow_html=True)
