#!bin/bash

delete_user(){
	read -p "Entrez le nom de l'utilisateur à supprimer." username 
	sudo userdel $username 

	if [ $? -eq 0 ];then 
		echo " Utilisateur $username supprimé avec succés."
	else
		echo " Echec de la suppression de l'utilisateur $username."
	fi 
}
