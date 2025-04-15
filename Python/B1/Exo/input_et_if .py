identifiant = "toto"
password = "1234"

userid = input("Entrer votre identifiant :")
usermdp = input("Entrer votre mot de passe :")

if identifiant == userid and password == usermdp :
    print ("connexion reussi")

else : 
    print ("connexion pourri")