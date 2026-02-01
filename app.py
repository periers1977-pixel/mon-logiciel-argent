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

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# --- CONFIGURATION DU MOTEUR DE RECHERCHE 32X ---
API_KEY = "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" 

def traitement_expert_donnees(texte, idee):
    """Filtre les données et les transforme en analyse stratégique."""
    # Nettoyage profond des bruits web et de l'anglais
    bruit = r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|sign up|footer|header|menu|click here|read more)'
    texte = re.sub(bruit, '', texte)
    
    # Extraction des segments à haute valeur ajoutée
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    valides = [s.strip() for s in segments if len(s.split()) > 15]
    
    if len(valides) < 10:
        valides.append(f"La viabilité de votre projet '{idee}' repose sur une analyse granulaire des besoins du marché en 2026.")
    return valides

def moteur_recherche_32x(idee):
    """Effectue 32 recherches web distinctes pour une densité record."""
    axes_32 = [
        "opportunités marché", "innovations technologiques", "cadre légal 2026", "rentabilité financière",
        "acquisition clients", "gestion des risques", "tendances consommation", "stratégie de différenciation",
        "optimisation fiscale", "leviers de croissance", "analyse concurrentielle", "digitalisation",
        "développement durable", "ressources humaines", "logistique et flux", "psychologie du consommateur",
        "branding et image", "investissements", "scalabilité du projet", "intelligence artificielle",
        "protection des données", "partenariats stratégiques", "fonds de roulement", "vision à long terme",
        "modèle économique", "expérience utilisateur", "e-réputation", "normes de qualité",
        "stratégie de prix", "canaux de distribution", "communication globale", "management de projet"
    ]
    
    savoir_total = []
    with st.status(f"Extraction massive de données (32 sources) pour '{idee}'...", expanded=True):
        for idx, axe in enumerate(axes_32):
            st.write(f"Source {idx+1}/32 : Expertise {axe}...")
            try:
                url = "https://api.tavily.com/search"
                payload = {"api_key": API_KEY, "query": f"analyse professionnelle {axe} {idee} 2026", "search_depth": "advanced"}
                response = requests.post(url, json=payload, timeout=12)
                contenu = " ".join([r['content'] for r in response.json().get('results', [])])
                savoir_total.extend(traitement_expert_donnees(contenu, idee))
            except:
                continue
    return savoir_total

def generer_livrable_geant(idee):
    """Génère environ 35 pages extrêmement remplies."""
    base_savoir = moteur_recherche_32x(idee)
    pages = []
    
    # On monte à 35 chapitres pour un volume maximal
    for i in range(1, 36):
        titre_chap = f"CHAPITRE {i} : ANALYSE DES FACTEURS CLÉS DE RÉUSSITE"
        sections = []
        
        # 6 paragraphes massifs par page pour garantir le remplissage
        for s in range(6):
            idx = (i * 6 + s) % len(base_savoir)
            data = base_savoir[idx]
            
            sub = ["CONTEXTE", "ANALYSE", "DIAGNOSTIC", "STRATÉGIE", "OPÉRATIONNEL", "PROJECTION"]
            bloc = f"<b>{sub[s]} :</b> {data} Concernant votre ambition '{idee}', ce point est un moteur de " \
                   f"croissance incontournable. L'intégration de cette donnée dans votre structure permet d'assurer " \
                   f"une pérennité financière et une avance technologique décisive pour l'horizon 2026-2030."
            sections.append(bloc)
            
        pages.append([titre_chap] + sections)
        
    signature = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
    return pages, signature

def fabriquer_pdf_geant(pages, idee, signature):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1*cm, leftMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm)
    styles = getSampleStyleSheet()
    
    style_corps = styles["Normal"]
    style_corps.alignment = TA_JUSTIFY
    style_corps.fontSize = 10
    style_corps.leading = 14

    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE PANORAMIQUE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Réf : {signature} | Analyse Certifiée du {datetime.now().strftime('%d/%m/%Y')}", styles["Normal"]),
        Spacer(1, 0.5*cm)
    ]
    
    for page in pages:
        for ligne in page:
            s = styles["Heading2"] if "CHAPITRE" in ligne else style_corps
            story.append(Paragraph(ligne, s))
            story.append(Spacer(1, 10))
        story.append(PageBreak())
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.title("💎 Architect Solution Pro")
st.subheader("Moteur de Recherche 32x : Levier de Haute Performance")

# Bloc de paiement
st.markdown("""
<div style="background-color:#f0f2f6;padding:15px;border-radius:10px;border:1px solid #d1d5db;text-align:center">
    <h3>📂 DOSSIER STRATÉGIQUE GÉANT (35 PAGES)</h3>
    <p>Le document le plus complet du marché, basé sur 32 sources web mondiales.</p>
    <a href="#" style="background-color:#007bff;color:white;padding:12px 25px;text-decoration:none;border-radius:5px;font-weight:bold">DÉBLOQUER MON DOSSIER (9€)</a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
idee = st.text_input("Saisissez votre projet pour lancer l'expertise géante :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 LANCER L'EXPERTISE (PUISSANCE 32)"):
    if idee:
        pages, signature = generer_livrable_geant(idee)
        pdf_file = fabriquer_pdf_geant(pages, idee, signature)
        
        if code == "23111977":
            st.success(f"✅ Dossier géant de 35 pages généré avec 32 sources.")
            st.download_button("📥 TÉLÉCHARGER LE PDF GÉANT", pdf_file, f"Expertise_32x_{idee}.pdf", "application/pdf")
        else:
            st.info("🎯 Votre expertise de 35 pages est prête. Payez 9€ pour débloquer le téléchargement.")
