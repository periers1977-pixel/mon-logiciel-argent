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

# CSS : Interface Premium et masquage des menus natifs
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .main { background-color: #0e1117; }
    .payment-card {
        background: linear-gradient(135deg, #1c1f26 0%, #0e1117 100%);
        padding: 30px; border-radius: 20px; border: 1px solid #333; text-align: center;
    }
    .success-box {
        background-color: #0d2111;
        border: 1px solid #28a745;
        padding: 20px;
        border-radius: 10px;
        color: #d4edda;
        text-align: center;
        margin-top: 20px;
    }
    .admin-box { margin-top: 50px; padding: 10px; opacity: 0.2; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE MOTEUR ---
API_KEY = "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"

def purger_donnees(texte):
    bruit = r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu)'
    texte = re.sub(bruit, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return list(dict.fromkeys([p.strip() for p in segments if len(p.split()) > 12]))

def moteur_furtif(idee):
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    pool, titres = [], []
    with st.spinner("💎 Intelligence Artificielle : Analyse de votre projet en cours..."):
        for axe in axes:
            try:
                url = "https://api.tavily.com/search"
                payload = {"api_key": API_KEY, "query": f"expertise approfondie {axe} {idee} 2026", "search_depth": "advanced"}
                r = requests.post(url, json=payload, timeout=12).json()
                data = purger_donnees(" ".join([res['content'] for res in r.get('results', [])]))
                if data:
                    pool.append(data); titres.append(axe.upper())
            except: continue
    return pool, titres

def fabriquer_pdf_dense(pages, idee, sig):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    style_p = styles["Normal"]; style_p.alignment, style_p.fontSize, style_p.leading = TA_JUSTIFY, 9.5, 12
    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Référence : {sig} | Émis le {datetime.now().strftime('%d/%m/%Y')}", styles["Normal"]),
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

# Le client saisit son idée
idee = st.text_input("Saisissez votre projet pour lancer la création du dossier :", placeholder="ex: Agence de voyage éco-responsable...")

# Bouton visible pour le client (il déclenche la création mais pas le téléchargement sans code)
if st.button("🚀 CRÉER MON DOSSIER D'EXPERTISE"):
    if idee:
        pool, titres = moteur_furtif(idee)
        pages = []
        for i in range(len(pool)):
            pages.append([f"SECTION {i+1} : {titres[i]}"] + pool[i][:15])
        sig = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
        
        # ON AFFICHE QUE LE DOSSIER EST CRÉÉ
        st.markdown(f"""
            <div class="success-box">
                <h3>✅ ANALYSE TERMINÉE AVEC SUCCÈS</h3>
                <p>Votre dossier d'expertise intégral (Réf: <b>{sig}</b>) a été généré et archivé.</p>
                <p>Pour débloquer l'accès au document complet et le télécharger immédiatement, veuillez finaliser votre règlement.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # BLOC DE PAIEMENT APPARAÎT APRÈS GÉNÉRATION
        st.markdown(f"""
            <div class="payment-card" style="margin-top:20px;">
                <h2 style="color: #007bff !important;">DÉBLOQUER MON DOSSIER</h2>
                <p style="font-size: 24px; font-weight: bold; color: white;">9.00 €</p>
                <a href="https://buy.stripe.com/votre_lien" target="_blank" style="text-decoration: none;">
                    <div style="background: #007bff; color: white; padding: 15px; border-radius: 10px; font-weight: bold;">
                        PAYER ET TÉLÉCHARGER MAINTENANT
                    </div>
                </a>
                <p style="font-size: 0.7em; color: #666; margin-top: 10px;">🔒 Accès sécurisé SSL</p>
            </div>
            """, unsafe_allow_html=True)
        
        # STOCKAGE TEMPORAIRE POUR LE CONCEPTEUR
        st.session_state['current_pdf'] = fabriquer_pdf_dense(pages, idee, sig)
        st.session_state['current_idee'] = idee

# --- ZONE CONCEPTEUR DISCRÈTE (BAS DE PAGE) ---
st.markdown("<div class='admin-box'>", unsafe_allow_html=True)
code_admin = st.text_input("Accès Admin :", type="password")
st.markdown("</div>", unsafe_allow_html=True)

if code_admin == "23111977" and 'current_pdf' in st.session_state:
    st.success("Mode Concepteur : Téléchargement débloqué.")
    st.download_button("📥 TÉLÉCHARGER LE PDF (GRATUIT POUR VOUS)", st.session_state['current_pdf'], f"Expertise_{st.session_state['current_idee']}.pdf")
