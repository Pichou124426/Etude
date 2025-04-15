#!/bin/sh

read -p "Combien de joueurs dans la partie ? " nb_player

player=()
scores=()
wins=()

for ((i=1; i<=nb_player; i++)); do 
    read -p "Nom du joueur $i : " name 
    player+=("$name")
    scores+=(301)
    wins+=(0)
done 

# Début réel du jeu

nb_tours=1

while true; do 
    for ((i=0; i<nb_player; i++)); do 
        archer="${player[$i]}"
        score_actuel="${scores[$i]}"
        echo  "\nAu tour de $archer (score actuel : $score_actuel)"
        read -p "Score réalisé : " score 

        if ! [[ "$score" =~ ^[0-9]+$ ]]; then 
            echo "La valeur saisie est incorrecte, veuillez saisir un nombre."
            continue 
        fi 

        new_score=$((score_actuel - score))

        if ((new_score < 0)); then 
            echo "Vous avez tapé trop haut !! Redescendez à $score_actuel"
        elif ((new_score == 0)); then 
            echo "En plein dans le mille, $archer a gagné la partie en $nb_tours tours !"
            wins[$i]=$((wins[$i] + 1))
            echo "$archer gagne sa partie en $nb_tours tours" >> stats.txt
            exit 0
        else 
            scores[$i]=$new_score
        fi

        ((nb_tours++))
    done 
done
