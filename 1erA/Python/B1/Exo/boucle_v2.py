import random

#generateur de nimbre aléatoire

num_funder = random.randint (0,101)
num_user = input("Saisie un chiffre de départ :\n")
tentative = 0
#condition lorsque les deux nombres sont differents 
while not ( int(num_funder) == int(num_user) ) :
    if int(num_funder) > int(num_user):
        print ("Plus grand, votre ancienne saisie était",int(num_user))
        num_user = input("Saisie un nouveau chiffre :\n")
        tentative += 1
        
    else :
        print("Plus petit, votre ancienne saisie était",int(num_user))
        num_user = input("Saisie un nouveau chiffre :\n")
        tentative += 1
# Lorsque les deux sont identiques.
tentative += 1
print ("Bravo, tu as trouvé en",tentative," tentative(s) et  le nombre mistére  était :", int(num_funder),".")

