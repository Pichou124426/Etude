#Nom: Classeur de nombre pair ou impair
#BUT: A partir d'une liste crée deux listes distincts (pair/impair)

list1 = [34 , 15, 42, 28, 3, 55, 22, 95]
pair = []
odd = []

for value in list1 :
    if (value % 2 == 0) :
        pair.append(value)
    else :
        odd.append(value)

print (pair,odd)
