import streamlit as st
import requests
import hashlib
import io
import re
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY

# --- 1. CONFIGURATION & SÉCURITÉ MÉMOIRE ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# Utilisation des secrets Streamlit pour l'API KEY (Recommandé) ou fallback
API_KEY = st.secrets.get("TAVILY_API_KEY", "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")

if 'pdf_binaire' not in st.session_state:
    st.session_state['pdf_binaire'] = None
if 'nom_projet' not in st.session_state:
    st.session_state['nom_projet'] = ""

# --- 2. DESIGN PROFESSIONNEL ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;} [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    .admin-bar {
        background-color: #1e1e1e; color: #00ff00; padding: 15px;
        border-radius: 10px; border: 2px solid #00ff00; margin-bottom: 20px;
        text-align: center; font-weight: bold;
    }
    .card-paiement {
        background: white; padding: 35px; border-radius: 15px;
        border: 2px solid #dee2e6; text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-top: 20px;
    }
    .prix-tag { font-size: 50px; font-weight: 900; color: #007bff; margin: 10px 0; }
    .stTextInput input { border: 2px solid #000 !important; color: black !important; }
    .stButton button { background: #007bff; color: white; font-weight: bold; height: 50px; border-radius: 8px; width: 100%; }
    .secret-trigger { position: fixed; bottom: 10px; left: 10px; width: 60px; opacity: 0.1; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIQUE MÉTIER & OPTIMISATION ---

@st.cache_data(show_spinner=False)
def moteur_expertise(idee, premium=False):
    """Moteur avec gestion d'erreurs et mise en cache des résultats."""
    # Sanitisation basique
    idee_clean = re.sub(r'[^\w\s-]', '', idee)
    axes = ["Marché", "Innovation", "Légal", "Finance", "Risques"]
    if premium: 
        axes += ["Scalabilité", "Concurrents", "Logistique", "Digital", "Vente"]
    
    resultats = []
    barre = st.progress(0)
    for i, axe in enumerate(axes):
        try:
            query = f"expertise stratégique {axe} {idee_clean} 2026 en français"
            response = requests.post(
                "https://api.tavily.com/search", 
                json={"api_key": API_KEY, "query": query, "search_depth": "advanced" if premium else "basic"},
                timeout=15
            )
            response.raise_for_status()
            r = response.json()
            textes = [res['content'] for res in r.get('results', []) if len(res['content']) > 120]
            if textes:
                resultats.append((axe.upper(), textes))
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur technique (axe {axe}). Veuillez réessayer.")
            continue
        barre.progress((i + 1) / len(axes))
    barre.empty()
    return resultats

def generer_pdf(data, projet):
    """Génération PDF modulaire et robuste."""
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    style_p = ParagraphStyle('Corps', fontName='Helvetica', fontSize=10, leading=14, alignment=TA_JUSTIFY)
    
    story = [Paragraph(f"<b>Architect Solution Pro : {projet.upper()}</b>", styles["Title"]), Spacer(1, 1*cm)]
    
    for titre, paragraphes in data:
        story.append(Paragraph(f"<b>{titre}</b>", styles["Heading2"]))
        for p in paragraphes:
            p_clean = re.sub('<[^<]+?>', '', p)  # Sanitisation HTML
            story.append(Paragraph(p_clean, style_p))
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 0.5*cm))
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- 4. ACCÈS CONCEPTEUR (SÉCURISÉ) ---
st.markdown("<div class='secret-trigger'>", unsafe_allow_html=True)
code = st.text_input("A", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code == "23111977":
    st.markdown("<div class='admin-bar'>🔓 ACCÈS CONCEPTEUR ACTIVÉ</div>", unsafe_allow_html=True)
    if st.session_state['pdf_binaire']:
        st.download_button("📥 TÉLÉCHARGER LE DOSSIER", st.session_state['pdf_binaire'], "Expertise_Solution_Pro.pdf")
    else:
        st.info("Lancez une analyse pour générer le document.")

# --- 5. INTERFACE UTILISATEUR ---
st.markdown("<h1 style='text-align: center;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
input_idee = st.text_input("Saisissez votre idée de projet :", placeholder="ex: Boutique de luxe, Agence immobilière...")

c1, c2 = st.columns(2)
with c1:
    if st.button("🚀 ANALYSE STANDARD (9€)"):
        if input_idee.strip():
            res = moteur_expertise(input_idee, False)
            if res:
                st.session_state['pdf_binaire'] = generer_pdf(res, input_idee)
                st.session_state['nom_projet'] = input_idee
                st.rerun()
        else:
            st.warning("Veuillez saisir une idée de projet.")

with c2:
    if st.button("👑 EXPERTISE BANCAIRE (29€)"):
        if input_idee.strip():
            res = moteur_expertise(input_idee, True)
            if res:
                st.session_state['pdf_binaire'] = generer_pdf(res, input_idee)
                st.session_state['nom_projet'] = input_idee
                st.rerun()
        else:
            st.warning("Veuillez saisir une idée de projet.")

# --- 6. AFFICHAGE RÉSULTAT ---
if st.session_state['pdf_binaire']:
    st.success("✅ ANALYSE TERMINÉE : VOTRE DOSSIER EST PRÊT")
    st.markdown(f"""
        <div class="card-paiement">
            <h3>PROJET : {st.session_state['nom_projet'].upper()}</h3>
            <p>Notre moteur a compilé les données stratégiques. Le rapport est prêt pour téléchargement.</p>
            <div class="prix-tag">9.00 €</div>
            <a href="https://buy.stripe.com/votre_lien" style="text-decoration:none;">
                <div style="background:#007bff; color:white; padding:18px; border-radius:10px; font-weight:bold;">
                    ACCÉDER AU DOSSIER COMPLET
                </div>
            </a>
        </div>
    """, unsafe_allow_html=True)
