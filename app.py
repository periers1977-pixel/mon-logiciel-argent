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

# --- 1. INITIALISATION ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# Clé API - Version directe sans détour
API_KEY = "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"

# Mémoire de session pour ne pas perdre le document
if 'pdf_binaire' not in st.session_state:
    st.session_state['pdf_binaire'] = None
if 'projet_nom' not in st.session_state:
    st.session_state['projet_nom'] = ""

# --- 2. STYLE VISUEL (PRO ET CLAIR) ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    .admin-bar {
        background-color: #1e1e1e; color: #00ff00; padding: 15px;
        border-radius: 10px; border: 2px solid #00ff00; margin-bottom: 20px;
        text-align: center; font-weight: bold;
    }
    .stTextInput input { border: 2px solid #1e1e1e !important; color: black !important; }
    .stButton button { background: #007bff; color: white; font-weight: bold; height: 50px; border-radius: 10px; width: 100%; }
    .trigger-admin { position: fixed; bottom: 10px; left: 10px; width: 60px; opacity: 0.1; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LE MOTEUR D'ORIGINE ---
def moteur_expertise(idee, premium=False):
    # Les axes d'origine qui fonctionnaient
    axes = ["Marché", "Innovation", "Légal", "Finance", "Risques"]
    if premium: 
        axes += ["Scalabilité", "Concurrents", "Logistique", "Digital", "Vente"]
    
    resultats = []
    barre = st.progress(0)
    for i, axe in enumerate(axes):
        try:
            query = f"expertise stratégique {axe} {idee} 2026 en français"
            r = requests.post("https://api.tavily.com/search", 
                             json={"api_key": API_KEY, "query": query, "search_depth": "advanced" if premium else "basic"},
                             timeout=25).json()
            
            # Extraction directe du contenu (Minimum 60 caractères pour éviter le vide)
            textes = [res['content'] for res in r.get('results', []) if len(res['content']) > 60]
            if textes:
                resultats.append((axe.upper(), textes))
        except:
            continue
        barre.progress((i + 1) / len(axes))
    barre.empty()
    return resultats

# --- 4. LA GÉNÉRATION PDF (LIGNE PAR LIGNE) ---
def generer_pdf(data, projet):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    style_p = ParagraphStyle('Corps', fontName='Helvetica', fontSize=10, leading=14, alignment=TA_JUSTIFY)
    
    story = [Paragraph(f"<b>Architect Solution Pro : {projet.upper()}</b>", styles["Title"]), 
             Paragraph(f"CERTIFICATION : {hashlib.sha256(projet.encode()).hexdigest()[:12].upper()} | 2026", styles["Normal"]),
             Spacer(1, 1*cm)]
    
    # Écriture forcée : on s'assure que chaque donnée récupérée entre dans le PDF
    for titre, paragraphes in data:
        story.append(Paragraph(f"<b>{titre}</b>", styles["Heading2"]))
        for p in paragraphes:
            p_clean = re.sub('<[^<]+?>', '', p) # Nettoyeur HTML simple
            story.append(Paragraph(p_clean, style_p))
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 0.5*cm))
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- 5. ACCÈS CONCEPTEUR ---
st.markdown("<div class='trigger-admin'>", unsafe_allow_html=True)
code_secret = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code_secret == "23111977":
    st.markdown("<div class='admin-bar'>🔓 ACCÈS CONCEPTEUR : TÉLÉCHARGEMENT DIRECT</div>", unsafe_allow_html=True)
    if st.session_state['pdf_binaire']:
        st.download_button("📥 TÉLÉCHARGER LE DOSSIER", st.session_state['pdf_binaire'], "Expertise_Solution_Pro.pdf")
    else:
        st.info("Lancez une analyse ci-dessous.")

# --- 6. INTERFACE UTILISATEUR ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
input_idee = st.text_input("Saisissez votre idée de business :", placeholder="ex: Agence immobilière, Site e-commerce...")

c1, c2 = st.columns(2)
with c1:
    if st.button("🚀 ANALYSE STANDARD (9€)"):
        if input_idee:
            res = moteur_expertise(input_idee, False)
            if res:
                st.session_state['pdf_binaire'] = generer_pdf(res, input_idee)
                st.session_state['projet_nom'] = input_idee
                st.rerun()

with c2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if input_idee:
            res = moteur_expertise(input_idee, True)
            if res:
                st.session_state['pdf_binaire'] = generer_pdf(res, input_idee)
                st.session_state['projet_nom'] = input_idee
                st.rerun()

# --- 7. AFFICHAGE RÉSULTAT ---
if st.session_state['pdf_binaire']:
    st.success("✅ ANALYSE TERMINÉE : VOTRE DOSSIER EST PRÊT")
    st.markdown(f"""
        <div style="background: white; padding: 30px; border-radius: 15px; border: 1px solid #dee2e6; text-align: center;">
            <h3>PROJET : {st.session_state['projet_nom'].upper()}</h3>
            <div style="font-size: 40px; font-weight: 900; color: #007bff; margin: 10px 0;">9.00 €</div>
            <a href="https://buy.stripe.com/9" style="text-decoration:none;">
                <div style="background:#007bff;color:white;padding:15px;border-radius:10px;font-weight:bold;">DÉBLOQUER LE DOSSIER</div>
            </a>
        </div>
    """, unsafe_allow_html=True)
