import random

messages= {
    "welcome" : {
        "Français": "Bienvenue dans le jeu du Codeur !",
        "English": "Welcome to the Codebreaker game!"
    },
    "rules" : {
        "Français": "Le but du jeu est de deviner la combinaison secrète de chiffres.",
        "English": "The goal of the game is to guess the secret combination of numbers."
    },
    "difficulty" : {
        "Français": "Choisissez le niveau de difficulté :",
        "English": "Choose the difficulty level:"
    },
    "easy" : {
        "Français": "Facile (Chiffre bien placé + Chiffre dans la combinaison)",
        "English": "Easy (Correct digit + Digit in the combination)"
        
    },
    
    "hard" : {
        "Français": "Difficile (Uniquement chiffre bien placé)",
        "English": "Hard (Only correct digit)"
        
    },
    "enter_choice (1-2)" : {
        "Français": "Entrez votre choix (1-2) :",
        "English": "Enter your choice (1-2):"
        
    },
    "error_invalid_choice" : {
        "Français": "Choix invalide. Veuillez choisir un niveau entre 1 et 2.",
        "English": "Invalid choice. Please choose a level between 1 and 2."
        
    },
    "attempts_game" : {
        "Français": "Tentative(s) exécutée(s) :",
        "English": "Attempt(s) executed:"
        
    },
}

language = "Français"
combinaison_to_find = ""
difficulty = "Facile"
attempts_game = 0
proposed_combinaisons = []

def generate_combinaison(lenght=4):
    global combinaison_to_find
    combinaison_to_find = [random.randint(0, 9) for _ in range(lenght)]
    return combinaison_to_find
    
def set_difficulty():
    global language, difficulty, attempts_left, attempts_left_game
    print("---------------------------------------")
    print("")
    print(messages["difficulty"][language])
    print(messages["easy"][language])
    print(messages["hard"][language])
    print("")
    
    try:
        choice = int(input(messages["enter_choice (1-2)"][language]))
        match choice:
            case 1:
                difficulty = "Facile"
                correct_digit= 0
                digit_in_combinaison = 0
            case 2:
                difficulty = "Difficile"
                correct_digit= 0
            case _:
                print(messages["error_invalid_choice"][language])
                return set_difficulty()
    except ValueError:
        print(messages["error_invalid_choice"][language])
        return set_difficulty()


def show_rules():
    global language
    print("")
    print(messages["welcome"][language])
    print(messages["rules"][language])
    print("")
    print(messages["difficulty"][language])
    print(messages["easy"][language])
    print(messages["hard"][language])
    print("")
    

def game_menu():
    global language, proposed_combinaisons, attempts_game