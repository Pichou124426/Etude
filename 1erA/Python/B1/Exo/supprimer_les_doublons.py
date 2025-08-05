course = ['banane','banane','pasteque','merguez']
new_list = []

def supprimer_doublons (chaine):
    new_list = []
    for position in course :
        if position not in new_list:
            new_list.append(position)
    return new_list


print (supprimer_doublons(course))



