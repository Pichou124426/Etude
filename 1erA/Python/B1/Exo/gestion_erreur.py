try:
    number = input("Donne moi un diviseur : \n")
    number = int(number)
    result = 150 / number
    print("Le résultat est", int(result))
except ZeroDivisionError:
    print("Tu es un zeub, c'est impossible de diviser par zéro !!!")
except ValueError:
    print("Tu es un zeub, c'est impossible de diviser par autre chose qu'un nombre !!!")
