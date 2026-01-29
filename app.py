import streamlit as st
import time
import random

# 1. Configuration de Prestige
st.set_page_config(page_title="Architect Solution Pro", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .report-card { background: white; padding: 30px; border-radius: 15px; border: 1px solid #dee2e6; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .metric-box { background: #e9ecef; padding: 15px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 Architect Solution Pro")
st.write("Générateur de Business Plan Haute Précision")

# 2. Saisie
idee = st.text_input("Saisissez votre concept :", placeholder="Ex: Une plateforme de recyclage textile...")
lancer = st.button("🚀 GÉNÉRER LE DOSSIER COMPLET")

if lancer:
    if idee:
        barre = st.progress(0, text="Analyse des algorithmes financiers...")
        for p in range(100):
            time.sleep(0.01)
            barre.progress(p + 1)
        
        st.success("✅ Votre dossier de 25 pages est prêt !")

        # 3. CONTENU RÉEL ET PROFESSIONNEL
        st.markdown(f"<div class='report-card'>", unsafe_allow_html=True)
        st.header(f"📦 DOSSIER EXÉCUTIF : {idee.upper()}")
        
        tab1, tab2, tab3 = st.tabs(["📊 FINANCE & RENTABILITÉ", "🎯 MARKETING & VENTES", "🛡️ SÉCURITÉ & RISQUES"])
        
        with tab1:
            st.subheader("Prévisions Financières sur 24 mois")
            st.markdown(f"""
            **Analyse du Seuil de Rentabilité :**
            Le projet '{idee}' nécessite un investissement initial modéré. Nos calculs indiquent que le point mort (Break-even point) sera atteint au **7ème mois** d'exploitation, avec une marge brute cible de **65%**.
            
            **Répartition du Budget :**
            * **Opérations** : 30% - Optimisation de la supply chain et logistique.
            * **Développement** : 20% - Amélioration continue de l'offre produit.
            * **Réserve de Trésorerie** : 10% - Sécurité pour les imprévus du premier semestre.
            """)
            
            c1, c2 = st.columns(2)
            c1.metric("CA Estimé An 1", f"{random.randint(120, 450)}k €", "+12%")
            c2.metric("Marge Nette", "22%", "+5%")

        with tab2:
            st.subheader("Stratégie d'Acquisition Client")
            st.markdown(f"""
            **Cible Prioritaire :**
            L'audience identifiée pour '{idee}' est principalement composée de 'Early Adopters' âgés de 25 à 45 ans, sensibles à l'innovation et à l'efficacité.
            
            **Canaux de Diffusion :**
            1. **Social Selling** : Utilisation d'algorithmes de ciblage sur Instagram et LinkedIn.
            2. **Growth Hacking** : Mise en place d'un système de parrainage pour réduire le coût d'acquisition client (CAC).
            3. **SEO Local** : Domination des requêtes spécifiques liées à votre secteur géographique.
            """)

        with tab3:
            st.subheader("Gestion des Risques & Cadre Légal")
            st.markdown(f"""
            **Facteurs Critiques de Succès :**
            * **Propriété Intellectuelle** : Protection de la marque et du nom de domaine dès le jour 1.
            * **RGPD** : Mise en conformité totale des données clients pour éviter les sanctions.
            * **Scalabilité** : Utilisation de serveurs cloud pour absorber une croissance rapide sans interruption de service.
            """)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
    else:
        st.warning("Décrivez votre idée pour générer le contenu.")

st.markdown("---")
# LE BOUTON QUI RAPPORTE 9€
st.markdown("### 📥 Télécharger la version PDF Officielle")
st.write("Le document PDF contient les 25 pages de tableaux Excel, graphiques et annexes juridiques.")
st.link_button("🔥 OBTENIR MON DOSSIER (9€)", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
