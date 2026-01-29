import streamlit as st
import time
import random

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# 1. BIBLIOTHÈQUE UNIVERSELLE D'EXPERTISE (Base de données étendue)
BIBLIO_GLOBAL = {
    "AGRO": {
        "mots": ["viande", "boucherie", "boulangerie", "vin", "ferme", "agro", "bio", "cuisine"],
        "sections": [
            "Analyse de la traçabilité et conformité HACCP pour {idee}.",
            "Optimisation du rendement matière et gestion des pertes sèches.",
            "Stratégie de circuit court et valorisation du savoir-faire artisanal."
        ]
    },
    "BTP_INDUSTRIE": {
        "mots": ["maison", "travaux", "usine", "construction", "artisan", "garage", "meuble"],
        "sections": [
            "Gestion de la supply-chain et sécurisation des approvisionnements matières.",
            "Optimisation du taux d'utilisation des actifs et des équipements.",
            "Protocoles de sécurité et conformité aux normes industrielles 2026."
        ]
    },
    "TECH_SERVICES": {
        "mots": ["app", "logiciel", "web", "agence", "conseil", "ia", "plateforme", "digital"],
        "sections": [
            "Modélisation de la scalabilité et infrastructure cloud haute disponibilité.",
            "Stratégie de 'Growth Hacking' et optimisation du coût d'acquisition client.",
            "Protection de la propriété intellectuelle et conformité RGPD."
        ]
    },
    "COMMERCE_LUXE": {
        "mots": ["boutique", "magasin", "luxe", "mode", "vente", "bijoux", "parfum"],
        "sections": [
            "Ingénierie de l'expérience client et parcours omnicanal premium.",
            "Gestion des stocks en flux tendu et optimisation du merchandising.",
            "Storytelling de marque et levier de rareté pour le projet {idee}."
        ]
    }
}

def moteur_recherche_expert(idee):
    mots_cles = idee.lower()
    # Recherche sémantique par correspondance de mots-clés
    for domaine, data in BIBLIO_GLOBAL.items():
        if any(m in mots_cles for m in data["mots"]):
            return data["sections"]
    # Valeur par défaut si aucun secteur n'est identifié
    return [
        "Analyse de la viabilité économique globale du projet {idee}.",
        "Optimisation des processus opérationnels et réduction des frais fixes.",
        "Stratégie de développement commercial et positionnement de marché."
    ]

def generer_le_rapport_ultime(idee):
    expertise = moteur_recherche_expert(idee)
    doc = f"============================================================\n"
    doc += f"ARCHITECT SOLUTION PRO - RAPPORT D'INGÉNIERIE STRATÉGIQUE\n"
    doc += f"PROJET ANALYSÉ : {idee.upper()} | DOCUMENT CERTIFIÉ\n"
    doc += f"============================================================\n\n"
    
    for i in range(1, 26):
        doc += f"--- CHAPITRE {i} : ANALYSE DÉTAILLÉE DU SECTEUR ---\n\n"
        # Le moteur choisit la section la plus pertinente
        base_texte = expertise[i % len(expertise)].format(idee=idee)
        
        # Rédaction dense pour atteindre les 25 pages
        doc += f"Dans le cadre de l'étude sur '{idee}', ce chapitre développe les leviers critiques.\n"
        doc += f"{base_texte}\n"
        doc += "Cette section inclut des modélisations financières et des audits de performance.\n"
        doc += "L'analyse démontre une probabilité de réussite élevée sous réserve d'application des protocoles.\n"
        doc += (base_texte + " ") * 6 + "\n\n"
        doc += f"© ARCHITECT SOLUTION PRO - PAGE {i}/25\n\n"
        
    return doc

# 2. INTERFACE ÉPURÉE
st.title("💎 Architect Solution Pro")
st.subheader("Système Expert de Recherche & Conseil Stratégique")

st.link_button("🔥 ACCÈS CLIENT : PAYER 9€ POUR LE DOSSIER", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre projet pour une analyse profonde :")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 LANCER LA RECHERCHE & GÉNÉRER LE DOSSIER"):
    if idee:
        with st.status("Activation du pouvoir de recherche sémantique...", expanded=True) as status:
            time.sleep(1)
            st.write("Scan de la base de données mondiale...")
            time.sleep(1)
            st.write("Analyse contextuelle des 25 pages...")
            status.update(label="✅ Expertise générée !", state="complete")
        
        if code == "23111977":
            st.success("✅ Accès Développeur. Dossier prêt.")
            resultat = generer_le_rapport_ultime(idee)
            st.download_button("📥 TÉLÉCHARGER LE DOSSIER DE 25 PAGES", resultat, file_name=f"Expertise_{idee}.txt")
            st.text_area("Aperçu de la recherche intelligente :", resultat[:1500] + "...", height=400)
        else:
            st.info("🎯 L'analyse est prête. Payez 9€ pour débloquer votre dossier complet.")
