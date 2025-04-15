#!/bin/sh





function choose_game_mode {
    while true; do
        read -p "Choisissez le mode de jeu (301 ou 501) : " game_mode
        if [[ "$game_mode" == "301" || "$game_mode" == "501" ]]; then
            break
        else
            echo "Mode de jeu invalide. Veuillez entrer 301 ou 501."
        fi
    done
}

function setup_players {
    player=()
    scores=()
    wins=()
    for ((i=1; i<=nb_player; i++)); do 
        read -p "Nom du joueur $i : " name 
        player+=("$name")
        scores+=("$game_mode")
        wins+=(0)
    done 
}

function reset_scores {
    for ((i=0; i<nb_player; i++)); do
        scores[$i]=$game_mode
    done
}

function play_game {
    nb_tours=1

  
    echo -e "\nPartie commencée à : $(date)\n" >> stats.txt
    printf "%-20s %-15s %-20s\n" "Joueur" "Score restant" "Tours pour gagner" >> stats.txt
    echo "--------------------------------------------------------" >> stats.txt

    while true; do 
        for ((i=0; i<nb_player; i++)); do 
            archer="${player[$i]}"
            score_actuel="${scores[$i]}"
            echo "\nAu tour de $archer (score actuel : $score_actuel)"
            while true; do
                read -p "Score réalisé : " score 

                if ! [[ "$score" =~ ^[0-9]+$ ]]; then 
                    echo "La valeur saisie est incorrecte, veuillez saisir un nombre."
                    continue 
                fi 

                if ((score > 180)); then
                    echo "Wow ! Tu joues avec un lance-roquettes ou des fléchettes ? 180 c'est le max… à moins que tu aies trouvé une faille spatio-temporelle ? $archer ton score sent un peu le mytho, non ?"
                    continue
                fi

                new_score=$((score_actuel - score))

                if ((new_score < 0)); then 
                    echo "Vous avez tapé trop haut !! Redescendez à $score_actuel"
                    break
                elif ((new_score == 0)); then 
                    echo "En plein dans le mille, $archer a gagné la partie en $nb_tours tours !"
                    wins[$i]=$((wins[$i] + 1))
                    printf "Le grand vainqueur est : %s\n" "$archer" >> stats.txt
                    printf "%-20s %-15s %-20s\n" "$archer" "$new_score" "$nb_tours" >> stats.txt
                    echo "--------------------------------------------------------" >> stats.txt

                  
                    for ((j=0; j<nb_player; j++)); do
                        if [[ $i -ne $j ]]; then
                            printf "%-20s %-15s %-20s\n" "${player[$j]}" "${scores[$j]}" "-" >> stats.txt
                        fi
                    done

                    echo "--------------------------------------------------------" >> stats.txt
                    return
                elif ((score == 180)); then
                    echo "Bravo $archer ! ONE HUNDRED AND EIGHTY !!! 🎯🔥 !"
                fi
                
                scores[$i]=$new_score
                break
            done

            ((nb_tours++))
        done 
    done
}

function main_menu {
    echo "\nMenu :"
    echo "Q - Quitter le programme"
    echo "R - Revanche"
    echo "E - Éditer le nombre de joueurs"
    echo "S - Afficher les statistiques"
    read -p "Choix : " choice

    case "$choice" in 
        Q|q) exit 0 ;;
        R|r) reset_scores; play_game; main_menu ;;
        E|e) read -p "Combien de joueurs dans la partie ? " nb_player
             setup_players
             play_game
             main_menu ;;
		 S|s) cat stats.txt 
		 		main_menu ;;
        *) echo "Choix invalide, veuillez réessayer."
           main_menu ;;
    esac
}

function validate_players_count {
    while true; do
        read -p "Combien de joueurs dans la partie ? " nb_player
        if ! [[ "$nb_player" =~ ^[0-9]+$ ]] || [ "$nb_player" -le 0 ]; then
            echo "Valeur incorrecte. Veuillez saisir un nombre entier positif."
        else
            break
        fi
    done
}

validate_players_count
choose_game_mode
setup_players
play_game
main_menu
