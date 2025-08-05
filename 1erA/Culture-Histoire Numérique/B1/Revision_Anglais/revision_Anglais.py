import random 
import datetime


quiz = [
    {"question": "to hit the headline", "answer": "faire la une"},
    {"question": "tights", "answer": "collant"},
    {"question": "sample", "answer": "échantillon"},
    {"question": "spectacles", "answer": "glasses"},
    {"question": "municipal utilities", "answer": "stations d'épuration"},
    {"question": "compounds", "answer": "éléments chimiques"},
    {"question": "garment", "answer": "a piece of clothing"},
    {"question": "non-stick", "answer": "anti-adhérent"},
    {"question": "flocking", "answer": "flocage"},
    {"question": "cookware", "answer": "batterie de cuisine"},
    {"question": "ties", "answer": "cordons"},
    {"question": "data base", "answer": "base de données"},
    {"question": "contact lenses", "answer": "lentilles"},
    {"question": "water repellent", "answer": "déperlant"},
    {"question": "rubber", "answer": "gomme"},
    {"question": "stain resistant", "answer": "anti-taches"},
    {"question": "to be telling", "answer": "meaningful"},
    {"question": "out of sheer ignorance", "answer": "être purement ignorant"},
    {"question": "to be pig-ignorant", "answer": "être sale d'ignorance"},
    {"question": "to dwarf", "answer": "minimiser"},
    {"question": "school curriculum syllabus", "answer": "programme scolaire"},
    {"question": "asbestos", "answer": "amiante"},
    {"question": "to what extent", "answer": "dans quelle mesure"},
    {"question": "harmful", "answer": "nuisible"},
    {"question": "to some extent", "answer": "dans une certaine mesure"},
    {"question": "ubiquity", "answer": "être partout en même temps"},
    {"question": "ground water", "answer": "nappe phréatique"},
    {"question": "a landfill", "answer": "une décharge à ordures"},
    {"question": "birth defect", "answer": "malformation à la naissance"},
    {"question": "delay", "answer": "retard"},
    {"question": "to entail", "answer": "entraîner"},
    {"question": "offset", "answer": "décalage"},
    {"question": "rubbish ", "answer": "déchets"},
    {"question": "rule", "answer": "une décision"},
    {"question": "to bin", "answer": "mettre à la poubelle"},
    {"question": "a faucet ", "answer": "un robinet"},
    {"question": "pitchers", "answer": "carafes"},
    {"question": "state-of-the-art", "answer": "dernier cri"},
    {"question": "tin foil", "answer": "papier aluminium"},
    {"question": "political opponent", "answer": "opposant politique"},
    {"question": "pans and pots", "answer": "poêles et casseroles"},
    {"question": "kettle", "answer": "bouilloire"},
    {"question": "a coup", "answer": "un coup d'état"},
    {"question": "domestic appliance", "answer": "appareil ménager"},
    {"question": "electric wire", "answer": "câble électrique"},
    {"question": "coating", "answer": "revêtement"},
    {"question": "to impeach", "answer": "destituer"},
    {"question": "handle", "answer": "poignée"},
    {"question": "to curb", "answer": "freiner"},
    {"question": "to reign in", "answer": "restreindre"},
    {"question": "egg whisk", "answer": "batteur à œufs"},
    {"question": "container", "answer": "contenant"},
    {"question": "to cap", "answer": "limiter"},
    {"question": "as far as the eye can reach", "answer": "à perte de vue"},
    {"question": "work-force", "answer": "main d'œuvre"},
    {"question": "lanky", "answer": "élancé"},
    {"question": "caste system", "answer": "hiérarchie indienne "},
    {"question": "grazing", "answer": "brouter"},
    {"question": "land-owners", "answer": "propriétaires terriens"},
    {"question": "gunnysack", "answer": "sac en toile de jute"},
    {"question": "a mill", "answer": "un moulin"},
    {"question": "raw material", "answer": "matière première"},
    {"question": "to scavenge", "answer": "trier les déchets"},
    {"question": "to manufacture", "answer": "transformer la matière"},
    {"question": "added value", "answer": "valeur ajoutée"},
    {"question": "bankrupt", "answer": "banqueroute"},
    {"question": "to be behind bars", "answer": "être derrière les barreaux"},
    {"question": "Let there be light and there was light", "answer": "Que la lumière soit, et la lumière fut"},
    {"question": "down-hearted", "answer": "abattu"},
    {"question": "handcuffs", "answer": "menottes"},
    {"question": "a bowler hat", "answer": "un chapeau melon"},
    {"question": "shackle", "answer": "chaînes (grosses)"},
    {"question": "a bow tie", "answer": "un nœud papillon"},
    {"question": "a trolley = a cart", "answer": "un caddie"},
    {"question": "below the poverty line", "answer": "sous le seuil de pauvreté"},
    {"question": "absurd", "answer": "absurde"},
    {"question": "a cesspool", "answer": "fosse d'eaux usées"},
    {"question": "over-consumption", "answer": "surconsommation"},
    {"question": "consumer goods", "answer": "biens de consommation"},
    {"question": "humdrum", "answer": "routine"},
    {"question": "a well", "answer": "un puits"},
    {"question": "a can", "answer": "boîte de conserve"},
    {"question": "dishy = gorgeous", "answer": "belle à croquer"},
    {"question": "to lodge a complaint", "answer": "porter plainte"},
    {"question": "the big shot", "answer": "les types importants"},
    {"question": "the brass", "answer": "les cuivres"},
    {"question": "time", "answer": "faire passer le temps"},
    {"question": "to be pissed", "answer": "être ivre"},
    {"question": "a big shot", "answer": "un gros plan"},
    {"question": "an extreme close-up", "answer": "un très gros plan"},
    {"question": "to squander money", "answer": "gaspiller de l'argent"},
    {"question": "shopaholic", "answer": "accro au shopping"},
    {"question": "to throw money down the drain", "answer": "jeter l'argent par les fenêtres"},
    {"question": "a fizzy drink", "answer": "un soda"},
    {"question": "to tread", "answer": "fouler"},
    {"question": "a buffalo", "answer": "un bison"},
    {"question": "the red tape", "answer": "la paperasse"},
    {"question": "to wreak havoc", "answer": "saccager"},
    {"question": "to bend to someone's will", "answer": "se plier à la volonté de quelqu'un"},
    {"question": "to go on a rampage", "answer": "tout détruire par une action spécifique"},
    {"question": "to become extinct", "answer": "être en voie d'extinction"},
    {"question": "colt", "answer": "arme de cowboy"},
    {"question": "to weave", "answer": "tisser"},
    {"question": "a spoke", "answer": "un rayon"},
    {"question": "self-sufficient", "answer": "auto-suffisant"},
    {"question": "loom", "answer": "un métier à tisser"},
    {"question": "manicheistic", "answer": "manichéen"},
    {"question": "in the bottom left-hand corner", "answer": "dans le coin en bas à gauche"},
    {"question": "as if it were", "answer": "comme si c'était"},
    {"question": "the top-notch", "answer": "le meilleur"},
    {"question": "a proxy", "answer": "un mandataire"},
    {"question": "staunch supporters", "answer": "soutiens inconditionnels"},
    {"question": "the nuke", "answer": "arme nucléaire"},
    {"question": "academics", "answer": "universitaires"},
    {"question": "the scythe", "answer": "une faucille"},
    {"question": "to be indebted", "answer": "endetté"},
    {"question": "a hammer", "answer": "un marteau"},
    {"question": "civil rights movement", "answer": "droit civique"},
    {"question": "subtle", "answer": "subtile"},
    {"question": "a clenched fist", "answer": "un poing serré"},
    {"question": "tense", "answer": "tendu"},
    {"question": "the Supreme Court", "answer": "cour suprême"},
    {"question": "to sink into oblivion", "answer": "tomber dans l'oubli"},
    {"question": "corn", "answer": "maïs ou blé"},
    {"question": "to apply for", "answer": "s'inscrire"},
    {"question": "wheat", "answer": "blé"},
    {"question": "to register = to enlist", "answer": "être inscrit"},
    {"question": "maize", "answer": "maïs"},
    {"question": "cdd job", "answer": "petit boulot"},
    {"question": "sunflower oil", "answer": "huile de tournesol"},
    {"question": "unrest", "answer": "désordre"},
    {"question": "US: gas", "answer": "essence"},
    {"question": "UK: petrol", "answer": "essence"},
    {"question": "to rule", "answer": "décider"},
    {"question": "GDP", "answer": "PIB"},
    {"question": "to appoint", "answer": "nommer"},
    {"question": "GDP per capita", "answer": "PIB par habitant"},
    {"question": "a term", "answer": "un mandat"},
    {"question": "on average", "answer": "en moyenne"},
    {"question": "rigged", "answer": "truqué"},
    {"question": "to impoverish", "answer": "s'appauvrir"},
    {"question": "gun-bearing", "answer": "port d'arme"},
    {"question": "a slump", "answer": "une baisse (en économie)"},
    {"question": "CEO (Chief Executive Officer)", "answer": "PDG"},
    {"question": "tariffs", "answer": "taxes douanières"},
    {"question": "To cast a ballot", "answer": "voter"},
    {"question": "NATO (North Atlantic Treaty Organization)", "answer": "OTAN"},
    {"question": "a bone of contention", "answer": "un sujet de dispute"},
    {"question": "to retaliate", "answer": "se venger"},
    {"question": "The Congress = Senate + House of Representatives", "answer": "Le Congrès (Sénat + Chambre des représentants)"},
    {"question": "a nuclear plant", "answer": "une centrale nucléaire"},
    {"question": "blackmail", "answer": "chantage"},
    {"question": "a parson", "answer": "un pasteur"},
    {"question": "a tariff", "answer": "une taxe"},
    {"question": "interviewee", "answer": "l'interviewé"},
    {"question": "to back down", "answer": "se rétracter"},
    {"question": "a school-girl", "answer": "une écolière"},
    {"question": "a chip", "answer": "une puce électronique"},
    {"question": "to put under arrest", "answer": "mettre en état d'arrestation"},
    {"question": "protectionism", "answer": "protectionnisme"},
    {"question": "to send behind the bars", "answer": "mettre derrière les barreaux"},
    {"question": "purchasing power", "answer": "pouvoir d'achat"},
    {"question": "the turnover", "answer": "le chiffre d'affaire"},
    {"question": "to entail = to involve", "answer": "impliquer"},
      {"question": "staggering", "answer": "impressive"},
    {"question": "a TV set", "answer": "un téléviseur"},
    {"question": "prominent", "answer": "important"},
    {"question": "wield", "answer": "possess"},
    {"question": "the red necks", "answer": "les gens qui soutiennent le port d'arme"},
    {"question": "a seamstress", "answer": "une couturière"},
    {"question": "solely", "answer": "uniquement"},
    {"question": "resilience", "answer": ""},
    {"question": "murkier", "answer": "less clear"},
    {"question": "to flare up", "answer": "s'embraser"},
    {"question": "stake", "answer": "enjeu"},
    {"question": "disincentive", "answer": "dissuasion"},
    {"question": "the fare", "answer": "le prix d'un trajet"},
    {"question": "consumer society", "answer": "société de consommation"},
    {"question": "dawn", "answer": "aube"},
    {"question": "It's the last straw that breaks the camel's back", "answer": "c'est la goutte d'eau qui fait déborder le vase"},
    {"question": "autocracy", "answer": "autocratie / autoritarisme"},
    {"question": "a shelf", "answer": "une étagère / un bord"},
    {"question": "to give a testimony", "answer": "témoigner"},
    {"question": "freewheeling", "answer": "indépendant"},
    {"question": "to witness", "answer": "être témoin de"},
    {"question": "home-grown", "answer": "national"},
    {"question": "to make passes", "answer": "draguer"},
    {"question": "wired", "answer": "câblé / relié"},
    {"question": "a custom", "answer": "une coutume"},
    {"question": "shrank", "answer": "rétréci (shrink - shrank - shrunk)"},
    {"question": "a mob", "answer": "une populace"},
    {"question": "lone", "answer": "solitaire"},
    {"question": "to lynch", "answer": "pendre"},
    {"question": "dissident", "answer": "dissident / rebelle"},
    {"question": "to be acquitted", "answer": "être acquitté"},
    {"question": "sheer scope", "answer": "l'étendue (des données)"},
    {"question": "a turntable", "answer": "un tourne-disque"},
    {"question": "social unrest / disorder", "answer": "désordre social"},
    {"question": "ill-at-ease", "answer": "mal à l'aise"},
    {"question": "to stir unrest", "answer": "provoquer des troubles"},
    {"question": "a mayor", "answer": "un maire"},
    {"question": "to disrupt", "answer": "perturber"},
    {"question": "a record", "answer": "un disque vinyle"},
    {"question": "the World Happiness Report", "answer": "Rapport mondial sur le bonheur"},
    {"question": "content", "answer": "contenu"},
    {"question": "to abide by the law", "answer": "respecter la loi"},
    {"question": "a law-abiding citizen", "answer": "un citoyen respectueux de la loi"},
    {"question": "a slaughter", "answer": "un massacre"},
    {"question": "to stutter / stammer", "answer": "bégayer"},
    {"question": "humankind", "answer": "l'espèce humaine"},
    {"question": "a mike", "answer": "un micro"},
    {"question": "evidence", "answer": "une preuve"},
    {"question": "to hold a meeting", "answer": "tenir une conférence"},
    {"question": "proof of the pudding", "answer": "la preuve du pudding"},
    {"question": "to draft an amendment", "answer": "rédiger un amendement"},
    {"question": "a meltdown", "answer": "la fonte"},
    {"question": "a hood", "answer": "une cagoule"},
    {"question": "a fee", "answer": "frais d'inscription"},
    {"question": "The Confederate flag", "answer": "Drapeau de la Confédération (armée du Sud des USA)"},
    {"question": "a scholarship = a grant", "answer": "une bourse"},
    {"question": "to get on a bus", "answer": "prendre le bus"},
    {"question": "a loan from the bank", "answer": "un prêt à la banque"},
    {"question": "to run into debts", "answer": "s'endetter"},
    {"question": "to reimburse = to pay back", "answer": "rembourser"},
    {"question": "lithium", "answer": ""},
    {"question": "The World Trade Organisation", "answer": "Traité"},
    {"question": "trench warfare", "answer": "guerre des tranchées"},
    {"question": "to retaliate", "answer": "en guise de représailles"},
    {"question": "a tramp", "answer": "un vagabond"},
    {"question": "commercial", "answer": "pub à la TV"},
    {"question": "a hardship", "answer": "une épreuve"},
    {"question": "publicity", "answer": "domaine publicitaire"},
    {"question": "misled", "answer": "trompé"},
    {"question": "shamrock", "answer": "trèfle de la Saint Patrick"},
    {"question": "a milestone / a landmark", "answer": "une grande étape"},
    {"question": "to be as happy as a rabbit in a clover field", "answer": "être heureux comme un poisson dans l'eau"},
    {"question": "homesickness", "answer": "mal du pays"},
    {"question": "a cliff", "answer": "une falaise"},
    {"question": "to be well thought-of", "answer": "être bien vu"},
    {"question": "top hat", "answer": "chapeau haut de forme"},
    {"question": "to be ill-thought-of", "answer": "être mal vu"},
    {"question": "destitute", "answer": "indigent"},
    {"question": "RP (Received Pronunciation)", "answer": "Queen's English"},
    {"question": "to be in a predicament", "answer": "une situation sans issue"},
    {"question": "rye", "answer": "seigle"},
    {"question": "a plain Jane", "answer": "laide comme un poux"},
    {"question": "paddy", "answer": "surnom méchant irlandais"},
    {"question": "a Jack-of-all-trades", "answer": "un touche-à-tout"},
    {"question": "battle dress", "answer": "treillis de l'armée"},
    {"question": "prejudices", "answer": "préjugés"},
    {"question": "Northern Ireland", "answer": "Ulster"},
    {"question": "a banshee", "answer": "sorcière / hurlement"},
    {"question": "Irish Republic (southern)", "answer": "Eire / Erin"},
    {"question": "governance", "answer": "administration"},
    {"question": "to be stranded", "answer": "être naufragé"},
    {"question": "tit-for-tat", "answer": "du tac au tac"},
    {"question": "bitterness", "answer": "amertume"},
    {"question": "to stretch over", "answer": "s'étendre sur"},
    {"question": "Whitehall", "answer": "quartier des ministères"},
    {"question": "An eye for an eye, a tooth for a tooth", "answer": "œil pour œil, dent pour dent"},
    {"question": "a machine gun", "answer": "une mitraillette"},
    {"question": "Westminster", "answer": "Parlement britannique"},
    {"question": "barbed wire", "answer": "fil barbelé"},
    {"question": "to be locked up in jail", "answer": "être enfermé en prison"},
    {"question": "cannon fodder", "answer": "chair à canon"},
    {"question": "to hero-worship", "answer": "culte des héros"},
    {"question": "blackmail", "answer": "chantage"},
    {"question": "rifle", "answer": "fusil"},
    {"question": "10 Downing Street", "answer": "Premier ministre britannique"},
    {"question": "WASPs (White Anglo-Saxon Protestants)", "answer": "Protestants anglo-saxons blancs"},
    {"question": "a shell", "answer": "un obus"},
    {"question": "U-boat", "answer": "sous-marin allemand"},
    {"question": "to snipe", "answer": "tirer en étant embusqué"},
    {"question": "a convict", "answer": "un prisonnier"},
    {"question": "a trigger", "answer": "une gâchette"},
    {"question": "a parson", "answer": "pasteur"},
    {"question": "Sinn Féin", "answer": "journal gaélique / parti politique"},
    {"question": "ruthless", "answer": "impitoyable"},
    {"question": "to scuttle", "answer": "saborder son propre bateau"},
    {"question": "to ambush", "answer": "tendre une embuscade"},
    {"question": "to brood", "answer": "couver"},{"question": "a tenant", "answer": "an owner"},
    {"question": "sorrowful", "answer": "triste +++"},
    {"question": "wistful", "answer": "mélancolie / nostalgie"},
    {"question": "pristine", "answer": "immaculé"},
    {"question": "deoraí", "answer": "forced immigration"},
    {"question": "eisimircí", "answer": "voluntary immigration"},
    {"question": "to say farewell", "answer": "dire adieu"},
    {"question": "secluded", "answer": "isolé"},
    {"question": "a fungus", "answer": "un champignon (maladie)"},
    {"question": "mushrooms", "answer": "champignons"},
    {"question": "to sack", "answer": "piller"},
    {"question": "a tung", "answer": "un pain"},
    {"question": "a lore", "answer": "une légende / tradition"},
    {"question": "a dirge", "answer": "une lamentation"},
    {"question": "a thatched cottage", "answer": "maison en chaume"},
    {"question": "a shack", "answer": "délabré"},
    {"question": "a mass grave", "answer": "une fosse commune"},
    {"question": "a hamlet", "answer": "un hameau"},
    {"question": "a casket", "answer": "un cercueil"},
    {"question": "armored cars", "answer": "voitures blindées"},
    {"question": "top-level talk", "answer": "discussion de haut niveau"},
    {"question": "a dominion", "answer": ""},
    {"question": "the customs", "answer": "la douane"},
    {"question": "the sub-plot", "answer": "intrigue secondaire"},
    {"question": "a boarding house", "answer": "une pension de famille"},
    {"question": "a shop assistant", "answer": "une vendeuse"},
    {"question": "a lodging", "answer": "un logement"},
    {"question": "a community hall", "answer": "une salle des fêtes pour une communauté"},
    {"question": "On Danny Boy", "answer": "chanson funèbre irlandaise"},
    {"question": "to mourn", "answer": "porter le deuil"},
    {"question": "witchcraft", "answer": "sorcellerie"},
    {"question": "to snag", "answer": "il y a un os"},
    {"question": "shears", "answer": "cisailles"},
    {"question": "a tinkle bell", "answer": "une clochette"},
    {"question": "to give someone shivers", "answer": "donner la chair de poule"},
    {"question": "to bang a door", "answer": "claquer la porte"},
    {"question": "to deal blows", "answer": "donner des coups"},
    {"question": "a law enforcement officer", "answer": "un représentant de la loi"},
    {"question": "a police constable", "answer": "un agent de police"},
    {"question": "to lurk in the shadows", "answer": "se cacher dans l'ombre"},
    {"question": "devoid of", "answer": "privé de"},
    {"question": "to spill the beans / to let the cat out of the bag", "answer": "révéler un secret"},
    {"question": "young and dashing", "answer": "des beaux jeunes gens"},
    {"question": "to have a paunch", "answer": "avoir un petit ventre"},
    {"question": "to have a beer belly", "answer": "avoir un bide"},
    {"question": "a patron", "answer": "un habitué du bar"},
    {"question": "an oath", "answer": "un serment"},
    {"question": "to shush someone", "answer": "faire taire"},
    {"question": "to pledge", "answer": "promettre"},
    {"question": "to cast a spell", "answer": "jeter un sort"},
    {"question": "a shite", "answer": "une merde"},
    {"question": "to give the finger", "answer": "faire un doigt"},
    {"question": "an old bachelor", "answer": "un vieux garçon"},
    {"question": "a spinster", "answer": "une vieille fille"},
    {"question": "an apron", "answer": "un tablier"},
    {"question": "trivial / trite", "answer": "banal"},
    {"question": "blissful", "answer": "béat / heureux"},
    {"question": "to hoot", "answer": "klaxonner"},
    {"question": "a block of flats", "answer": "un immeuble (HLM)"},
    {"question": "to be secluded", "answer": "être isolé"},
    {"question": "the beacon", "answer": "la lumière du phare"},
    {"question": "a lighthouse", "answer": "un phare"},
    {"question": "a light bull", "answer": "une ampoule"}
]


number_questions = 10 
mode_de_jeu = "Hybride"


    

def play_quiz():
    global quiz, number_questions, mode_de_jeu
    print("----------------------------------------------------")
    print("                Lancer le quiz")
    print("")
    pseudo = input("Entrez votre pseudo : ").strip()
    if not pseudo:
        print("Le pseudo ne peut pas être vide.")
        play_quiz()
    print("")
    questions_du_quiz = random.sample(quiz, min(number_questions, len(quiz)))
    
    score = 0
    for compteur,ligne in enumerate(questions_du_quiz,1):
        if mode_de_jeu == "Hybride":
            if compteur % 2 == 0:
                print("")
                print(f"Question {compteur} (Anglais => Français) : {ligne['question']}")
                reponse = input("Entrez votre réponse : ").strip().lower()
                if reponse == ligne["answer"].lower():
                    print("Correct !")
                    score += 1
                else:
                    print(f"Incorrect ! La bonne réponse est : {ligne['answer']}")
            else:
                print("")
                print(f"Question {compteur} (Français => Anglais) : {ligne['answer']}")
                reponse = input("Entrez votre réponse : ").strip().lower()
                if reponse == ligne["question"].lower():
                    print("Correct !")
                    score += 1
                else:
                    print(f"Incorrect ! La bonne réponse est : {ligne['question']}")
        elif mode_de_jeu == "Traduction Anglais => Français":
            print("")
            print(f"Question {compteur} (Anglais => Français) : {ligne['question']}")
            reponse = input("Entrez votre réponse : ").strip().lower()
            if reponse == ligne["answer"].lower():
                print("Correct !")
                score += 1
            else:
                print(f"Incorrect ! La bonne réponse est : {ligne['answer']}")
        elif mode_de_jeu == "Traduction Français => Anglais":
            print("")
            print(f"Question {compteur} (Français => Anglais) : {ligne['answer']}")
            reponse = input("Entrez votre réponse : ").strip().lower()
            if reponse == ligne["question"].lower():
                print("Correct !")
                score += 1
            else:
                print(f"Incorrect ! La bonne réponse est : {ligne['question']}")
        
    score_pourcentage = (score / min(number_questions,len(quiz))) * 100
    print("")
    print("Quizz terminé !")
    print(f"Votre score est de {score} sur {min(number_questions,len(quiz))}.")
    print("----------------------------------------------------")
    
    sauvegarder_resultats(pseudo, round(score_pourcentage,2))
    menu_principal()
            

def menu_principal():
    while True: 
        print("----------------------------------------------------")
        print("                Menu principal")
        print("")
        print(" Reglages du quiz : ")
        print(" Nombre de questions : ", number_questions)
        print(" Mode de jeu : ", mode_de_jeu)
        print("")
        print("----------------------------------------------------")
        print("Que souhaitez-vous faire ? ")
        print("")
        print("1. Modifier le nombre de questions du quiz")
        print("2. Modifier le mode de jeu")
        print("3. Afficher mes résultats")
        print("4. Lancer le quiz")
        print("5. Quitter")
        print("")
        
        choix = int(input("Entrez votre choix (1-5) : "))
        match choix:
            case 1: 
                modifier_nombre_questions()
            case 2:
                modifier_mode_de_jeu()
            case 3:
                afficher_resultats()
            case 4:
                play_quiz()
            case 5:
                print("")
                print("Merci d'avoir joué ! À bientôt !")
                print
                exit()
            case _: 
                print("Choix invalide. Veuillez choisir entre 1 et 5.")
                menu_principal()
        
        
def modifier_nombre_questions():
    global number_questions
    print("----------------------------------------------------")
    print("    Modifier le nombre de questions du quiz")
    print("")
    print(f"Le nombre actuel de questions est de {number_questions}.")
    print("")
    print("Combien de questions souhaitez-vous avoir dans le quiz ?")
    choix = int(input("Entrez un nombre entre 1 et 100: "))
    if choix < 1 or choix > 100:
        print("")
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 100.")
    else:
        number_questions = choix
        menu_principal()
    
    
def modifier_mode_de_jeu():
    global mode_de_jeu
    print("----------------------------------------------------")
    print("           Modifier le mode de jeu")
    print("")
    print(f"Le mode de jeu actuel est : {mode_de_jeu}.")
    print("")
    print("Quel mode de jeu souhaitez-vous choisir ?")
    print("")
    print("1. Hybride")
    print("2. Traduction Anglais => Français")
    print("3. Traduction Français => Anglais")
    print("")
    choix = int(input("Entrez votre choix (1-3) : "))
    match choix:
        case 1:
            mode_de_jeu = "Hybride"
            menu_principal()
        case 2:
            mode_de_jeu = "Traduction Anglais => Français"
            menu_principal()
        case 3:
            mode_de_jeu = "Traduction Français => Anglais"
            menu_principal()
        case _:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 3.")
            modifier_mode_de_jeu()
            
            
            
def afficher_resultats():
    print("----------------------------------------------------")
    print("                Mes résultats")
    print("")
    try :
        with open("resultats.txt", "r") as file:
            resultats = file.readlines()
            if not resultats:
                print("Aucun résultat enregistré.")
            else:
                print("Vos résultats :")
                for ligne in resultats:
                    print(ligne.strip())
    except FileNotFoundError:
        print("Aucun résultat enregistré.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier des résultats : {e}")
        
    print("----------------------------------------------------")
    print("Appuyez sur Entrée pour retourner au menu principal.")
    input()
    menu_principal()
    
    
def sauvegarder_resultats(pseudo,score_pourcentage):
    date_du_test = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("resultats.txt", "a") as file:
        file.write(f"{pseudo} - {score_pourcentage}% - {date_du_test}\n")
    print("Résultats sauvegardés avec succès.")
    print("----------------------------------------------------")
    print("")
    menu_principal()
    
    
    
menu_principal()
    
    
 
 
 
 

