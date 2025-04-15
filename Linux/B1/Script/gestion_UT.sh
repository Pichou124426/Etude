#!bin/bash 
. ./f°_gestion_UT
while true; do 
	echo  "Menu de la gestion des utilisateurs:"
	echo " 1. Creer un utilisateur"
	echo " 2. Creer un groupe"
	echo "3. Gerer les permissions "
	echo "4. Quitter"
	read -p " Choisissez une option que vous souhaitez executer.  " option 

	case $option in 
		1) 
			echo "Ajouter un utilisateur"
			# Appeler la fonction d'ajout ici ./...
		   	add_user
		
			;;

		2) 
			echo "Creer un groupe"
			# Appel fonction de creation groupe 
			create_groups 
			;;

		3) 
			echo "Gerer les permissions"
			#appel focntion
			manage-permissions
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
	
