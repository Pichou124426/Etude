chelou = (1, 4, 7, "toto", [1, ("x", 12)], 9)

pairs = []
impairs = []

for element in chelou:
    try:
        if isinstance(element, int):
            if element % 2 == 0:
                pairs.append(element)
            else:
                impairs.append(element)
        else:
            raise ValueError(f"L'élément {element} n'est pas un chiffre.")
    except ValueError as e:
        print(e)

tuples_nombres = (pairs, impairs)
print(tuples_nombres)