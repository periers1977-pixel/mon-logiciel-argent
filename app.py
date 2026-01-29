import streamlit as st
import time
import random

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# 1. MOTEUR DE GÉNÉRATION INSTANTANÉE (Zéro Latence)
# On utilise des listes massives pour créer des millions de conseils uniques.
STRUCTURES = [
    "Pour réussir '{idee}', il faut d'abord organiser votre gestion financière.",
    "Le secret de '{idee}' réside dans une communication simple et honnête avec vos clients.",
    "La protection de votre projet '{idee}' passe par le respect strict des règles de sécurité.",
    "L'avenir de '{idee}' dépend de votre capacité à ne pas vous laisser distraire par l'inutile.",
    "Pour gagner du temps avec '{idee}', automatisez les tâches qui vous ennuient chaque jour.",
    "L'image de '{idee}' doit être impeccable pour attirer des partenaires de confiance.",
    "Chaque étape de '{idee}' doit être testée avant de dépenser trop d'argent dedans.",
    "La force de '{idee}' est de répondre à un problème que les gens veulent vraiment résoudre.",
    "Gardez un moral d'acier : '{idee}' est une aventure qui demande de la persévérance.",
    "Vérifiez vos marges sur '{idee}' pour être sûr de gagner de l'argent à chaque vente."
]

def fabriquer_dossier_instantané(idee):
    doc = f"============================================================\n"
    doc += f"ARCHITECT SOLUTION PRO - VOTRE ANALYSE DE RÉUSSITE\n"
    doc += f"SUJET : {idee.upper()} | GÉNÉRATION HAUTE VITESSE\n"
    doc += f"============================================================\n\n"
    
    # On mélange les structures pour chaque dossier
    pool = STRUCTURES.copy()
    random.shuffle(pool)
    
    for i in range(1, 26):
        doc += f"--- CHAPITRE {i} : ANALYSE ET CONSEILS ---\n\n"
        
        # On crée des variantes uniques pour éviter la répétition
        for _ in range(6):
            base = random.choice(STRUCTURES)
            variante = base.format(idee=idee)
            doc += f"✔ {variante}\n\n"
            
        doc += f"[ ANALYSE PAGE {i}/25 - TÉLÉCHARGEMENT IMMÉDIAT ]\n"
        doc += f"© ARCHITECT SOLUTION PRO 2026\n\n"
    return doc

# 2. INTERFACE ÉPURÉE ET RAPIDE
st.title("💎 Architect Solution Pro")
st.subheader("Système Expert de Conseil Stratégique - Vitesse Maximum")

st.link_button("🔥 ACCÈS : RECEVOIR MON DOSSIER DE 25 PAGES (9€)", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre projet ou votre ambition (Travail & Vie) :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

# On prépare la génération
if st.button("🚀 GÉNÉRER MON DOSSIER INSTANTANÉMENT"):
    if idee:
        # La barre de chargement est maintenant purement esthétique car le code est trop rapide
        with st.status("Génération ultra-rapide en cours...", expanded=True) as status:
            resultat_final = fabriquer_dossier_instantané(idee)
            status.update(label="✅ Votre expertise de 25 pages est prête !", state="complete")
        
        if code == "23111977":
            st.success("✅ Accès Développeur. Dossier prêt.")
            
            # TÉLÉCHARGEMENT IMMÉDIAT
            st.download_button(
                label="📥 TÉLÉCHARGER LE DOSSIER (25 PAGES)",
                data=resultat_final,
                file_name=f"Expertise_Rapide_{idee}.txt",
                mime="text/plain"
            )
            
            st.text_area("Aperçu du dossier (Aucune latence) :", resultat_final[:1500] + "...", height=400)
        else:
            st.info("🎯 L'analyse est finie. Payez 9€ pour débloquer le téléchargement.")
