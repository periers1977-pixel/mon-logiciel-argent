import streamlit as st
import requests
import time

st.set_page_config(page_title="Business Master AI", page_icon="🚀")

st.title("🚀 Mon Générateur de Business")
st.write("Obtenez une stratégie professionnelle pour votre projet en quelques secondes.")

idee = st.text_input("Votre projet", placeholder="Ex: Ouvrir un food-truck bio...")

if st.button("Obtenir mon plan"):
    if idee:
        # --- DÉBUT DE LA BARRE DE PROGRESSION ---
        progress_text = "Analyse approfondie de votre projet en cours..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.02)  # Simule le temps de réflexion de l'IA
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        time.sleep(0.5)
        my_bar.empty() # Efface la barre une fois fini
        # --- FIN DE LA BARRE DE PROGRESSION ---

        try:
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
            headers = {"Authorization": "Bearer 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"}
            payload = {"inputs": f"Donne 3 conseils stratégiques pour : {idee}", "options": {"wait_for_model": True}}
            
            with st.spinner("Rédaction finale..."):
                response = requests.post(API_URL, headers=headers, json=payload)
                resultat = response.json()
                
                if isinstance(resultat, list) and 'generated_text' in resultat[0]:
                    st.success("✅ Votre plan est prêt !")
                    st.markdown(f"### Conseils Stratégiques :\n{resultat[0]['generated_text']}")
                else:
                    st.warning("L'IA est encore en train de chauffer. Re-cliquez une fois.")
        except:
            st.error("Petit délai réseau. Veuillez réessayer.")
    else:
        st.error("Veuillez entrer une idée avant de cliquer.")

st.markdown("---")
st.link_button("🔥 PAYER 9€ POUR LE PLAN COMPLET", "https://buy.stripe.com/test_evq3cp2GmgDg6Ho6axfUQ00")
st.caption("Paiement sécurisé par Stripe. Accès immédiat au dossier PDF.")
