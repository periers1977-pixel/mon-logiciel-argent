def generer_livrable_integral(idee):
    """Rédige un dossier dont les titres de chapitres sont variés et précis."""
    # On définit une liste de titres pro pour varier les plaisirs
    titres_pro = [
        "ANALYSE DU MARCHÉ ET OPPORTUNITÉS", "INNOVATIONS ET DISRUPTIONS", 
        "CADRE RÉGLEMENTAIRE ET CONFORMITÉ", "MODÈLE ÉCONOMIQUE ET RENTABILITÉ",
        "STRATÉGIE D'ACQUISITION CLIENTS", "GESTION DES RISQUES OPÉRATIONNELS",
        "TENDANCES DE CONSOMMATION 2026", "DIFFÉRENCIATION CONCURRENTIELLE",
        "OPTIMISATION FISCALE ET JURIDIQUE", "LEVIERS DE CROISSANCE PRIORITAIRES",
        "ÉVALUATION DE LA SCALABILITÉ", "DIGITALISATION ET AUTOMATISATION"
    ]
    
    base_savoir = moteur_recherche_24x_dynamique(idee)
    pages = []
    
    # Nombre de chapitres adapté dynamiquement
    nb_chapitres = min(len(titres_pro), len(base_savoir) // 4) 
    
    for i in range(nb_chapitres):
        # ICI : On pioche un titre différent dans la liste au lieu d'un texte fixe
        titre_page = f"CHAPITRE {i+1} : {titres_pro[i]}"
        sections = []
        
        for s in range(5):
            if base_savoir:
                data = base_savoir.pop(0)
            else:
                data = f"L'analyse sectorielle pour '{idee}' confirme l'importance de ce pilier stratégique."
            
            labels = ["CONTEXTE", "DIAGNOSTIC", "ENJEUX", "STRATÉGIE", "DÉPLOIEMENT"]
            sections.append(f"<b>{labels[s]} :</b> {data}")
            
        pages.append([titre_page] + sections)
        
    signature = hashlib.sha256(str(pages).encode()).hexdigest()[:12].upper()
    return pages, signature
