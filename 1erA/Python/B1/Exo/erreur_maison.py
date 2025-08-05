def age () :
    age = input ("quel est ton age : \n")
    age = int(age)

    if age > 125 : 
        raise ValueError("Cet age est trop avancé")

