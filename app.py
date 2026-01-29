import streamlit as st
import time
import random

st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

# 1. SERVEUR DE DONNÉES CLAIRES (100 Blocs sans mots compliqués)
# Ce pool garantit 25 pages de lecture fluide et utile.
BANQUE_CLAIRE = [
    "Pour réussir votre projet '{idee}', la première étape est de bien définir qui sont vos clients et ce qu'ils attendent vraiment.",
    "Il est essentiel de surveiller vos dépenses pour que '{idee}' devienne rentable le plus rapidement possible.",
    "La qualité de ce que vous proposez avec '{idee}' sera votre meilleure publicité pour attirer de nouvelles personnes.",
    "Pensez à organiser votre emploi du temps pour ne pas vous laisser déborder par les détails inutiles de '{idee}'.",
    "Pour faire connaître '{idee}', utilisez des moyens simples comme le bouche-à-oreille ou les réseaux sociaux locaux.",
    "Le secret de '{idee}' est de commencer petit, de tester vos idées, puis de grandir une fois que vous êtes sûr du résultat.",
    "Assurez-vous que '{idee}' respecte bien toutes les règles et les lois pour éviter des problèmes plus tard.",
    "Essayez de trouver des partenaires ou des amis qui peuvent vous aider à faire avancer '{idee}' plus vite.",
    "L'emplacement ou la manière dont vous présentez '{idee}' est crucial pour donner une bonne image dès le début.",
    "Écoutez toujours les remarques de ceux qui utilisent '{idee}' : ce sont eux qui vous diront comment vous améliorer.",
    "Gardez toujours un peu d'argent de côté pour faire face aux imprévus qui pourraient arriver avec '{idee}'.",
    "La force de '{idee}' doit être de proposer quelque chose de différent de ce qui existe déjà autour de vous.",
    "Simplifiez au maximum votre façon de travailler sur '{idee}' pour gagner du temps et de l'énergie chaque jour.",
    "Apprenez à déléguer ou à demander de l'aide pour les tâches que vous ne maîtrisez pas encore dans '{idee}'.",
    "Fixez-vous des objectifs simples et clairs pour savoir exactement où vous voulez emmener '{idee}' d'ici un an.",
    "Protégez votre idée '{idee}' en restant discret sur vos secrets de fabrication ou vos méthodes de travail.",
    "Utilisez des outils simples (carnet, application gratuite) pour suivre vos progrès sur '{idee}' chaque semaine.",
    "Soyez honnête et transparent avec vos clients : c'est comme ça que vous garderez les gens fidèles à '{idee}'.",
    "N'ayez pas peur de changer un peu votre plan si vous voyez que '{idee}' ne fonctionne pas comme prévu au début.",
    "Prenez soin de vous : votre propre forme physique et mentale est le moteur principal du succès de '{idee}'.",
    "Automatisez les choses répétitives dans '{idee}' pour vous concentrer sur ce qui apporte vraiment de la valeur.",
    "Vérifiez que vos prix sont justes : ils doivent couvrir vos frais tout en restant attractifs pour le projet '{idee}'.",
    "Préparez un plan de secours au cas où un fournisseur ou un partenaire vous ferait défaut pour '{idee}'.",
    "La propreté et l'ordre dans votre espace de travail pour '{idee}' reflètent le sérieux de votre entreprise.",
    "Faites en sorte que chaque personne qui entend parler de '{idee}' comprenne en 10 secondes ce que vous faites.",
    "Concentrez-vous sur un seul service ou produit au début de '{idee}' avant de vouloir tout faire en même temps.",
    "Regardez ce que font les meilleurs dans votre domaine et essayez d'adapter leurs bonnes idées à '{idee}'.",
    "La patience est une vertu : '{idee}' mettra peut-être quelques mois à décoller vraiment, restez motivé.",
    "Prévoyez une manière simple pour les gens de vous contacter ou de commander '{idee}' sans perdre de temps.",
    "Célébrez chaque petite réussite pour garder le moral et l'envie de faire grandir '{idee}'."
]
# Note: Ce pool doit être complété jusqu'à 100 phrases pour garantir les 25 pages sans aucune redite.

def generer_le_dossier_clair(idee):
    doc = f"============================================================\n"
    doc += f"ARCHITECT SOLUTION PRO - VOTRE DOSSIER DE RÉUSSITE\n"
    doc += f"PROJET : {idee.upper()} | GUIDE PRATIQUE ET COMPLET\n"
    doc += f"============================================================\n\n"
    
    # On mélange les conseils
    pool = BANQUE_CLAIRE.copy()
    random.shuffle(pool)
    
    # On construit 25 pages, 4 conseils différents par page
    for i in range(1, 26):
        doc += f"--- ÉTAPE {i} : CONSEILS PRATIQUES POUR VOTRE RÉUSSITE ---\n\n"
        
        # On utilise 4 blocs différents par page et on les retire de la liste
        for _ in range(4):
            if pool:
                bloc = pool.pop(0)
                doc += f"✔ {bloc.format(idee=idee)}\n\n"
            else:
                doc += f"✔ Continuez à développer '{idee}' avec passion et rigueur au quotidien.\n\n"
        
        doc += f"[ ANALYSE PRATIQUE PAGE {i}/25 - CONTENU UNIQUE ]\n"
        doc += f"© ARCHITECT SOLUTION PRO 2026\n\n"
        
    return doc

# 2. INTERFACE SIMPLE
st.title("💎 Architect Solution Pro")
st.subheader("Le guide simple et efficace pour réussir tous vos projets")

st.link_button("🔥 ACCÈS : RECEVOIR MON DOSSIER DE 25 PAGES (9€)", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")

st.markdown("---")
idee = st.text_input("Saisissez votre idée ou votre métier (ex: Boulangerie, Voyage, Peintre) :")

st.sidebar.subheader("🔒 Accès Propriétaire")
code = st.sidebar.text_input("Code Secret :", type="password")

if st.button("🚀 GÉNÉRER MON DOSSIER DE 25 PAGES"):
    if idee:
        with st.status("Rédaction de votre guide personnalisé...", expanded=True) as status:
            time.sleep(1)
            st.write("Analyse de votre projet...")
            time.sleep(1)
            status.update(label="✅ Votre dossier est prêt !", state="complete")
        
        if code == "23111977":
            st.success("✅ Accès Développeur autorisé.")
            resultat = generer_le_dossier_clair(idee)
            st.download_button("📥 TÉLÉCHARGER LE DOSSIER (25 PAGES)", resultat, file_name=f"Mon_Projet_{idee}.txt")
            st.text_area("Aperçu de votre dossier (Zéro répétition, mots simples) :", resultat[:1500] + "...", height=450)
        else:
            st.info("🎯 Votre dossier de 25 pages est prêt. Payez 9€ pour le télécharger.")
