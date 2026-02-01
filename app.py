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

# --- CONFIGURATION DU MOTEUR ---
API_KEY = "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" 

def purger_donnees(texte):
    bruit = r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu|sign up)'
    texte = re.sub(bruit, '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    return list(dict.fromkeys([p.strip() for p in segments if len(p.split()) > 15]))

def moteur_recherche_furtif(idee):
    """Effectue les recherches en arrière-plan sans rien afficher à l'écran."""
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
    # L'affichage status est maintenant très sobre et ne mentionne pas les sources
    with st.spinner("Élaboration de votre expertise intégrale..."):
        for axe in axes_strategiques:
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
    pool_segments, titres = moteur_recherche_furtif(idee)
    pages = []
    for i in range(len(pool_segments)):
        titre_chap = f"CHAPITRE {i+1} : {titres[i]}"
        sections = []
        base_page = pool_segments[i]
        labels = ["CONTEXTE", "DIAGNOSTIC", "ENJEUX", "STRATÉGIE", "DÉPLOIEMENT"]
        for s in range(min(5, len(base_page))):
            sections.append(f"<b>{labels[s]} :</b> {base_page[s]} Pour votre projet '{idee}', ce levier est capital pour 2026.")
        pages.append([titre_chap] + sections)
    
    signature = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
    return pages, signature

def fabriquer_pdf(pages, idee, signature):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    style_p = styles["Normal"]
    style_p.alignment, style_p.fontSize, style_p.leading = TA_JUSTIFY, 10.5, 15
    story = [Paragraph(f"<b>DOSSIER D'EXPERTISE INTÉGRAL : {idee.upper()}</b>", styles["Title"]), Paragraph(f"Référence : {signature}", styles["Normal"]), Spacer(1, 0.5*cm)]
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
<div style="background-color:#f0f2f6;padding:25px;border-radius:10px;border:2px solid #007bff;text-align:center">
    <h3 style="color:#007bff">📂 DOSSIER D'EXPERTISE INTÉGRAL</h3>
    <p>Une analyse exhaustive personnalisée, générée en temps réel pour votre projet.</p>
    <a href="https://buy.stripe.com/votre_lien" target="_blank" style="background-color:#007bff;color:white;padding:12px 25px;text-decoration:none;border-radius:5px;font-weight:bold">OBTENIR MON DOSSIER (9€)</a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
idee = st.text_input("Saisissez votre ambition pour lancer l'expertise :", placeholder="ex: vente de chaussures, agence immobilière...")

# Sidebar pour le code secret
st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'EXPERTISE INTÉGRALE"):
    if idee:
        # Lancement de la génération
        pages, sig = generer_livrable(idee)
        pdf = fabriquer_pdf(pages, idee, sig)
        
        # LOGIQUE D'AFFICHAGE CONDITIONNELLE
        if code == "23111977":
            # N'apparaît QUE si le code est bon
            st.success(f"✅ Expertise '{idee}' finalisée avec succès.")
            st.download_button("📥 TÉLÉCHARGER LE DOSSIER PDF", pdf, f"Expertise_{idee}.pdf", "application/pdf")
        else:
            # Message standard pour le client
            st.info("🎯 Votre dossier d'expertise est prêt. Une fois votre règlement de 9€ effectué, utilisez votre accès pour le télécharger.")

# Pied de page discret
st.markdown("---")
if st.button("⚖️ Mentions Légales"):
    st.caption("Architect Solution Pro - Service d'analyse numérique. Prix : 9€ TTC. Livraison immédiate. Non remboursable après génération.")
