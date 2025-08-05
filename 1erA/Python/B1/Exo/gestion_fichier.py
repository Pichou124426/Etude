fichier = open("exo.txt","r")
for ligne in fichier :
    print(ligne.rstrip("\n"))
    
    
fichier.close()

