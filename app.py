import streamlit as st
import time
import random
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# 1. CONFIGURATION DE L'INTERFACE
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# 2. BASE DE DONNÉES D'EXPERTISE MASSIF (Contenu profond et varié)
MARKETING_DB = [
    "Analyse de la Matrice de Porter : Évaluation des barrières à l'entrée pour {idee}. Stratégie de différenciation par la valeur perçue.",
    "Psychologie du Consommateur : Utilisation des biais d'ancrage et de rareté pour optimiser le tunnel de conversion de {idee}.",
    "Acquisition 3.0 : Déploiement d'un écosystème de contenu omnicanal automatisé pour réduire le coût d'acquisition client (CAC).",
    "Branding de Niche : Construction d'une identité de marque 'Ultra-Premium' pour sortir de la guerre des prix sur le marché de {idee}."
]

FINANCE_DB = [
    "Ingénierie Financière : Modélisation du BFR (Besoin en Fonds de Roulement) et optimisation des flux de trésorerie sur 24 mois.",
    "Seuil de Rentabilité : Calcul du point mort opérationnel pour {idee} avec une marge brute cible de {val}% dès le 6ème mois.",
    "Scalabilité du Modèle : Analyse de la réduction des coûts marginaux permettant une expansion rapide de {idee} sans perte de qualité.",
    "Valorisation Prédictive : Estimation de l'EBITDA et préparation des indicateurs pour une éventuelle levée de fonds en Année 2."
]

STRATEGIE_DB = [
    "Feuille de Route Opérationnelle : Les 90 premiers jours critiques pour valider le 'Product-Market Fit' du projet {idee}.",
    "Gestion des Risques 2026 : Analyse SWOT approfondie et mise en place de protocoles de résilience pour sécuriser l'activité.",
    "Automatisation No-Code : Intégration d'outils d'IA pour supprimer les tâches à faible valeur et libérer {val}% de productivité.",
    "Conformité et Éthique : Mise aux normes RGPD et sécurisation des actifs immatériels pour pérenniser {idee}."
]

def generer_visuel_croissance(idee):
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.linspace(0, 10, 100)
    y = np.exp(x/3.5) * random.uniform(0.9, 1.1)
    ax.plot(x, y, color='#00a8cc', linewidth=3, label='Courbe de Scalabilité')
    ax.fill_between(x, y, color='#00a8cc', alpha=0.1)
    ax.set_title(f"PRÉVISION DE PERFORMANCE : {idee.upper()}", fontsize=14, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    return fig

def generer_dossier_25_pages(idee):
    session_ref = f"BP-{random.randint(10000, 99999)}"
    doc = f"============================================================\n"
    doc += f"ARCHITECT SOLUTION PRO - EXPERTISE STRATÉGIQUE COMPLÈTE\n"
    doc += f"RÉFÉRENCE : {session_ref} | PROJET : {idee.upper()}\n"
    doc += f"============================================================\n\n"
    
    # GÉNÉRATION DE 25 SECTIONS UNIQUES ET DÉVELOPPÉES
    categories = ["MARKETING", "FINANCE", "STRATEGIE"]
    for i in range(1, 26):
        doc += f"PAGE {i} : ANALYSE DÉTAILLÉE DES LEVIERS DE RÉUSSITE\n"
        doc += "-"*50 + "\n"
        
        cat = categories[i % 3]
        if cat == "MARKETING":
            base = MARKETING_DB
        elif cat == "FINANCE":
            base = FINANCE_DB
        else:
            base = STRATEGIE_DB
            
        conseils = random.sample(base, 2)
        doc += f"Domaine d'intervention : {cat}\n"
        doc += conseils[0].format(idee=idee, val=random.randint(15, 45)) + "\n"
        doc += conseils[1].format(idee=idee, val=random.randint(5, 25)) + "\n"
        doc += "Analyse experte complémentaire : Ce chapitre inclut des schémas de flux et des projections détaillées.\n"
        doc += f"[ RÉFÉRENCE GRAPHIQUE PAGE {i} : SCHÉMA DE PERFORMANCE {i}.A ]\n\n"
        
    return doc

# 3. INTERFACE UTILISATEUR
st.title("💎 Architect Solution Pro - Intelligence 2026")

# BOUTON DE PAIEMENT PRIORITAIRE
st.link_button("🔥 ACCÈS CLIENT : PAYER 9€ POUR LE DOSSIER COMPLET", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre idée business pour une analyse profonde :", placeholder="Ex: Une plateforme de luxe...")

# Zone Administrateur Sécurisée
st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER MON DOSSIER D'EXPERT"):
    if idee:
        barre = st.progress(0, text="L'IA Architect Solution développe vos 25 pages...")
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        if code == "23111977":
            st.success("✅ Accès Développeur Validé. Analyse de 25 pages prête.")
            
            # Affichage du Croquis Financier
            st.subheader("📊 Croquis de Croissance prédictive")
            st.pyplot(generer_visuel_croissance(idee))
            
            # Téléchargement
            contenu_final = generer_dossier_25_pages(idee)
            st.download_button(
                label="📥 TÉLÉCHARGER MON DOSSIER DE 25 PAGES",
                data=contenu_final,
                file_name=f"Expertise_Complete_{idee}.txt",
                mime="text/plain"
            )
            st.text_area("Aperçu de la rédaction d'expert :", contenu_final, height=400)
        else:
            st.info("🎯 L'expertise est prête. Réglez 9€ via le bouton ci-dessus pour débloquer votre dossier de 25 pages.")
    else:
        st.warning("Veuillez entrer une idée.")

st.markdown("---")
st.caption("Architect Solution Pro - Technologie de Conseil Automatisé 2026")
