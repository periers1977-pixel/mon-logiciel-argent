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

# --- STYLE CLARTÉ MAXIMALE (CSS) ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    
    /* Fond gris clair pour détacher les éléments */
    .stApp { 
        background-color: #f8f9fa; 
        color: #212529;
    }

    /* Cartes blanches avec bordures nettes */
    .premium-card {
        background: #ffffff;
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #dee2e6;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Titres et textes sombres */
    h1, h3, p, label { color: #212529 !important; font-family: 'Helvetica', sans-serif; }
    
    .price-tag { 
        font-size: 48px; 
        font-weight: bold; 
        color: #007bff; 
        margin: 10px 0; 
    }

    /* Barres de saisie très visibles */
    .stTextInput > div > div > input {
        background-color: #ffffff !important;
        color: #212529 !important;
        border: 2px solid #ced4da !important;
    }

    .stButton > button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 15px;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
    }

    /* Admin en bas à gauche */
    .admin-footer { position: fixed; bottom: 10px; left: 10px; width: 100px; opacity: 0.2; }
    .admin-footer:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR DE RECHERCHE ---
API_KEY = "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"

def filtrage_final(texte):
    blacklist = r'(?i)(Dhruv|Bhatia|analyst|Research Nester|Research Dive|Pune|India|consultant|biography|Getty|AFP|Twitter|Instagram)'
    texte = re.sub(r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|login|footer)', '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return [s.strip() for s in segments if len(s.split()) > 15 and not re.search(blacklist, s)]

def moteur_expertise(idee, mode_premium=False, lang_suffix="en français"):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    if mode_premium:
        axes += ["Scalabilité", "Psychologie", "Concurrents", "Supply Chain", "Export", "Fiscale", "Géo-politique", "Automatisation", "Branding", "Vente"]
    
    pool, titres = [], []
    progress_bar = st.progress(0)
    for i, axe in enumerate(axes):
        query = f"expertise stratégique {axe} {idee} 2026 {lang_suffix}"
        depth = "advanced" if mode_premium else "basic"
        try:
            url = "https://api.tavily.com/search"
            payload = {"api_key": API_KEY, "query": query, "search_depth": depth}
            r = requests.post(url, json=payload, timeout=25).json()
            data = filtrage_final(" ".join([res['content'] for res in r.get('results', [])]))
            if data: pool.append(data); titres.append(axe.upper())
        except: continue
        progress_bar.progress((i + 1) / len(axes))
    progress_bar.empty()
    return pool, titres

# --- INTERFACE ---
lang = st.selectbox("🌐 Language", ["Français", "English"])
suffix = "en français" if lang == "Français" else "in english"

st.markdown(f"<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
idee = st.text_input("Saisissez votre projet :", placeholder="ex: Agence immobilière...")

col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 ANALYSE (9€)"):
        if idee:
            p, t = moteur_expertise(idee, False, suffix)
            st.markdown(f'<div class="premium-card"><div class="price-tag">9€</div><p>Rapport Standard Prêt</p><a href="https://stripe.com/9" style="text-decoration:none;"><div style="background:#007bff;color:white;padding:15px;border-radius:10px;font-weight:bold;">DÉBLOQUER</div></a></div>', unsafe_allow_html=True)

with col2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if idee:
            p, t = moteur_expertise(idee, True, suffix)
            st.markdown(f'<div class="premium-card" style="border-color:#ffd700;"><div class="price-tag" style="color:#ffd700;">29€</div><p>Expertise Bancaire Prête</p><a href="https://stripe.com/29" style="text-decoration:none;"><div style="background:#ffd700;color:black;padding:15px;border-radius:10px;font-weight:bold;">DÉBLOQUER PREMIUM</div></a></div>', unsafe_allow_html=True)

# Admin discret
st.markdown("<div class='admin-footer'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)
