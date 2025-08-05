#BUT: Creer une fonction qui prend en compte la liste 1 et le tuple 1 et cela renvoie un dictionnaire 
#ENTREE : Un tuple et une liste 
#SORTIE : un dictionaire 

l1 = [1,2,3,4,5]
t2 = ("a","b","c","d","e")

def create_dicto (clé,valeur):
    mon_dictio = {}
    for position in range (len(clé)) :
        mon_dictio[clé[position]] = valeur [position]
    return mon_dictio
   

print (create_dicto(l1,t2))