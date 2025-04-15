#Nom Palindrom
#BUT: Dans un premier temmps, inverse la saisie de l'utilisateur pour en suite verifier si la saisie est un palindrome ou non.
#ENTREE : Mot entré par l'Utilisateur
#SORTIE : Booleen, palindrome ou non 

word_user = input("Veuillez saisir le mot:\n")

def invertString (word):
    reverse_word_user = word_user[::-1]
    return reverse_word_user

if (invertString(word_user)==word_user):
    print("Le mot : {} est un palindrome".format(word_user))
else :
    print("Le mot : {} n'est pas un palindrome".format(word_user))
