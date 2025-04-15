#Nom: Createur de liste 
#BUT: Concatener deux listes d'une maniere où chaque age et suivi du prenom, ainsi que lorsque l'on affiche que chaque couple (age/prenom) soit à la ligne
#ENTREE : Deux listes 
#SORTIE : Une liste 






list1 = [31, 18, 41, 60, 1, 17, 27, 55, 89, 125, 19, 36]
list2 = ["Pierre", "Mohamed", "Elodie", "Georges", "Timéo", "Sirine", "Amadou","Matthieu", "Néo", "Jeanne", "Ece", "Nicolas"]
list3 = []
for age, name in zip(list1, list2):
    list3.append(age)
    list3.append(name)


for age, name in zip(list1, list2):
    print("{} {}".format(age, name))