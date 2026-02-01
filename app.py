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
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

# --- CONFIGURATION PAGE ---
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="centered")

# --- DESIGN IMMERSIF (CSS) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .main { background: radial-gradient(circle, #1a1c23 0%, #0e1117 100%); color: white; }
    .premium-card {
        background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px);
        padding: 40px; border-radius: 30px; border: 1px solid rgba(0, 198, 255, 0.2);
        text-align: center; box-shadow: 0 20px 50px rgba(0,0,0,0.5); margin: 20px 0;
    }
    .stButton > button {
        background: linear-gradient(45deg, #007bff, #00c6ff); color: white;
        border: none; padding: 12px 24px; border-radius: 12px; font-weight: bold;
    }
    .admin-footer { position: fixed; bottom: 5px; left: 5px; width: 120px; opacity: 0.05; transition: 0.3s; }
    .admin-footer:hover { opacity: 1; }
    </style>
    """, unsafe_allow_html=True)

# --- MOTEURS DE PRÉCISION ---
API_KEY = "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"

def filtrage_strict(texte):
    """Exclut les biographies et les publicités d'entreprises."""
    # Liste noire de termes liés aux bios et pubs
    blacklist = r'(?i)(Dhruv|Bhatia|analyst|Research Nester|Research Dive|Pune|India|consultant|biography|about us|contact us|Research LLC)'
    texte = re.sub(r'(?i)(cookie|consent|policy|analytics|http|www|subscribe|transcript|login|footer|menu)', '', texte)
    segments = re.findall(r'[^.!?]*[.!?]', texte)
    # On garde les segments longs et sans termes de la blacklist
    return [s.strip() for s in segments if len(s.split()) > 15 and not re.search(blacklist, s)]

def moteur_expertise_progression(idee):
    """Génération avec barre de progression immersive."""
    axes = ["Marché", "Innovation", "Légal", "Finance", "Acquisition", "Risques", "Vision", "Digital", "RH", "Logistique"]
    steps = ["Connexion aux flux de données mondiaux...", "Analyse sectorielle systémique...", "Calcul des indicateurs de performance...", "Sécurisation du protocole de sortie..."]
    
    pool, titres = [], []
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i, axe in enumerate(axes):
        # Mise à jour de l'immersion
        step_idx = int((i / len(axes)) * len(steps))
        status_text.markdown(f"**💎 {steps[step_idx]}**")
        progress_bar.progress((i + 1) / len(axes))
        
        try:
            url = "https://api.tavily.com/search"
            payload = {"api_key": API_KEY, "query": f"expertise approfondie {axe} {idee} 2026", "search_depth": "advanced"}
            r = requests.post(url, json=payload, timeout=12).json()
            data = filtrage_strict(" ".join([res['content'] for res in r.get('results', [])]))
            if data:
                pool.append(data); titres.append(axe.upper())
        except: continue
    
    status_text.empty()
    progress_bar.empty()
    return pool, titres

def fabriquer_pdf_imperial(pages, idee, sig):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=1.2*cm, leftMargin=1.2*cm, topMargin=1.2*cm, bottomMargin=1.2*cm)
    styles = getSampleStyleSheet()
    
    # Styles personnalisés
    style_p = ParagraphStyle('Custom', parent=styles['Normal'], fontSize=9.5, leading=13, alignment=TA_JUSTIFY)
    style_liaison = ParagraphStyle('Liaison', parent=style_p, textColor=colors.HexColor("#007bff"), fontName="Helvetica-BoldOblique")
    
    story = [
        Paragraph(f"<b>DOSSIER D'EXPERTISE INTÉGRAL : {idee.upper()}</b>", styles["Title"]),
        Paragraph(f"Signature d'Authenticité : {sig} | ARCHITECT SOLUTION PRO", styles["Normal"]),
        Spacer(1, 0.5*cm)
    ]
    
    liaisons = [
        "En regard de votre ambition pour '{idee}', les indicateurs suivants confirment une opportunité majeure.",
        "L'intégration de '{idee}' dans ce contexte exige une maîtrise des flux de données suivants :",
        "Pour garantir la pérennité de votre projet '{idee}', l'analyse systémique révèle les points clés suivants :"
    ]

    for i, page in enumerate(pages):
        story.append(Paragraph(f"<b>{page[0]}</b>", styles["Heading2"]))
        
        # Phrase de liaison personnalisée
        story.append(Paragraph(random.choice(liaisons).format(idee=idee), style_liaison))
        story.append(Spacer(1, 6))
        
        # Contenu dense
        for ligne in page[1:]:
            story.append(Paragraph(ligne, style_p))
            story.append(Spacer(1, 6))
            
        # Ajout d'un tableau récapitulatif simulé (Indicateurs)
        data_tab = [
            ["INDICATEUR CLÉ", "VALEUR PRÉVISIONNELLE 2026", "NIVEAU D'IMPACT"],
            ["Potentiel de Croissance", f"{random.randint(4, 12)}%", "ÉLEVÉ"],
            ["Indice de Risque", f"{random.randint(1, 4)}/10", "MAÎTRISÉ"]
        ]
        t = Table(data_tab, colWidths=[6*cm, 7*cm, 5*cm])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1c1f26")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey)
        ]))
        story.append(Spacer(1, 0.4*cm))
        story.append(t)
        story.append(Spacer(1, 0.8*cm))
        
    doc.build(story)
    buf.seek(0)
    return buf

# --- INTERFACE ---
st.markdown("<h1 style='text-align: center; color: white;'>💎 Architect Solution Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00c6ff;'>Expertise Systémique & Algorithmes de Précision</p>", unsafe_allow_html=True)

idee = st.text_input("Définissez votre projet pour l'analyse :", placeholder="ex: Boutique éco-conçue, Logiciel SaaS...")

if st.button("🚀 GÉNÉRER L'EXPERTISE INTÉGRALE"):
    if idee:
        pool, titres = moteur_expertise_progression(idee)
        pages_data = []
        for i in range(len(pool)):
            pages_data.append([f"SECTION {i+1} : {titres[i]}"] + pool[i][:12])
        
        sig = hashlib.sha256(str(pages_data).encode()).hexdigest()[:12].upper()
        
        st.markdown(f"""
            <div class="premium-card">
                <div style="background:#28a745; color:white; padding:5px 15px; border-radius:50px; display:inline-block; font-size:0.8em; font-weight:bold; margin-bottom:15px;">DOSSIER ARCHIVÉ</div>
                <h3 style="color:white; margin:0;">Expertise Réf: {sig}</h3>
                <p style="color:#888;">Le dossier complet a été compilé avec succès.</p>
                <div style="margin:20px 0; border-top:1px solid #333;"></div>
                <p style="font-size:32px; font-weight:bold; color:white;">9.00 €</p>
                <a href="https://buy.stripe.com/votre_lien" target="_blank" style="text-decoration:none;">
                    <div style="background:linear-gradient(45deg, #007bff, #00c6ff); color:white; padding:18px; border-radius:12px; font-weight:bold; font-size:1.1em; box-shadow:0 10px 20px rgba(0,123,255,0.3);">
                        ACCÉDER AU DOSSIER COMPLET
                    </div>
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        st.session_state['pdf'] = fabriquer_pdf_imperial(pages_data, idee, sig)
        st.session_state['idee'] = idee

# Zone Admin Discrète
st.markdown("<div class='admin-footer'>", unsafe_allow_html=True)
code = st.text_input("Admin", type="password", label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

if code == "23111977" and 'pdf' in st.session_state:
    st.download_button("📥 TÉLÉCHARGER (ADMIN)", st.session_state['pdf'], f"Expertise_Elite_{st.session_state['idee']}.pdf")
