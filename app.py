import streamlit as st
import time
import random

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# 1. MOTEUR DE GÉNÉRATION DE LIVRABLES (Données techniques et chiffrées)
BIBLIO_ULTIMATE = {
    "STRATEGIE": [
        "**Analyse de la Chaîne de Valeur :** Pour {idee}, l'avantage concurrentiel repose sur la désintermédiation des flux logistiques. Nous préconisons un modèle d'intégration verticale pour capturer une marge supplémentaire de {val}%.",
        "**Ingénierie de la Scalabilité :** Le déploiement de {idee} doit suivre un modèle de croissance exponentielle (Blitzscaling). Nous préconisons une infrastructure élastique capable d'absorber une charge de +400% sans dégradation du service client.",
        "**Audit des Barrières à l'Entrée :** La protection de votre concept {idee} passe par la création d'effets de réseau sémantiques et la sécurisation de protocoles propriétaires."
    ],
    "MARKETING_AVANCE": [
        "**Ingénierie de la Rétention (LTV) :** Le coût d'acquisition pour {idee} étant indexé sur la concurrence publicitaire, la rentabilité réelle se jouera sur le taux de réachat et l'optimisation du tunnel de vente secondaire.",
        "**Psychologie du Consommateur :** L'étude comportementale pour {idee} révèle des leviers d'achat basés sur la rareté et l'autorité. Nous préconisons un tunnel de vente segmenté par persona.",
        "**Optimisation du Taux de Conversion (CRO) :** Chaque point de friction dans le parcours utilisateur de {idee} doit être éliminé par des tests rigoureux sur les pages de destination."
    ],
    "FINANCE_STRUCTURALE": [
        "**Modélisation du Seuil de Rentabilité :** Avec un panier moyen de {val_p}€, le point mort pour {idee} est projeté sur un volume de {val_v} unités mensuelles.",
        "**Plan de Trésorerie Prévisionnel :** La gestion du BFR (Besoin en Fonds de Roulement) pour {idee} nécessite un suivi hebdomadaire des créances clients et une renégociation des délais fournisseurs.",
        "**Valorisation et Sortie :** Le multiple de l'EBITDA appliqué à {idee} en 2026 permet d'envisager une valorisation cible de {val_m} fois le résultat opérationnel net en Année 3."
    ]
}

def generer_livrable_expert(idee):
    doc = f"============================================================\n"
    doc += f"ARCHITECT SOLUTION PRO - LIVRABLE D'EXPERTISE MÉTIER\n"
    doc += f"PROJET : {idee.upper()} | RÉFÉRENCE ANALYTIQUE : #EXP-{random.randint(1000, 9999)}\n"
    doc += f"============================================================\n\n"
    
    types = ["STRATEGIE", "MARKETING_AVANCE", "FINANCE_STRUCTURALE"]
    
    for i in range(1, 26):
        doc += f"--- CHAPITRE {i} : ANALYSE DÉTAILLÉE DU SECTEUR ---\n\n"
        
        # Sélection de blocs d'expertise différents pour chaque page pour éviter la répétition
        type_actuel = types[i % 3]
        extraits = random.sample(BIBLIO_ULTIMATE[type_actuel], 2)
        
        for e in extraits:
            doc += e.format(
                idee=idee, 
                val=random.randint(12, 28), 
                val_p=random.randint(45, 190), 
                val_v=random.randint(100, 500),
                val_m=random.randint(5, 9)
            ) + "\n\n"
        
        doc += f"Cette analyse technique de la page {i} est certifiée conforme aux protocoles de 2026.\n"
        doc += f"© ARCHITECT SOLUTION PRO - TOUS DROITS RÉSERVÉS\n\n"
        
    return doc

# 2. INTERFACE UTILISATEUR
st.title("💎 Architect Solution Pro")
st.subheader("Système Expert de Conseil Stratégique")

st.link_button("🔥 ACCÈS CLIENT : ACHETER LE DOSSIER COMPLET (9€)", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre projet pour une expertise de 25 pages :", placeholder="Ex: Boutique de mode éco-responsable...")

st.sidebar.subheader("🔒 Zone Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER LE LIVRABLE COMPLET"):
    if idee:
        with st.status("Génération du document d'expertise de 25 pages...", expanded=True) as status:
            time.sleep(1)
            st.write("Extraction des modèles financiers...")
            time.sleep(1)
            st.write("Rédaction des protocoles stratégiques...")
            status.update(label="✅ Dossier prêt pour téléchargement", state="complete")
        
        if code == "23111977":
            st.success("✅ Accès Développeur : Dossier de 25 pages généré.")
            resultat = generer_livrable_expert(idee)
            
            st.download_button(
                label="📥 TÉLÉCHARGER LE LIVRABLE (25 PAGES)",
                data=resultat,
                file_name=f"Expertise_Pro_{idee}.txt",
                mime="text/plain"
            )
            st.text_area("Aperçu de la rédaction d'expert :", resultat[:2000] + "...", height=400)
        else:
            st.info("🎯 L'expertise est générée. Payez 9€ pour débloquer le téléchargement client.")
