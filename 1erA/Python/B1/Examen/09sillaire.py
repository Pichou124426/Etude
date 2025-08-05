#NOM: Calculatrice 
# Entree : saisie UT deux nombre 
# Sortie : resultats 

def calculatrice():
    try:
       
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
    except ValueError:
        print("Erreur : vous devez entrer des nombres valides.")
        return

    operation = input("Entrez l'opération (+, -, *, /) : ")

    
    if operation == "+":
        resultat = a + b
    elif operation == "-":
        resultat = a - b
    elif operation == "*":
        resultat = a * b
    elif operation == "/":
        if b == 0:
            print("Erreur : division par zéro impossible .")
            return
        else:
            resultat = a / b
    else:
        print("Erreur : opération non valide.")
        return

    
    print(f"Le résultat de {a} {operation} {b} est : {resultat}")


calculatrice()
