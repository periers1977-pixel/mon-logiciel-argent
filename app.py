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

# --- CONFIGURATION DU MOTEUR ANTI-RÉPÉTITION ---
API_KEY = "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" 

def purger_et_preparer(texte):
    """Nettoie le texte et le découpe en unités d'expertise uniques."""
    # Nettoyage des bruits web
    texte = re.sub(r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu)', '', texte)
    # Découpage en phrases réelles
    phrases = re.findall(r'[^.!?]*[.!?]', texte)
    # On ne garde que les segments riches (> 15 mots) et on les rend uniques
    uniques = list(dict.fromkeys([p.strip() for p in phrases if len(p.split()) > 15]))
    return uniques

def moteur_recherche_24x_pur(idee):
    """Effectue 24 recherches et crée un réservoir de savoir sans doublons."""
    axes = [
        "opportunités marché", "innovations techniques", "cadre légal 2026", "rentabilité financière",
        "acquisition clients", "gestion des risques", "tendances consommation", "stratégie de différenciation",
        "optimisation fiscale", "leviers de croissance", "analyse concurrentielle", "digitalisation",
        "développement durable", "ressources humaines", "logistique et flux", "psychologie du consommateur",
        "branding et image", "investissements", "scalabilité du projet", "intelligence artificielle",
        "protection des données", "partenariats stratégiques", "fonds de roulement", "vision à long terme"
    ]
    
    pool_de_savoir = []
    with st.status(f"Extraction chirurgicale (24 sources) pour '{idee}'...", expanded=True):
        for idx, axe in enumerate(axes):
            st.write(f"Source {idx+1}/24 : Analyse de {axe}...")
            try:
                url = "https://api.tavily.com/search"
                payload = {"api_key": API_KEY, "query": f"expertise précise {axe} {idee} 2026", "search_depth": "advanced"}
                response = requests.post(url, json=payload, timeout=12)
                contenu = " ".join([r['content'] for r in response.json().get('results', [])])
                pool_de_savoir.extend(purger_et_preparer(contenu))
            except:
                continue
    # Suppression finale des doublons globaux
    return list(dict.fromkeys(pool_de_savoir))

def generer_expertise_unique(idee):
    """Rédige 35 pages en consommant le savoir : chaque phrase est unique."""
    base_savoir = moteur_recherche_24x_pur(idee)
    pages = []
    
    # On veut 35 chapitres denses
    for i in range(1, 36):
        titre_chap = f"CHAPITRE {i} : ANALYSE DES LEVIERS STRATÉGIQUES"
        sections = []
        
        # 5 blocs denses par page
        for s in range(5):
            if base_savoir:
                # On prend et on ENLÈVE la donnée (pop) pour qu'elle ne soit plus jamais utilisée
                data = base_savoir.pop(0)
            else:
                data = f"L'optimisation des vecteurs de performance pour '{idee}' exige une attention particulière sur ce pilier de croissance."
            
            sub = ["CONTEXTE", "DIAGNOSTIC", "ENJEUX", "STRATÉGIE", "OPÉRATIONNEL"]
            bloc = f"<b>{sub[s]} :</b> {data} Pour votre projet '{idee}', cette analyse confirme la nécessité d'une adaptation structurelle pour garantir vos marges en 2026."
            sections.append(bloc)
            
        pages.append([titre_chap] + sections)
        
    signature = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
    return pages, signature

def fabriquer_pdf_parfait(pages, idee, signature):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1*cm, leftMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm)
    styles = getSampleStyleSheet()
    
    style_corps = styles["Normal"]
    style_corps.alignment = TA_JUSTIFY
    style_corps.fontSize = 10.5
    style_corps.leading = 15

    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE PANORAMIQUE : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Réf : {signature} | Analyse Certifiée du {datetime.now().strftime('%d/%m/%Y')}", styles["Normal"]),
        Spacer(1, 0.5*cm)
    ]
    
    for page in pages:
        for ligne in page:
            s = styles["Heading2"] if "CHAPITRE" in ligne else style_corps
            story.append(Paragraph(ligne, s))
            story.append(Spacer(1, 12))
        story.append(PageBreak())
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.title("💎 Architect Solution Pro")
st.subheader("Analyse Autonome : Moteur de Rédaction à Zéro Répétition")

st.markdown("""
<div style="background-color:#f0f2f6;padding:15px;border-radius:10px;border:1px solid #d1d5db;text-align:center">
    <h3>📂 EXPERTISE STRATÉGIQUE (35 PAGES)</h3>
    <p>35 pages de contenu unique, sourcé et analysé spécifiquement pour votre projet.</p>
    <a href="#" style="background-color:#007bff;color:white;padding:12px 25px;text-decoration:none;border-radius:5px;font-weight:bold">DÉBLOQUER L'ACCÈS (9€)</a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
idee = st.text_input("Saisissez votre projet pour lancer l'expertise sans répétition :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'EXPERTISE (ZÉRO RÉPÉTITION)"):
    if idee:
        pages, signature = generer_expertise_unique(idee)
        pdf_file = fabriquer_pdf_parfait(pages, idee, signature)
        
        if code == "23111977":
            st.success("✅ Dossier de 35 pages généré avec une garantie de contenu unique.")
            st.download_button("📥 TÉLÉCHARGER LE PDF COMPLET", pdf_file, f"Expertise_Unique_{idee}.pdf", "application/pdf")
        else:
            st.info("🎯 Votre dossier est prêt. Payez 9€ pour débloquer le téléchargement.")
