import streamlit as st
import requests

# Configuration de la page
st.set_page_config(page_title="Business Master AI", page_icon="📈")

st.title("📈 Business Master AI")
st.markdown("**L'intelligence artificielle qui construit votre entreprise.**")

# Saisie utilisateur
idee = st.text_input("Quelle est votre idée de projet ?", placeholder="Ex: Créer une marque de vêtements...")

if st.button("🚀 GÉNÉRER MON PLAN"):
    if idee:
        try:
            # Appel à l'IA avec la clé simplifiée
            API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
            
            # Accès à la clé via le nom simplifié 'CLE_IA'
            headers = {"Authorization": f"Bearer {st.secrets['CLE_IA']}"}
            
            prompt = f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>Donne 3 étapes concrètes pour lancer ce projet : {idee}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
            
            payload = {
                "inputs": prompt,
                "parameters": {"max_new_tokens": 500},
                "options": {"wait_for_model": True}
            }
            
            with st.spinner("Analyse en cours..."):
                response = requests.post(API_URL, headers=headers, json=payload)
                resultat = response.json()
            
            if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                st.success("Voici votre plan :")
                st.write(resultat[0]['generated_text'])
            else:
                st.info("L'IA se réveille... Re-cliquez sur le bouton dans 5 secondes.")
        except Exception as e:
            st.error("Erreur de connexion. Vérifiez la clé 'import streamlit as st
import requests

# Configuration de la page
st.set_page_config(page_title="Business Master AI", page_icon="📈")

st.title("📈 Business Master AI")
st.markdown("**L'intelligence artificielle qui construit votre entreprise.**")

# Saisie utilisateur
idee = st.text_input("Quelle est votre idée de projet ?", placeholder="Ex: Créer une marque de vêtements...")

if st.button("🚀 GÉNÉRER MON PLAN"):
    if idee:
        try:
            # Appel à l'IA avec la clé simplifiée
            API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
            
            # Accès à la clé via le nom simplifié 'CLE_IA'
            headers = {"Authorization": f"Bearer {st.secrets['CLE_IA']}"}
            
            prompt = f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>Donne 3 étapes concrètes pour lancer ce projet : {idee}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
            
            payload = {
                "inputs": prompt,
                "parameters": {"max_new_tokens": 500},
                "options": {"wait_for_model": True}
            }
            
            with st.spinner("Analyse en cours..."):
                response = requests.post(API_URL, headers=headers, json=payload)
                resultat = response.json()
            
            if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                st.success("Voici votre plan :")
                st.write(resultat[0]['generated_text'])
            else:
                st.info("L'IA se réveille... Re-cliquez sur le bouton dans 5 secondes.")
        except Exception as e:
            st.error("Erreur de connexion. Vérifiez la clé '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' dans vos Secrets.")
    else:
        st.warning("Veuillez entrer une idée.")

st.markdown("---")
st.subheader("💰 Obtenez le dossier complet")
st.write("Pour recevoir votre stratégie de 20 pages et vos fournisseurs :")
# Remplacez l'URL ci-dessous par votre lien Stripe REEL dès qu'il est prêt
st.link_button("🔥 PAYER 9€ ET TÉLÉCHARGER", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")' dans vos Secrets.")
    else:
        st.warning("Veuillez entrer une idée.")

st.markdown("---")
st.subheader("💰 Obtenez le dossier complet")
st.write("Pour recevoir votre stratégie de 20 pages et vos fournisseurs :")
# Remplacez l'URL ci-dessous par votre lien Stripe REEL dès qu'il est prêt
st.link_button("🔥 PAYER 9€ ET TÉLÉCHARGER", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
