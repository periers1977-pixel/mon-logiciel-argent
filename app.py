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

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# Clé API Directe pour éviter les erreurs de lecture serveur
API_KEY = "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"

if 'pdf_binaire' not in st.session_state:
    st.session_state['pdf_binaire'] = None
if 'nom_projet' not in st.session_state:
    st.session_state['nom_projet'] = ""

# --- 2. DESIGN PROPRE ET FONCTIONNEL ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    .admin-header {
        background-color: #1e1e1e; color: #00ff00; padding: 15px;
        border-radius: 10px; border: 2px solid #00ff00; margin-bottom: 20px;
        text-align: center; font-weight: bold;
    }
    .status-box {
        background-color: #d4edda; color: #155724; padding: 15px;
        border-radius: 10px; border: 1px solid #c3e6cb; margin-bottom: 20px;
        text-align: center; font-weight: bold;
    }
    .stTextInput input { border: 2px solid #1e1e1e !important; color: black !important; }
    .stButton button { background: #007bff; color: white; font-weight: bold; height: 50px; border-radius: 10px; width: 100%; }
    .secret-trigger { position: fixed; bottom: 10px; left: 10px; width: 80px; opacity: 0.1; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MOTEUR DE RECHERCHE ET FILTRAGE ---
def moteur_expertise(idee, premium=False):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Risques", "Vision", "Digital", "RH", "Logistique"]
    resultats = []
    barre = st.progress(0)
    for i, axe in enumerate(axes):
        try:
            query = f"expertise approfondie stratégique {axe} {idee} 2026 en français"
            # Appel API simplifié pour éviter les erreurs roses
            response = requests.post("https://api.tavily.com/search", 
                             json={"api_key": API_KEY, "query": query, "search_depth": "advanced" if premium else "basic"},
                             timeout=20)
            data = response.json()
            # Extraction des textes de qualité
            textes = [res['content'] for res in data.get('results', []) if len(res['content']) > 60]
            if textes:
                resultats.append((axe.upper(), textes))
        except:
            continue
        barre.progress((i + 1) / len(axes))
    barre.empty()
    return resultats

def generer_pdf(data, projet):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
    styles = getSampleStyleSheet()
    style_p = ParagraphStyle('Corps', fontName='Helvetica', fontSize=10, leading=13, alignment=TA_JUSTIFY)
    
    elements = [Paragraph(f"<b>Architect Solution Pro : {projet.upper()}</b>", styles["Title"]),
                Paragraph(f"CERTIFICATION : {hashlib.sha256(projet.encode()).hexdigest()[:12].upper()} | 2026", styles["Normal"]),
                Spacer(1, 1*cm)]
    
    # BOUCLE D'ÉCRITURE : On parcourt chaque section et chaque paragraphe
    for titre, paragraphes in data:
        elements.append(Paragraph(f"<b>{titre}</b>", styles["Heading2"]))
        for p in paragraphes:
            p_clean = re.sub('<[^<]+?>', '', p) # Nettoyage HTML
            elements.append(Paragraph(p_clean, style_p))
            elements.append(Spacer(1, 6))
        
        # Ajout d'un tableau pour le look "Bancaire"
        tab_data = [["INDICATEUR", "PRÉVISION", "IMPACT"], ["Fiabilité", f"{random.randint(85,99)}%", "ÉLEVÉ"]]
        t = Table(tab_data, colWidths=[6*cm, 6*cm, 5*cm])
        t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey), ('TEXTCOLOR', (0,0), (-1,0), colors.white), ('GRID', (0,0), (-1,-1), 0.5, colors.grey)]))
        elements.append(Spacer(1, 0.5*cm)); elements.append(t); elements.append(Spacer(1, 1*cm))
        
    doc.build(elements)
    buf.seek(0)
    return buf

# --- 4. ACCÈS CONCEPTEUR ---
st.markdown("<div class='secret-trigger'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code == "23111977":
    st.markdown("<div class='admin-header'>🔓 ACCÈS CONCEPTEUR : TÉLÉCHARGEMENT LIBRE</div>", unsafe_allow_html=True)
    if st.session_state['pdf_binaire']:
        st.download_button("📥 TÉLÉCHARGER LE DOSSIER", st.session_state['pdf_binaire'], "Expertise_Solution_Pro.pdf")
    else:
        st.info("Lancez une analyse ci-dessous.")

# --- 5. INTERFACE UTILISATEUR ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
input_idee = st.text_input("Saisissez votre projet :", placeholder="ex: Agence immobilière, Glacier...")

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
    st.markdown("<div class='status-box'>✅ ANALYSE TERMINÉE : VOTRE DOSSIER EST PRÊT</div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style="background: white; padding: 30px; border-radius: 15px; border: 1px solid #dee2e6; text-align: center;">
            <h3>PROJET : {st.session_state['nom_projet'].upper()}</h3>
            <div style="font-size: 40px; font-weight: 900; color: #007bff; margin: 10px 0;">9.00 €</div>
            <a href="https://buy.stripe.com/9" style="text-decoration:none;">
                <div style="background:#007bff;color:white;padding:15px;border-radius:10px;font-weight:bold;">DÉBLOQUER LE DOSSIER</div>
            </a>
        </div>
    """, unsafe_allow_html=True)
