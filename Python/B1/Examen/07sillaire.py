#Nom: Classement des mots 
#BUT: Fait un classement du plus petit mot au plus grand et en cas d'egalité on les departages par l'ordre alphabetique. 
# ENTREE : Liste 
#SORTIE: Liste comportant des tuples 

words = ["tomate", "salade", "oignons", "pain"]
def trier_mots(words):
    
    liste_tuple = [(hint, word, len(word)) for hint, word in enumerate(words)]
    liste_tuple.sort(key=lambda order: (order[2], order[1]))
    return liste_tuple

resultat = trier_mots(words)
print(resultat)


