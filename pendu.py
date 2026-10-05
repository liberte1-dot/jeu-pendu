import dictionnaire, fonctions

# pour recommencer la partie
restart = True
continuite = True


if __name__ == '__main__' :
    while(restart) :
        print("***"*8)
        print("****  Devinez le mot cache ****")
        print("****  Vous devez entrer lettre par lettre pour deviner le mot cache")
        nom = input("Entrer votre nom : ")
        print("****  Veuillez entrer une lettre ****")
        # Mot a deviner 
        mots_cache = dictionnaire.mot()
        taille_mot = len(mots_cache)
        # tentatives restantes
        coups_restant = dictionnaire.coups
        mots_utilisateurs = []
        is_found = False
        for i in range(taille_mot) :
            mots_utilisateurs.append('*')
        while(coups_restant > 0 and not is_found) : 
            lettre_utilisateur = input("Votre lettre : ")
            verification_correcte = len(lettre_utilisateur)!= 1
            # Recuperation de la lettre de l'utilisateur
            while(verification_correcte == True) :
                print("Entrer incorrect, vous devez entrer un seul caractere, ex: a. NB: Les espaces, tabulations ne sont pas autorises")
                lettre_utilisateur = input("Votre lettre : ") 
                print(lettre_utilisateur)
                verification_correcte = len(lettre_utilisateur)!= 1 
                
            # verification lettre dans mots magique 
            if lettre_utilisateur in mots_cache :
                for i in range(taille_mot) :
                    # on met la lettre sur son emplacement
                    if mots_cache[i] == lettre_utilisateur :
                        mots_utilisateurs[i] = lettre_utilisateur
            mots_utilisateurs2 = ''.join(mots_utilisateurs)
            is_found = mots_utilisateurs2 == mots_cache
            print(f"Votre mot : {mots_utilisateurs2}")
            coups_restant -= 1
            print(f"Il vous reste {coups_restant} tentatives !")
        rep = ''
        if (mots_cache == mots_utilisateurs2) :
            print(f"Felicitations le mot cache etait bel et bien : {mots_cache}, vous avez obtenu un score de {coups_restant}")
        else :
            print(f"Domage le mot cache etait : {mots_cache}, votre score est de {coups_restant}")
            
        # sauvegarde du score
        fonctions.registration(nom=nom, score=coups_restant)
        print(fonctions.afficheScore())
        while rep != 'O' and rep != 'N' :
            rep = input("Souhaitez vous continuez : O/N. Entrer 'O' pour Oui et 'N' pour Non : ").upper()
        if rep == 'N' :
            restart = False
                
                