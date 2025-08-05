#!bin/bash 


add_user(){
	read -p "Entrer un nom d'utilisateur :" username
	sudo useradd $username
	if [ $? -eq 0 ];then 
		echo "Utilisatuer $username ajouté avec succés."
		sudo passwd $username 
		read -p "Entrer la durée d'expiration du mots de passe en jours :" expiration
		sudo chage -M $expiration $username 
		echo "Pas de soucis, le mdp de $username expira dans $expiration jours. "
	else 
		echo " Echec de l'ajout de l'utilisateur $username."
	fi
}




create_groups(){
	read -p 
}
