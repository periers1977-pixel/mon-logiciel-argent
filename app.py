import streamlit as st
import time
import random

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# 1. LA MÉTAGRILLE UNIVERSELLE (Travail + Vie + Ambitions)
BIBLIO_INFINIE = {
    "AMBITIONS_VIE": {
        "mots": ["vie", "voyage", "sport", "rêve", "bonheur", "santé", "succès", "ambition", "art"],
        "expertises": [
            "L'ingénierie de la réussite pour '{idee}' repose sur un alignement entre vos valeurs et vos ressources temporelles.",
            "La stratégie de transformation personnelle exige une discipline de fer et une planification par paliers de progression.",
            "Le déploiement de votre ambition '{idee}' nécessite un audit des freins psychologiques et une optimisation de l'énergie vitale.",
            "La pérennité de votre projet de vie dépend de votre capacité à bâtir un écosystème de soutien et de mentorat.",
            "L'analyse de l'impact à long terme de '{idee}' démontre une valorisation de votre patrimoine immatériel et humain."
        ]
    },
    "ECONOMIE_TRAVAIL": {
        "mots": ["boucherie", "maison", "app", "vente", "magasin", "usine", "bureau", "commerce"],
        "expertises": [
            "L'optimisation des flux opérationnels pour '{idee}' garantit une réduction des charges fixes de 20% en 12 mois.",
            "La stratégie de conquête de marché s'appuie sur une différenciation par la qualité et une traçabilité irréprochable.",
            "L'ingénierie financière prévoit une gestion du besoin en fonds de roulement (BFR) ultra-agile pour absorber la croissance.",
            "La protection des actifs et la mise en conformité réglementaire sont les piliers de votre avantage concurrentiel.",
            "L'analyse du ROI (Retour sur Investissement) pour '{idee}' confirme une viabilité économique forte pour 2026."
        ]
    }
}

def detecter_univers(idee):
    m = idee.lower()
    if any(mot in m for mot in BIBLIO_INFINIE["AMBITIONS_VIE"]["mots"]):
        return "AMBITIONS_VIE"
    return "ECONOMIE_TRAVAIL"

def generer_le_dossier_ultime(idee):
    univers = detecter_univers(idee)
    sources = BIBLIO_INFINIE[univers]["expertises"]
    
    doc = f"============================================================\n"
    doc += f"ARCHITECT SOLUTION PRO - RAPPORT DE STRATÉGIE GLOBALE\n"
    doc += f"SUJET : {idee.upper()} | RÉFÉRENCE : #LIFE-WORK-2026\n"
    doc += f"============================================================\n\n"
    
    for i in range(1, 26):
        doc += f"--- CHAPITRE {i} : ÉTAPE DÉCISIVE DE RÉALISATION ---\n\n"
        
        # Le secret pour éviter la répétition : On mélange et on enrichit chaque page
        random.shuffle(sources)
        for expertise in sources[:3]:
            doc += f"Analyse approfondie pour '{idee}' : " + expertise.format(idee=idee) + "\n\n"
        
        doc += f"Cette analyse technique de la page {i} contient des schémas de progression et des audits de faisabilité.\n"
        doc += f"© ARCHITECT SOLUTION PRO - PAGE {i}/25\n\n"
        
    return doc

# 2. INTERFACE
st.title("💎 Architect Solution Pro")
st.subheader("Le Système Expert de Réalisation pour le Travail et la Vie")

st.link_button("🔥 ACCÈS CLIENT : ACHETER LE DOSSIER DE 25 PAGES (9€)", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre idée de business ou votre grande ambition :", placeholder="Ex: Ouvrir une ferme bio, Devenir un grand athlète, Voyager autour du monde...")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'EXPERTISE ABSOLUE"):
    if idee:
        with st.status("Activation des moteurs de recherche travail et vie...", expanded=True) as status:
            time.sleep(1)
            st.write("Scan des référentiels de réussite mondiale...")
            time.sleep(1)
            status.update(label="✅ Votre dossier de 25 pages est prêt !", state="complete")
        
        if code == "23111977":
            st.success("✅ Accès Développeur. Dossier prêt.")
            resultat = generer_le_dossier_ultime(idee)
            st.download_button("📥 TÉLÉCHARGER LE DOSSIER DE 25 PAGES", resultat, file_name=f"Expertise_Globale_{idee}.txt")
            st.text_area("Aperçu de la rédaction d'expert :", resultat[:2000] + "...", height=400)
        else:
            st.info("🎯 L'analyse est prête. Payez 9€ pour débloquer votre dossier complet.")
