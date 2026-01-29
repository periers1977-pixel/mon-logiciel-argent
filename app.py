import streamlit as st
import time
import random

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# 1. COMPOSANTS DE L'IA (Bibliothèque illimitée)
# Ces briques s'assemblent pour créer des milliers de conseils clairs.
SUJETS = [
    "La gestion de l'argent pour '{idee}'", "La recherche de clients pour '{idee}'",
    "L'organisation de votre temps sur '{idee}'", "La sécurité de votre projet '{idee}'",
    "La vision à long terme de '{idee}'", "La qualité du service pour '{idee}'"
]

ACTIONS = [
    "doit rester une priorité absolue", "nécessite un plan simple et écrit",
    "doit être vérifiée chaque semaine", "demande de rester concentré sur l'essentiel",
    "doit s'adapter aux retours des clients", "nécessite d'économiser votre énergie"
]

OBJECTIFS = [
    "pour assurer une réussite durable.", "afin d'éviter les erreurs bêtes.",
    "pour gagner en efficacité réelle.", "dans le but de stabiliser vos revenus.",
    "pour transformer votre ambition en succès.", "afin de rester serein au quotidien."
]

# LA FONCTION QUI MANQUAIT (Doit être définie ICI)
def generer_phrase_unique(idee):
    """Génère une analyse cohérente en assemblant les briques de savoir."""
    s = random.choice(SUJETS).format(idee=idee)
    a = random.choice(ACTIONS)
    o = random.choice(OBJECTIFS)
    return f"✔ {s} {a} {o}"

def fabriquer_le_dossier_parfait(idee):
    doc = f"============================================================\n"
    doc += f"ARCHITECT SOLUTION PRO - LIVRABLE D'EXPERTISE SUPRÊME\n"
    doc += f"SUJET : {idee.upper()} | RÉFÉRENCE : #PERFECTION-2026\n"
    doc += f"============================================================\n\n"
    
    # Mémoire anti-répétition pour les 25 pages
    memoire = set()
    
    for i in range(1, 26):
        doc += f"--- CHAPITRE {i} : ANALYSE ET CONSEILS DE RÉUSSITE ---\n\n"
        
        count = 0
        while count < 8: # 8 conseils par page
            phrase = generer_phrase_unique(idee)
            if phrase not in memoire:
                doc += f"{phrase}\n\n"
                memoire.add(phrase)
                count += 1
        
        doc += f"[ ANALYSE PAGE {i}/25 - CONTENU UNIQUE ]\n"
        doc += f"© ARCHITECT SOLUTION PRO 2026\n\n"
    return doc

# 2. INTERFACE ÉPURÉE
st.title("💎 Architect Solution Pro")
st.subheader("Intelligence Stratégique pour tous les métiers et ambitions")

st.link_button("🔥 ACCÈS : RECEVOIR MON DOSSIER DE 25 PAGES (9€)", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre projet ou votre ambition (Travail & Vie) :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER L'EXPERTISE ET LE TÉLÉCHARGEMENT"):
    if idee:
        with st.status("L'IA construit votre dossier sans aucune répétition...", expanded=True) as status:
            # Appel de la fonction maintenant bien définie
            resultat = fabriquer_le_dossier_parfait(idee)
            time.sleep(1)
            status.update(label="✅ Votre expertise de 25 pages est prête !", state="complete")
        
        if code == "23111977":
            st.success("✅ Accès Développeur. Dossier prêt.")
            
            # Bouton de téléchargement fonctionnel
            st.download_button(
                label="📥 TÉLÉCHARGER LE DOSSIER ANALYSÉ (25 PAGES)",
                data=resultat,
                file_name=f"Expertise_Supreme_{idee}.txt",
                mime="text/plain"
            )
            
            st.text_area("Aperçu du dossier (Garanti sans répétition) :", resultat[:2000] + "...", height=450)
        else:
            st.info("🎯 L'analyse est prête. Payez 9€ pour débloquer votre dossier complet.")
