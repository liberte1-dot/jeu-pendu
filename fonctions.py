# creation d'utilisateurs
import pickle
import os

def isPresent(nom, scores) :
    for i in range(len(scores)) :
        if scores[i]['nom'] == nom :
            return [True, i]
    return [False, -1]
def afficheScore() :
    with open("scores.bin", 'rb') as fichier :
        pickler = pickle.Unpickler(fichier)
        return pickler.load()

def registration(nom, score) :
    nom = nom.upper()
    if (not os.path.exists('scores.bin') or os.path.getsize('scores.bin') == 0) :
        with open('scores.bin', 'wb') as fichier :
            # Creer le fichier si inexistant ou vide
            # Creation d'une liste vide pour stocker les utilisateurs
            pickler = pickle.Pickler(fichier)
            pickler.dump([])
        
    with open("scores.bin", "rb+") as fichier :
        # Recuperation liste utilisateur
        pickler = pickle.Unpickler(fichier)
        scores = pickler.load()
        fichier.seek(0)        # on remet le marque-page au début
        fichier.truncate()     # on efface l'ancien contenu
        # Ajout d'un nouvel utilisateur
        if (len(scores) == 0) :
            print("aert")
            scores.append({'nom':nom, 'score':score})
        
        else :
            print("Bast")
            # La liste n'est pas vide on doit ajouter un utilisateur
            presence_utilisateur = isPresent(nom, scores)
            if presence_utilisateur[0] :
                # Si l'utilisateur est deja present j'incremente son score avec le nouveau score
                scores[presence_utilisateur[1]]['score'] += score
            else :
                # Ajoutons l'utilisateur non present
                scores.append({'nom':nom, 'score':score})
        # Sauvegardons le score final 
        pickler = pickle.Pickler(fichier)
        pickler.dump(scores)


                
                    
            
# [
#     {'nom' : 'TAMO', 'score': 12},
# ]