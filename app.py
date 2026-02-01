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

# --- DESIGN IMMERSIF HAUTE LISIBILITÉ (CSS) ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    
    /* Fond Dynamique avec contraste amélioré */
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stApp {
        background: linear-gradient(-45deg, #0a0c10, #14181f, #1b2735, #0a0c10);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    /* Texte principal ultra-blanc */
    h1, h2, h3, p, label {
        color: #FFFFFF !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }

    /* Cartes plus lisibles */
    .premium-card {
        background: rgba(255, 255, 255, 0.08); /* Plus d'opacité */
        backdrop-filter: blur(20px);
        padding: 40px;
        border-radius: 30px;
        border: 2px solid rgba(0, 198, 255, 0.4); /* Bordure plus marquée */
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    .price-tag { 
        font-size: 54px; 
        font-weight: 900; 
        color: #00f2ff; /* Bleu plus clair/flashy */
        margin: 10px 0; 
    }
    
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #00c6ff !important;
    }

    .admin-footer { position: fixed; bottom: 5px; left: 5px; width: 100px; opacity: 0.05; transition: 0.3s; }
    .admin-footer:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEUR & FILTRAGE ---
API_KEY = "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"

def filtrage_strict(texte):
    blacklist = r'(?i)(Dhruv|Bhatia|analyst|Research Nester|Research Dive|Pune|India|consultant|biography|about us|contact us|Research LLC)'
    residus = r'(?i)(Getty Images|AFP|PHOTO|Twitter|Instagram|reCAPTCHA|Turnstile|ebook|click here)'
    texte = re.sub(r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|login|footer)', '', texte)
    texte = re.sub(residus, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return [s.strip() for s in segments if len(s.split()) > 15 and not re.search(blacklist, s)]

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00f2ff !important; font-size: 1.2em;'>Expertise Systémique & Algorithmes Mondiaux</p>", unsafe_allow_html=True)

idee = st.text_input("Définissez votre ambition business :", placeholder="ex: Agence de voyage de luxe...")

col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 ANALYSE STANDARD (9€)"):
        if idee:
            # Simulation rapide pour la démo, gardez votre moteur complet ici
            st.markdown(f'''
                <div class="premium-card">
                    <div style="color:#00f2ff; font-weight:bold;">DOSSIER GÉNÉRÉ</div>
                    <div class="price-tag">9€</div>
                    <p style="font-size:1.1em;">Accès immédiat à l'étude stratégique.</p>
                    <a href="https://stripe.com/9" style="text-decoration:none;">
                        <div style="background:#007bff; color:white; padding:15px; border-radius:10px; font-weight:bold;">DÉBLOQUER MAINTENANT</div>
                    </a>
                </div>
            ''', unsafe_allow_html=True)

with col2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if idee:
            st.markdown(f'''
                <div class="premium-card" style="border-color:#ffd700;">
                    <div style="color:#ffd700; font-weight:bold;">CERTIFICATION PREMIUM</div>
                    <div class="price-tag" style="color:#ffd700;">29€</div>
                    <p style="font-size:1.1em;">Audit complet 50 sources + Tableaux bancaires.</p>
                    <a href="https://stripe.com/29" style="text-decoration:none;">
                        <div style="background:#ffd700; color:black; padding:15px; border-radius:10px; font-weight:bold;">DÉBLOQUER L'EXPERTISE</div>
                    </a>
                </div>
            ''', unsafe_allow_html=True)

# Admin
st.markdown("<div class='admin-footer'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)
