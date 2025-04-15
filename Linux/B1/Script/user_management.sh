#!/bin/bash
. ./add_user.sh
. ./delete_user.sh
. ./list_user.sh
	
	
while true; do 
	echo  "Menu:"
	echo " 1. Ajouter un utilisateur"
	echo " 2. Supprimer un utilisateur"
	echo "3. Lister les utilisateur(s)"
	echo "4. Quitter"
	read -p " Choisissez une option " option 

	case $option in 
		1) 
			echo "Ajouter un utilisateur"
			# Appeler la fonction d'ajout ici ./...
		   	add_user
		
			;;

		2) 
			echo "Supprimer un utilisateur"
			# Appel fonction de suppression
			delete_user
			;;

		3) 
			echo "Lister les utilisateur(s)"
			#appel focntion
			list_user
			;;

		4)
			echo "Quitter"
			break 
			;;

		*)
			echo "Option invalide. Veuiller choisir une option valide."
			;;
		esac
	done 
	
