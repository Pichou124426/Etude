import random

""" french_words = [
    "chat", "maison", "arbre", "soleil", "fleur", "lune", "étoile", "rivière",
    "montagne", "forêt", "océan", "oiseau", "nuage", "pluie", "neige", "vent",
    "feuille", "cheval", "château", "jardin", "école", "train", "voiture", 
    "livre", "fenêtre", "porte", "chaise", "table", "couleur", "musique", 
    "ciel", "village", "pont", "bâteau", "route", "cloche", "mirroir", 
    "rivage", "lampe", "bijou", "saison", "drapeau", "chanson", "vélo", 
    "clémentine", "citron", "cerise", "framboise", "fromage", "piano"
]

english_words = [
    "hello", "world", "tree", "flower", "river", "mountain", "forest", 
    "ocean", "bird", "cloud", "rain", "snow", "wind", "leaf", "horse", 
    "castle", "garden", "sun", "moon", "star", "school", "train", "car", 
    "book", "window", "door", "chair", "table", "color", "music", "sky", 
    "village", "bridge", "boat", "road", "bell", "mirror", "shore", "lamp", 
    "jewel", "season", "flag", "song", "bike", "clementine", "lemon", 
    "cherry", "raspberry", "cheese", "piano"
] """

small_french_words = [
    "chien", "livre", "pomme", "boîte", "plume", "beurre", "salon",
    "raisin", "danse", "jouet", "balle", "cacao", "tasse", "écran",
    "hiver", "lampe", "brique", "route", "avion", "filme"
]

medium_french_words = [
    "château", "carrosse", "aventure", "camomille", "cascadeur", "évasion",
    "résidence", "mélancolie", "perroquet", "couturier", "architecte",
    "nuancier", "ballerine", "arbalète", "frontière", "lanterne", "musicien",
    "ombrageux", "explosion", "séparateur"
]

large_french_words = [
    "philosophie", "bibliothèque", "émerveillement", "mondialisation",
    "urbanisation", "responsabilité", "bienveillance", "volatilisation",
    "identification", "réinterprétation", "aristocratique", "contrebalancement",
    "électromécanique", "institutionnalisation", "psychologiquement"
]

small_english_words = [
    "apple", "chair", "train", "cloud", "table", "glass", "house",
    "light", "horse", "water", "plant", "piano", "beach", "grape",
    "knife", "clock", "floor", "dress", "mouse", "brush"
]

medium_english_words = [
    "mountain", "raincoat", "fountain", "passport", "computer",
    "landscape", "pineapple", "blueberry", "magazine", "adventure",
    "paradise", "airplane", "butterfly", "dinosaur", "sandwich",
    "ballerina", "treasure", "umbrella", "notebook", "telephone"
]

large_english_words = [
    "extraordinary", "responsibility", "transformation",
    "infrastructure", "psychological", "identification",
    "revolutionary", "microscopic", "entertainment",
    "misunderstood", "international", "philosophical",
    "sensationalism", "investigation", "extraordinaire"
]


language = "Français"
difficulty = "Facile"
word_to_find = random.choice(small_french_words)
errors = 0
proposed_letters = []

def edit_language():
    global language
    print("")
    choice = input("Choisissez la langue du mot à trouver (F = Français, E = English): ")
    print("")
    match choice:
        case 'F':
            print("Le mot à deviner est en français.")
            language = "Français"
            main_menu()
           
        case 'E':
            print("Le mot à deviner est en anglais.")
            language = "English"
            main_menu()
            
        case _:
            print("Choix invalide. Veuillez choisir 'F' pour Français ou 'E' pour Anglais.")
            edit_language()


def show_rules():
    print("---------------------------------------")
    print("")
    print("    Bienvenue dans le jeu du Pendu !")
    print("")
    print("Le but du jeu est de deviner le mot caché en proposant des lettres.")
    print("Vous avez un nombre limité de vie en fonction du niveau de difficulté choisi.")
    print("Bonne chance !")
    print("")
    
def game_menu():
    global language, word_to_find
    verify_errors()
    print("")
    print("")
    print("")
    print("---------------------------------------")
    print("           Jeu du Pendu")
    show_word()
    show_pendu(errors)
    print("Lettres déjà proposées : ", proposed_letters)
    print("")
    print("Que souhaitez-vous faire ?")
    print("1. Tenter de découvrir le mot caché ")
    print("2. Proposer une lettre")
    print("3. Donner sa langue au chat")
    print("")
    try:
        choice = (input("Entrez votre choix (1-3), choix par défaut 'Proposer une lettre' : "))
        match choice:
            case "1":
                check_word()
            case "2":
                check_letter()
            case "3":
                print ("")
                print("Vous avez choisi de donner votre langue au chat.")
                print("Le mot à deviner était : ", word_to_find)
                print("")
                print("Merci d'avoir joué ! À bientôt.") 
                exit()
            case "":
                check_letter()
            case _:
                print("Choix invalide. Veuillez choisir entre 1 et 4.")
                game_menu()
    except ValueError:
        print("Entrée invalide. Veuillez entrer un chiffre entre 1 et 4.")
        game_menu()

def show_word():
    global word_to_find, proposed_letters
    masked_word = ""
    for letter in word_to_find:
        if letter in proposed_letters:
            masked_word += letter + " "
        else:
            masked_word += "- "
    print("Mot à deviner : ", masked_word.strip())



def check_word():
    global word_to_find, errors
    print("")
    guess = input("Entrez le mot que vous pensez être le bon : ")
    if is_valid_word(guess):
        
        if guess == word_to_find:
            print("")
            print("Bravo ! Vous avez trouvé le mot !")
            print("Le mot était : ", word_to_find)
            print("")
            exit()
        else:
            print("")
            print("Désolé, ce n'est pas le bon mot.")
            errors += 1
            game_menu()
    else:
        print("")
        print("Entrée invalide. Veuillez entrer un mot valide (sans espaces et en minuscules).")
        check_word()
        
def check_letter():
    global word_to_find, errors, proposed_letters
    guess = input("Entrez une lettre : ")
    if is_valid_letter(guess):  
        if guess in proposed_letters:
            print("")
            print("Vous avez déjà proposé cette lettre.")
            check_letter()
        elif guess in word_to_find:
            print("")
            print("Bien joué ! La lettre est dans le mot.")
            proposed_letters.append(guess)
            if all(letter in proposed_letters for letter in word_to_find):
                print("")
                print("Bravo ! Vous avez trouvé le mot !")
                print("Le mot était : ", word_to_find)
                print("")
                exit()
            else : game_menu()
        else:
            print("")
            print("Désolé, la lettre n'est pas dans le mot.")
            errors += 1
            proposed_letters.append(guess)
            game_menu()
    else:
        print("Entrée invalide. Veuillez entrer une seule lettre minuscule.")
        check_letter()

def is_valid_letter(letter):
    return len(letter) == 1 and letter.isalpha() and letter.islower()

def is_valid_word(word):
    return word.isalpha() and word.islower() and " " not in word
    
    
def verify_errors():
    global errors
    if errors >= 8:
        print("Vous etes pendu !")
        show_pendu(errors)
        print("")
        print("Vous avez perdu ! Le mot était : ", word_to_find)
        main_menu()

def reset_game():
    global proposed_letters, attempts_left
    proposed_letters = []
    errors = 0
    word_to_find = ""
    main_menu()

def main_menu():
    global language, difficulty
    while True:
        show_rules()
        print("---------------------------------------")
        print("           Menu Principal")
        print("")
        print("Les paramètres du jeu sont :")
        print("")
        print(f"Langue : {language}")
        print(f"Difficulté : {difficulty}")
        print("")
        print("1. Choix de la langue du mot à trouver")
        print("2. Choix de la difficulté")
        print("3. Jouer")
        print("4. Quitter le jeu")
        print("")
        print("---------------------------------------")
        
        try:
            choice = int(input("Entrez votre choix (1-4) : "))
            match choice:
                case 1:
                    edit_language()
                case 2:
                    edit_difficulty()
                case 3:
                    generate_word()
                case 4:
                    print("")
                    print("Merci d'avoir joué ! À bientôt.")
                    print("")
                    exit()
                case _:
                    print("Choix invalide. Veuillez choisir entre 1 et 4.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un chiffre entre 1 et 4.")



def edit_difficulty():
    global difficulty, word_to_find, language
    print("")
    print("Choisissez le niveau de difficulté :")
    print("1. Facile (mots contenant jusqu'à 6 lettres)")
    print("2. Moyen" " (mots contenant jusqu'à 12 lettres)")
    print("3. Difficile (mots contenant plus de 12 lettres)")
    print("")
    try:
        choice = int(input("Entrez votre choix (1-3) : "))
        match choice:
            case 1:
                difficulty = "Facile"
                print("Difficulté choisie : Facile")
                main_menu()
            case 2:
                difficulty = "Moyen"
                print("Difficulté choisie : Moyen")
                main_menu()
            case 3:
                difficulty = "Difficile"
                print("Difficulté choisie : Difficile")
                main_menu()
            case _:
                print("Choix invalide. Veuillez choisir entre 1 et 3.")
                edit_difficulty()
        reset_game()
    except ValueError:
        print("Entrée invalide. Veuillez entrer un chiffre entre 1 et 3.")
        edit_difficulty()
def show_pendu(errors):
    stages = [
        "",
        """
           ------
                |
                |
                |
                |
                |
        """,
        """
           ------
           |    |
                |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        """
    ]
    print(stages[errors])

def generate_word():
    global word_to_find, language, difficulty
    if language == "Français":
        if difficulty == "Facile":
            word_to_find = random.choice(small_french_words)
        elif difficulty == "Moyen":
            word_to_find = random.choice(medium_french_words)
        else:
            word_to_find = random.choice(large_french_words)
    else:
        if difficulty == "Facile":
            word_to_find = random.choice(small_english_words)
        elif difficulty == "Moyen":
            word_to_find = random.choice(medium_english_words)
        else:
            word_to_find = random.choice(large_english_words)
    game_menu()
main_menu()
