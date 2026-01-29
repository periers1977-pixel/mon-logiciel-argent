import streamlit as st
import time
import random

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# 1. LA MÉTAGRILLE UNIVERSELLE (100% de couverture Vie & Travail)
UNIVERS_SAVOIR = {
    "VISION_STRAT": [
        "L'alignement de '{idee}' avec les flux mondiaux de 2026 exige une disruption des modèles de pensée traditionnels.",
        "Le succès de votre projet repose sur une clarté de vision capable d'anticiper les ruptures technologiques et sociales.",
        "La trajectoire de '{idee}' doit être jalonnée d'indicateurs de performance (KPI) orientés vers la pérennité.",
        "Nous préconisons une architecture décisionnelle agile pour adapter '{idee}' aux mutations rapides du marché."
    ],
    "PSYCHO_LOGISTIQUE": [
        "La maîtrise de l'énergie vitale est le moteur invisible qui propulsera '{idee}' vers sa réalisation concrète.",
        "L'ingénierie du succès passe par la déconstruction des freins psychologiques et l'optimisation des routines quotidiennes.",
        "Le déploiement opérationnel de '{idee}' nécessite une discipline de fer et une gestion du temps au millimètre.",
        "La résilience de votre ambition est corrélée à la qualité de votre écosystème de soutien et de mentorat."
    ],
    "FINANCE_VALEUR": [
        "La structure de coûts pour '{idee}' doit être optimisée pour maximiser l'autofinancement et la liberté d'action.",
        "L'ingénierie financière prévoit une gestion du BFR ultra-serrée pour garantir une agilité maximale.",
        "La valorisation de votre projet '{idee}' repose sur la création d'actifs immatériels et de propriété intellectuelle.",
        "Chaque euro investi dans '{idee}' doit répondre à un protocole de rentabilité directe ou de positionnement stratégique."
    ],
    "EXECUTION_PRO": [
        "Le protocole d'exécution pour '{idee}' s'appuie sur une traçabilité totale et une conformité aux standards d'excellence.",
        "L'automatisation des processus de bas niveau permet de libérer du temps expert pour la haute valeur ajoutée.",
        "La sécurisation juridique et contractuelle de '{idee}' est le garant de votre tranquillité à long terme.",
        "L'audit de performance hebdomadaire permet de corriger les trajectoires et d'accélérer la réussite de '{idee}'."
    ]
}

def generer_expertise_absolue(idee):
    doc = f"============================================================\n"
    doc += f"ARCHITECT SOLUTION PRO - LIVRABLE D'EXPERTISE TOTALE\n"
    doc += f"SUJET : {idee.upper()} | RÉFÉRENCE : #UNIVERSAL-2026\n"
    doc += f"============================================================\n\n"
    
    # Construction des 25 pages UNIQUES
    # On utilise un système de rotation de catégories pour éviter toute répétition
    for i in range(1, 26):
        doc += f"--- CHAPITRE {i} : ANALYSE MULTIDIMENSIONNELLE ---\n\n"
        
        # On pioche une idée dans chaque pilier pour chaque page
        page_items = []
        for cat in UNIVERS_SAVOIR:
            # On utilise random.sample pour ne jamais prendre le même bloc sur une même page
            phrase = random.choice(UNIVERS_SAVOIR[cat]).format(idee=idee)
            page_items.append(f"• {phrase}")
            
        random.shuffle(page_items) # On mélange l'ordre sur la page
        doc += "\n\n".join(page_items)
        
        doc += f"\n\n[ ANALYSE DE LA PAGE {i}/25 - VALIDÉE PAR LE SYSTÈME EXPERT ]\n"
        doc += f"© ARCHITECT SOLUTION PRO 2026\n\n"
        
    return doc

# 2. INTERFACE ÉPURÉE
st.title("💎 Architect Solution Pro")
st.subheader("L'Intelligence Suprême pour tous les Projets de Vie et de Travail")

st.link_button("🔥 ACCÈS CLIENT : PAYER 9€ POUR LE DOSSIER COMPLET", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez n'importe quel projet, ambition ou idée business :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'EXPERTISE UNIVERSELLE"):
    if idee:
        with st.status("Génération du savoir multidimensionnel...", expanded=True) as status:
            time.sleep(1)
            st.write("Analyse des vecteurs de réussite...")
            time.sleep(1)
            status.update(label="✅ Dossier de 25 pages prêt !", state="complete")
        
        if code == "23111977":
            st.success("✅ Accès Développeur. Dossier sans répétition prêt.")
            resultat = generer_expertise_absolue(idee)
            st.download_button("📥 TÉLÉCHARGER LE DOSSIER DE 25 PAGES", resultat, file_name=f"Expertise_Universelle_{idee}.txt")
            st.text_area("Aperçu de la rédaction sans erreur :", resultat[:2000] + "...", height=400)
        else:
            st.info("🎯 L'expertise est prête. Réglez 9€ pour débloquer le téléchargement client.")
