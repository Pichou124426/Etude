#NOM: Max
#BUT: Ressortir la plus grande valeur d'une liste 

list1 = [42, 4, 11, 12, 8, 73, 1, 21] 

max = list1[0]
for value in list1 :
    if value > max :
        max = value

print("Le plus grand élément de cette liste à la valeur {}.".format(max))