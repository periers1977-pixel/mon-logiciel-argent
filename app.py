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

# --- MOTEUR DE RECHERCHE ET NETTOYAGE ---
API_KEY = "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" 

def purger_donnees(texte):
    bruit = r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu|sign up)'
    texte = re.sub(bruit, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return list(dict.fromkeys([p.strip() for p in segments if len(p.split()) > 15]))

def moteur_recherche_24x(idee):
    # Liste des 24 axes pour les recherches et les titres de chapitres
    axes_strategiques = [
        "Marché et Opportunités", "Innovation Technique", "Cadre Légal 2026", "Rentabilité Financière",
        "Acquisition Clients", "Gestion des Risques", "Tendances Consommation", "Différenciation",
        "Optimisation Fiscale", "Leviers de Croissance", "Analyse Concurrentielle", "Digitalisation",
        "Développement Durable", "Ressources Humaines", "Logistique et Flux", "Psychologie Client",
        "Branding et Image", "Investissements", "Scalabilité", "Intelligence Artificielle",
        "Protection des Données", "Partenariats", "Fonds de Roulement", "Vision Long Terme"
    ]
    
    pool = []
    titres_final = []
    with st.status(f"Analyse de '{idee}' par balayage de 24 sources...", expanded=True):
        for idx, axe in enumerate(axes_strategiques):
            st.write(f"Source {idx+1}/24 : {axe}...")
            try:
                url = "https://api.tavily.com/search"
                payload = {"api_key": API_KEY, "query": f"expertise stratégique {axe} {idee} 2026", "search_depth": "advanced"}
                response = requests.post(url, json=payload, timeout=12)
                data = response.json().get('results', [])
                texte_axe = " ".join([r['content'] for r in data])
                segments_propres = purger_donnees(texte_axe)
                if segments_propres:
                    pool.append(segments_propres)
                    titres_final.append(axe.upper())
            except: continue
    return pool, titres_final

def generer_livrable(idee):
    pool_segments, titres = moteur_recherche_24x(idee)
    pages = []
    
    for i in range(len(pool_segments)):
        titre_chap = f"CHAPITRE {i+1} : {titres[i]}"
        sections = []
        base_page = pool_segments[i]
        
        labels = ["CONTEXTE", "DIAGNOSTIC", "ENJEUX", "STRATÉGIE", "DÉPLOIEMENT"]
        for s in range(min(5, len(base_page))):
            data = base_page[s]
            sections.append(f"<b>{labels[s]} :</b> {data} Pour votre projet '{idee}', ce levier est capital pour 2026.")
            
        pages.append([titre_chap] + sections)
        
    signature = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
    return pages, signature

def fabriquer_pdf(pages, idee, signature):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    style_p = styles["Normal"]
    style_p.alignment, style_p.fontSize, style_p.leading = TA_JUSTIFY, 10.5, 15
    
    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE INTÉGRAL : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Référence : {signature} | {datetime.now().strftime('%d/%m/%Y')}", styles["Normal"]),
        Spacer(1, 0.5*cm)
    ]
    
    for page in pages:
        for ligne in page:
            story.append(Paragraph(ligne, styles["Heading2"] if "CHAPITRE" in ligne else style_p))
            story.append(Spacer(1, 12))
        story.append(PageBreak())
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.title("💎 Architect Solution Pro")
st.subheader("Cabinet de Conseil Stratégique Autonome")

st.markdown("""
<div style="background-color:#f0f2f6;padding:20px;border-radius:10px;border:2px solid #007bff;text-align:center">
    <h3 style="color:#007bff">📂 DOSSIER D'EXPERTISE INTÉGRAL</h3>
    <p>Analyse exhaustive, sans répétition, basée sur 24 sources web en temps réel.</p>
    <a href="https://buy.stripe.com/votre_lien" target="_blank" style="background-color:#007bff;color:white;padding:12px 25px;text-decoration:none;border-radius:5px;font-weight:bold">OBTENIR MON DOSSIER (9€)</a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
idee = st.text_input("Saisissez votre ambition pour lancer l'expertise :")

# Mentions Légales
if st.button("⚖️ Mentions Légales & CGV"):
    st.info("Directeur de publication : Architect Solution Pro. Hébergement : Streamlit Cloud. Prix : 9€ TTC. Livraison immédiate.")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'EXPERTISE INTÉGRALE"):
    if idee:
        pages, sig = generer_livrable(idee)
        pdf = fabriquer_pdf(pages, idee, sig)
        if code == "23111977":
            st.success(f"✅ Dossier '{idee}' généré avec succès.")
            st.download_button("📥 TÉLÉCHARGER LE PDF", pdf, f"Expertise_{idee}.pdf", "application/pdf")
        else:
            st.info("🎯 Analyse terminée. Payez 9€ pour débloquer le téléchargement.")
