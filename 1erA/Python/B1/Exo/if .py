age_user = input("Saisir votre age :")

if int(age_user)>= 18 : 
    if int(age_user) >62 :
        print ("Vous etes retraité.")
    else : 
        print ("Tu es majeur.")
else :
    print ("Tu es mineur. ")