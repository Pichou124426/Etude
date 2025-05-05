# Script de révision QCM interactif

questions = [
    {
        "question": "Quel était le premier téléphone portable commercialisé ?",
        "choix": ["Nokia 3310", "Motorola DynaTAC 8000X", "iPhone 3G", "Samsung Galaxy S"],
        "reponse": "Motorola DynaTAC 8000X"
    },
    {
        "question": "En quelle année a été lancé le premier iPhone ?",
        "choix": ["2005", "2007", "2009", "2010"],
        "reponse": "2007"
    },
    {
        "question": "Quel est le nom du système d'exploitation mobile développé par Google ?",
        "choix": ["iOS", "Windows Mobile", "Android", "Symbian"],
        "reponse": "Android"
    },
    {
        "question": "Quel est le nom du premier smartphone à écran tactile capacitif ?",
        "choix": ["BlackBerry", "Nokia N95", "iPhone", "HTC Dream"],
        "reponse": "iPhone"
    },
    {
        "question": "Quel est le nom de la technologie permettant de réaliser des paiements sans contact avec un smartphone ?",
        "choix": ["NFC", "QR Code", "Bluetooth", "Wi-Fi"],
        "reponse": "NFC"
    },]
 
questions.extend([
    {
        "question": "Quelle entreprise a été la première à intégrer le TouchPad dans ses ordinateurs portables ?",
        "choix": ["Apple", "Olivetti", "HP", "Compaq"],
        "reponse": "Apple"
    },
    {
        "question": "Quel équipement était censé provoquer la 'mort du PC' ?",
        "choix": ["Le smartphone", "Le PDA", "La tablette tactile", "Le SaaS"],
        "reponse": "La tablette tactile"
    },
    {
        "question": "Quelle technologie a permis de développer la téléphonie mobile ?",
        "choix": ["1G", "2G", "3G"],
        "reponse": "1G"
    },
    {
        "question": "Quel est le premier appareil permettant d’écouter de la musique en se déplaçant ?",
        "choix": ["Le smartphone", "Le Walkman", "Le Discman", "Le baladeur MP3"],
        "reponse": "Le Walkman"
    },
    {
        "question": "Qu’est-ce que l’Internet des Objets (IoT) ?",
        "choix": [
            "Un réseau de personnes connectées",
            "Un réseau d’appareils physiques connectés à Internet",
            "Un type de logiciel de gestion de données",
            "Un protocole de communication sans fil"
        ],
        "reponse": "Un réseau d’appareils physiques connectés à Internet"
    },
    {
        "question": "Quel est le principal avantage des applications SaaS pour les utilisateurs ?",
        "choix": [
            "Réduction des coûts de matériel",
            "Accès à des logiciels à jour depuis n’importe où",
            "Augmentation des ventes",
            "Réduction du personnel"
        ],
        "reponse": "Accès à des logiciels à jour depuis n’importe où"
    },
    {
        "question": "Sur quelle technologie s’appuie le réseau cellulaire de téléphonie ?",
        "choix": ["Le satellite", "Le Wi-Fi", "Les ondes hertziennes", "Le Bluetooth"],
        "reponse": "Les ondes hertziennes"
    },
    {
        "question": "Pour quelle raison existe-t-il encore des cabines téléphoniques en France ?",
        "choix": [
            "Pour joindre les secours en zone blanche",
            "Pour attirer des touristes",
            "Parce qu’elles ont été oubliées par Orange",
            "Pour leur design d’avant-garde"
        ],
        "reponse": "Pour joindre les secours en zone blanche"
    },
    {
        "question": "Quel est le principal service de données introduit par la 2G ?",
        "choix": ["MMS", "SMS", "Internet mobile", "VoIP"],
        "reponse": "SMS"
    },
    {
        "question": "Quel est le nom du standard de la 4G ?",
        "choix": ["LTE", "UMTS", "GSM", "EDGE"],
        "reponse": "LTE"
    }
])

# Ajout des 20 nouvelles questions

questions.extend([
    {
        "question": "Quel était le nom du premier réseau informatique ?",
        "choix": ["ARPANET", "NSFNET", "INTERNET", "MILNET"],
        "reponse": "ARPANET"
    },
    {
        "question": "Qui a inventé le World Wide Web ?",
        "choix": ["Vint Cerf", "Tim Berners-Lee", "Larry Page", "Mark Zuckerberg"],
        "reponse": "Tim Berners-Lee"
    },
    {
        "question": "Quel est le nom du premier service de messagerie instantanée ?",
        "choix": ["WhatsApp", "MSN Messenger", "ICQ", "Skype"],
        "reponse": "ICQ"
    },
    {
        "question": "Quel est le nom du premier site de commerce électronique ?",
        "choix": ["Amazon", "eBay", "Alibaba", "Craigslist"],
        "reponse": "Amazon"
    },
    {
        "question": "Quel protocole de communication a été développé pour ARPANET ?",
        "choix": ["TCP/IP", "HTTP", "FTP", "SMTP"],
        "reponse": "TCP/IP"
    },
    {
        "question": "Quel pays a développé le réseau Cyclades ?",
        "choix": ["États-Unis", "France", "Royaume-Uni", "Allemagne"],
        "reponse": "France"
    },
    {
        "question": "Quel réseau a succédé à ARPANET pour devenir le backbone de l'Internet moderne ?",
        "choix": ["NSFNET", "BITNET", "MILNET", "INTERNET2"],
        "reponse": "NSFNET"
    },
    {
        "question": "Quel était l'objectif principal du Minitel ?",
        "choix": [
            "Fournir des services de messagerie instantanée",
            "Offrir des services de vidéoconférence",
            "Permettre l'accès à des services en ligne",
            "Diffuser des vidéos en streaming"
        ],
        "reponse": "Permettre l'accès à des services en ligne"
    },
    {
        "question": "Quel réseau a été préféré à Cyclades en France ?",
        "choix": ["Internet", "Ethernet", "Transpac", "Compuserve"],
        "reponse": "Transpac"
    },
    {
        "question": "Qu'est-ce que la convergence numérique ?",
        "choix": [
            "La fusion des technologies de l'information et de la communication",
            "La séparation des technologies de l'information et de la communication",
            "L'augmentation de la vitesse des réseaux",
            "La réduction des coûts des technologies"
        ],
        "reponse": "La fusion des technologies de l'information et de la communication"
    },
    {
        "question": "Lequel des éléments suivants est un exemple de convergence numérique ?",
        "choix": ["Un téléphone fixe", "Un smartphone", "Une télévision analogique", "Une radio FM"],
        "reponse": "Un smartphone"
    },
    {
        "question": "Quel est un défi de la convergence numérique ?",
        "choix": [
            "La réduction des coûts",
            "L'augmentation de la vitesse des réseaux",
            "La facilité d'utilisation",
            "La sécurité des données"
        ],
        "reponse": "La sécurité des données"
    },
    {
        "question": "Quel secteur a été le moins transformé par la convergence numérique ?",
        "choix": ["L'agriculture", "La finance", "Les médias", "L'éducation"],
        "reponse": "L'agriculture"
    },
    {
        "question": "Lequel des éléments suivants est un exemple de convergence numérique dans le divertissement ?",
        "choix": ["Les cassettes VHS", "Les plateformes de streaming", "Les disques vinyles", "Les radios FM"],
        "reponse": "Les plateformes de streaming"
    },
    {
        "question": "Quel est le nom du réseau utilisé pour connecter des ordinateurs dans une entreprise ou une organisation ?",
        "choix": ["WAN", "LAN", "MAN", "PAN"],
        "reponse": "LAN"
    },
    {
        "question": "Quel est le nom du réseau qui couvre une grande zone géographique, comme un pays ou un continent ?",
        "choix": ["WAN", "LAN", "MAN", "PAN"],
        "reponse": "WAN"
    },
    {
        "question": "Quel type de réseau permet aux employés de travailler à distance en accédant aux ressources internes de l'entreprise ?",
        "choix": ["LAN", "Extranet", "Intranet", "WAN"],
        "reponse": "Extranet"
    },
    {
        "question": "Quel type de réseau est utilisé pour les communications internes au sein d'une organisation ?",
        "choix": ["WAN", "Extranet", "Intranet", "LAN"],
        "reponse": "Intranet"
    },
    {
        "question": "Quel est le rôle principal d'un modem ?",
        "choix": [
            "Convertir les signaux numériques en signaux analogiques et vice versa",
            "Stocker des données",
            "Protéger les réseaux contre les virus",
            "Gérer les adresses IP"
        ],
        "reponse": "Convertir les signaux numériques en signaux analogiques et vice versa"
    },
    {
        "question": "Quel est le service de streaming vidéo appartenant à Google ?",
        "choix": ["Netflix", "Hulu", "YouTube", "Disney+"],
        "reponse": "YouTube"
    }
])

# Ajout des 20 nouvelles questions

questions.extend([
    {
        "question": "Qui est considéré comme le père de l'informatique moderne ?",
        "choix": ["Alan Turing", "Charles Babbage", "John von Neumann", "Bill Gates"],
        "reponse": "Alan Turing"
    },
    {
        "question": "Quel était le nom du premier ordinateur électronique programmable ?",
        "choix": ["UNIVAC", "Colossus", "ENIAC", "IBM 701"],
        "reponse": "ENIAC"
    },
    {
        "question": "Qui a développé le premier système d'exploitation UNIX ?",
        "choix": ["Bill Gates", "Steve Jobs", "Ken Thompson et Dennis Ritchie", "Linus Torvalds"],
        "reponse": "Ken Thompson et Dennis Ritchie"
    },
    {
        "question": "Quel était le nom du premier ordinateur personnel commercialisé par IBM ?",
        "choix": ["IBM PC", "IBM 5100", "IBM System/360", "IBM ThinkPad"],
        "reponse": "IBM PC"
    },
    {
        "question": "Qui a fondé Microsoft ?",
        "choix": ["Steve Jobs", "Bill Gates et Paul Allen", "Larry Page et Sergey Brin", "Mark Zuckerberg"],
        "reponse": "Bill Gates et Paul Allen"
    },
    {
        "question": "Quel était le nom du premier navigateur web ?",
        "choix": ["Internet Explorer", "Netscape Navigator", "NSCA Mosaic", "Firefox"],
        "reponse": "NSCA Mosaic"
    },
    {
        "question": "Qui est l'inventeur du World Wide Web ?",
        "choix": ["Tim Berners-Lee", "Vint Cerf", "Robert Kahn", "Marc Andreessen"],
        "reponse": "Tim Berners-Lee"
    },
    {
        "question": "Qui a construit la première machine à calculer mécanique, capable d'effectuer des additions et soustractions ?",
        "choix": ["Charles Babbage", "Gottfried Wilhelm Leibniz", "Blaise Pascal", "Joseph-Marie Jacquard"],
        "reponse": "Blaise Pascal"
    },
    {
        "question": "Qui a fondé Apple Inc. ?",
        "choix": ["Steve Jobs et Steve Wozniak", "Bill Gates et Paul Allen", "Larry Page et Sergey Brin", "Mark Zuckerberg"],
        "reponse": "Steve Jobs et Steve Wozniak"
    },
    {
        "question": "Quel fut le premier navigateur web populaire ?",
        "choix": ["Internet Explorer", "Mozilla Firefox", "Netscape Navigator", "Safari"],
        "reponse": "Netscape Navigator"
    },
    {
        "question": "Quel est le nom du système d'exploitation open source basé sur Linux ?",
        "choix": ["Windows", "macOS", "Ubuntu", "iOS"],
        "reponse": "Ubuntu"
    },
    {
        "question": "Quel est le nom du navigateur web développé par Google ?",
        "choix": ["Firefox", "Safari", "Edge", "Chrome"],
        "reponse": "Chrome"
    },
    {
        "question": "Quel est le nom de l'ordinateur développé par Apple en 1984 qui a popularisé l'interface graphique ?",
        "choix": ["Apple II", "Macintosh", "Lisa", "Newton"],
        "reponse": "Macintosh"
    },
    {
        "question": "Quel est le nom du réseau social fondé par Mark Zuckerberg en 2004 ?",
        "choix": ["Twitter", "LinkedIn", "Facebook", "Instagram"],
        "reponse": "Facebook"
    },
    {
        "question": "Quel est le nom du service de messagerie électronique lancé par Google en 2004 ?",
        "choix": ["Yahoo Mail", "Outlook", "Gmail", "Hotmail"],
        "reponse": "Gmail"
    },
    {
        "question": "Quel est le nom de la technologie de paiement mobile développée par Apple ?",
        "choix": ["Google Pay", "Samsung Pay", "Apple Pay", "PayPal"],
        "reponse": "Apple Pay"
    },
    {
        "question": "Quel est le nom du premier système d'exploitation développé par Microsoft ?",
        "choix": ["Windows 1.0", "MS-DOS", "Windows 95", "OS/2"],
        "reponse": "MS-DOS"
    },
    {
        "question": "Quel est le nom du premier réseau social professionnel lancé en 2003 ?",
        "choix": ["LinkedIn", "Facebook", "Twitter", "MySpace"],
        "reponse": "LinkedIn"
    },
    {
        "question": "Quel est le nom du premier ordinateur personnel à succès commercialisé par Commodore en 1982 ?",
        "choix": ["Commodore 64", "Commodore PET", "Commodore VIC-20", "Commodore Amiga"],
        "reponse": "Commodore 64"
    },
    {
        "question": "Quel était le nom du premier micro-ordinateur développé en France ?",
        "choix": ["Micral", "Mitra 15", "Apple I", "Altair 8800"],
        "reponse": "Micral"
    }
])

# Ajout des 20 nouvelles questions

questions.extend([
    {
        "question": "Qui est considéré comme le premier programmeur informatique ?",
        "choix": ["Alan Turing", "Ada Lovelace", "Charles Babbage", "John von Neumann"],
        "reponse": "Ada Lovelace"
    },
    {
        "question": "Quel langage de programmation est connu pour être le premier langage de haut niveau ?",
        "choix": ["COBOL", "C", "Pascal", "FORTRAN"],
        "reponse": "FORTRAN"
    },
    {
        "question": "Quel langage de programmation est principalement utilisé pour le développement web côté serveur ?",
        "choix": ["JavaScript", "HTML", "PHP", "CSS"],
        "reponse": "PHP"
    },
    {
        "question": "Quel langage de programmation est utilisé pour les bases de données relationnelles ?",
        "choix": ["NOSQL", "SQL", "HTML", "XML"],
        "reponse": "SQL"
    },
    {
        "question": "Quel langage de programmation est utilisé pour le développement de l'intelligence artificielle et l'apprentissage automatique ?",
        "choix": ["JavaScript", "Python", "PHP", "Ruby"],
        "reponse": "Python"
    },
    {
        "question": "Quel langage de programmation est utilisé pour le développement de l'interface utilisateur avec jQuery ?",
        "choix": ["Python", "C++", "JavaScript", "Ruby"],
        "reponse": "JavaScript"
    },
    {
        "question": "Quel langage de programmation a été créé par Grace Hopper en 1959 ?",
        "choix": ["COBOL", "FORTRAN", "LISP", "BASIC"],
        "reponse": "COBOL"
    },
    {
        "question": "Quel langage de programmation a été développé par John Backus en 1957 ?",
        "choix": ["BASIC", "LISP", "FORTRAN", "COBOL"],
        "reponse": "FORTRAN"
    },
    {
        "question": "Qui est considéré comme le père de l'algorithmique moderne ?",
        "choix": ["Alan Turing", "Donald Knuth", "John von Neumann", "Al-Khwârizmî"],
        "reponse": "Al-Khwârizmî"
    },
    {
        "question": "Quel est l'objectif principal de l'algorithme d'Euclide ?",
        "choix": [
            "Trouver le plus court chemin dans un graphe",
            "Trier un tableau",
            "Calculer le plus grand commun diviseur (PGCD)",
            "Résoudre le problème du sac à dos"
        ],
        "reponse": "Calculer le plus grand commun diviseur (PGCD)"
    },
    {
        "question": "Quel mathématicien grec proposa le premier un algorithme pour le calcul de π ?",
        "choix": ["Pythagore", "Euclide", "Thalès", "Archimède"],
        "reponse": "Archimède"
    },
    {
        "question": "Avec quel mathématicien Ada Lovelace a-t-elle collaboré sur la machine analytique ?",
        "choix": ["Alan Turing", "John von Neumann", "Charles Babbage", "George Boole"],
        "reponse": "Charles Babbage"
    },
    {
        "question": "Quel concept informatique Ada Lovelace a-t-elle introduit dans son algorithme pour l'Analytical Engine ?",
        "choix": ["Les structures de données", "Les boucles conditionnelles", "Les réseaux neuronaux", "Les bases de données"],
        "reponse": "Les boucles conditionnelles"
    },
    {
        "question": "Quel langage fut le premier à implémenter le paradigme de l'orienté objet ?",
        "choix": ["C++", "Simula 67", "FORTRAN", "Python"],
        "reponse": "Simula 67"
    },
    {
        "question": "Quel langage de programmation a été créé par Bjarne Stroustrup ?",
        "choix": ["Java", "Python", "Ruby", "C++"],
        "reponse": "C++"
    },
    {
        "question": "Quel langage est le plus adapté pour traiter facilement de l'information de type texte ?",
        "choix": ["Perl", "Java", "Python", "PHP"],
        "reponse": "Perl"
    },
    {
        "question": "Quel langage a pour ambition de remplacer le C et le C++ ?",
        "choix": ["Go", "SQL", "Rust", "HTML"],
        "reponse": "Go"
    },
    {
        "question": "Quel langage est reconnu pour son efficacité en intelligence artificielle ?",
        "choix": ["Python", "Java", "C", "COBOL"],
        "reponse": "Python"
    },
    {
        "question": "Quel langage de programmation est utilisé pour le développement de logiciels embarqués ?",
        "choix": ["JavaScript", "Python", "C", "PHP"],
        "reponse": "C"
    },
    {
        "question": "Quel langage de programmation est utilisé pour les scripts shell sous Unix/Linux ?",
        "choix": ["Python", "Bash", "Perl", "Ruby"],
        "reponse": "Bash"
    }
])

# Ajout des 20 nouvelles questions sur les jeux vidéo

questions.extend([
    {
        "question": "Quelle est la première console de jeux vidéo commercialisée ?",
        "choix": ["Atari 2600", "Magnavox Odyssey", "Nintendo Entertainment System (NES)", "Sega Genesis"],
        "reponse": "Magnavox Odyssey"
    },
    {
        "question": "En quelle année est sortie la console Atari 2600 ?",
        "choix": ["1972", "1977", "1983", "1985"],
        "reponse": "1977"
    },
    {
        "question": "Quelle console a popularisé les jeux vidéo dans les foyers dans les années 1980 ?",
        "choix": ["Atari 2600", "Magnavox Odyssey", "Nintendo Entertainment System (NES)", "Sega Genesis"],
        "reponse": "Nintendo Entertainment System (NES)"
    },
    {
        "question": "Quelle console a été la première à utiliser des cartouches interchangeables ?",
        "choix": ["Atari 2600", "Magnavox Odyssey", "Nintendo Entertainment System (NES)", "Intellivision"],
        "reponse": "Atari 2600"
    },
    {
        "question": "Quelle console est souvent considérée comme la première console de jeux vidéo portable ?",
        "choix": ["Game Boy", "Atari Lynx", "Sega Game Gear", "TurboExpress"],
        "reponse": "Game Boy"
    },
    {
        "question": "En quelle année est sortie la PlayStation originale de Sony ?",
        "choix": ["1993", "1994", "1995", "1996"],
        "reponse": "1994"
    },
    {
        "question": "Quelle console a introduit le jeu 'The Legend of Zelda: Ocarina of Time' ?",
        "choix": ["Super Nintendo Entertainment System (SNES)", "Nintendo 64", "GameCube", "Wii"],
        "reponse": "Nintendo 64"
    },
    {
        "question": "Quelle console a été la première à offrir des graphismes en haute définition (HD) ?",
        "choix": ["PlayStation 2", "Xbox", "Xbox 360", "PlayStation 3"],
        "reponse": "Xbox 360"
    },
    {
        "question": "Quelle console a été la première à offrir un service de jeu en ligne ?",
        "choix": ["Sega Dreamcast", "PlayStation 2", "Xbox", "GameCube"],
        "reponse": "Sega Dreamcast"
    },
    {
        "question": "Quelle console a introduit le jeu 'Halo: Combat Evolved' ?",
        "choix": ["PlayStation 2", "Xbox", "GameCube", "Sega Dreamcast"],
        "reponse": "Xbox"
    },
    {
        "question": "Quelle console a été la première à inclure des manettes sans fil de série ?",
        "choix": ["PlayStation 2", "Xbox", "GameCube", "Wii"],
        "reponse": "Wii"
    },
    {
        "question": "Quel jeu est encore aujourd'hui le produit le mieux noté de l'histoire des jeux vidéo ?",
        "choix": ["Half-Life", "Metal Gear Solid", "The Legend of Zelda: Ocarina of Time", "Tomb Raider"],
        "reponse": "The Legend of Zelda: Ocarina of Time"
    },
    {
        "question": "Quelle console a été la première à offrir un abonnement de jeux en ligne ?",
        "choix": ["PlayStation 2", "Xbox", "Xbox 360", "PlayStation 3"],
        "reponse": "Xbox"
    },
    {
        "question": "Quelle console a été la première à inclure un écran tactile ?",
        "choix": ["Nintendo DS", "PlayStation Portable (PSP)", "Game Boy Advance", "Sega Nomad"],
        "reponse": "Nintendo DS"
    },
    {
        "question": "Quel est le premier jeu mobile jamais créé ?",
        "choix": ["Snake", "Tetris", "Pong", "Space Invaders"],
        "reponse": "Snake"
    },
    {
        "question": "En quelle année le jeu 'Snake' a-t-il été introduit sur les téléphones Nokia ?",
        "choix": ["1994", "1997", "2000", "2003"],
        "reponse": "1997"
    },
    {
        "question": "Quel jeu mobile a été le premier à utiliser la réalité augmentée (AR) ?",
        "choix": ["Ingress", "Harry Potter: Wizards Unite", "Pokémon GO", "Minecraft Earth"],
        "reponse": "Pokémon GO"
    },
    {
        "question": "Quel jeu mobile a été le premier à inclure un mode multijoueur en ligne ?",
        "choix": ["Fortnite", "Asphalt 9: Legends", "PUBG Mobile", "Clash of Clans"],
        "reponse": "Clash of Clans"
    },
    {
        "question": "Quel jeu est souvent considéré comme ayant popularisé l'e-sport en Corée du Sud ?",
        "choix": ["League of Legends", "StarCraft", "Dota 2", "Counter-Strike"],
        "reponse": "StarCraft"
    },
    {
        "question": "Quel jeu en ligne a été le premier à atteindre 10 millions d'abonnés ?",
        "choix": ["EverQuest", "World of Warcraft", "Runescape", "Final Fantasy XI"],
        "reponse": "World of Warcraft"
    }
])

# Ajout des 20 nouvelles questions sur l'histoire des jeux vidéo

questions.extend([
    {
        "question": "Quel est le premier jeu vidéo commercialisé ?",
        "choix": ["Pong", "Space Invaders", "Pac-Man", "Tetris"],
        "reponse": "Pong"
    },
    {
        "question": "En quelle année est sorti le jeu 'Super Mario Bros.' ?",
        "choix": ["1983", "1985", "1987", "1989"],
        "reponse": "1985"
    },
    {
        "question": "Quel jeu est souvent crédité comme ayant sauvé l'industrie du jeu vidéo après le krach de 1983 ?",
        "choix": ["Donkey Kong", "Pac-Man", "Super Mario Bros.", "Sonic the Hedgehog"],
        "reponse": "Super Mario Bros."
    },
    {
        "question": "Quel jeu est souvent considéré comme le premier jeu de plateforme ?",
        "choix": ["Donkey Kong", "Super Mario Bros.", "Pitfall!", "Sonic the Hedgehog"],
        "reponse": "Donkey Kong"
    },
    {
        "question": "Quel jeu de rôle en ligne massivement multijoueur (MMORPG) a été le plus populaire au début des années 2000 ?",
        "choix": ["World of Warcraft", "EverQuest", "Final Fantasy XI", "Runescape"],
        "reponse": "World of Warcraft"
    },
    {
        "question": "Quel jeu de puzzle a été développé par un programmeur russe et est devenu un succès mondial ?",
        "choix": ["Tetris", "Dr. Mario", "Columns", "Puyo Puyo"],
        "reponse": "Tetris"
    },
    {
        "question": "Quel jeu de course a été le premier à utiliser des graphismes en 3D ?",
        "choix": ["Out Run", "Pole Position", "Virtua Racing", "Gran Turismo"],
        "reponse": "Virtua Racing"
    },
    {
        "question": "Quel jeu de plateforme a été développé par Naughty Dog et est devenu une série emblématique pour la PlayStation ?",
        "choix": ["Spyro the Dragon", "Crash Bandicoot", "Jak and Daxter", "Ratchet & Clank"],
        "reponse": "Crash Bandicoot"
    },
    {
        "question": "Quel jeu a popularisé le genre des jeux de tir à la première personne (FPS) ?",
        "choix": ["Wolfenstein 3D", "Quake", "Half-Life", "Doom"],
        "reponse": "Doom"
    },
    {
        "question": "Quel jeu a été le premier à inclure un mode multijoueur en ligne ?",
        "choix": ["Doom", "Ultima Online", "Quake", "EverQuest"],
        "reponse": "Doom"
    },
    {
        "question": "Quel jeu de simulation de ville a été créé par Will Wright ?",
        "choix": ["Spore", "SimCity", "RollerCoaster Tycoon", "The Sims"],
        "reponse": "SimCity"
    },
    {
        "question": "Quel est le premier jeu vidéo jamais créé ?",
        "choix": ["Pong", "Spacewar!", "Tennis for Two", "Computer Space"],
        "reponse": "Tennis for Two"
    },
    {
        "question": "Quel est le premier jeu vidéo commercialisé ?",
        "choix": ["Pong", "Space Invaders", "Computer Space", "Pac-Man"],
        "reponse": "Computer Space"
    },
    {
        "question": "Quel est le nom de la première console de jeux vidéo domestique ?",
        "choix": ["Atari 2600", "Magnavox Odyssey", "Nintendo Entertainment System (NES)", "Sega Genesis"],
        "reponse": "Magnavox Odyssey"
    },
    {
        "question": "Quel jeu est souvent considéré comme le premier jeu d'arcade à succès ?",
        "choix": ["Pong", "Space Invaders", "Pac-Man", "Donkey Kong"],
        "reponse": "Space Invaders"
    },
    {
        "question": "Quel est le nom du créateur de l'ancêtre des consoles, la Brown Box ?",
        "choix": ["Ralph Baer", "Nolan Bushnell", "Gunpei Yokoi", "Yuji Naka"],
        "reponse": "Ralph Baer"
    },
    {
        "question": "Quel jeu 'Bertie the Brain' permettait-il de jouer ?",
        "choix": ["Pong", "Space Invaders", "Tic-tac-toe", "Pac-Man"],
        "reponse": "Tic-tac-toe"
    },
    {
        "question": "Qu'est-il arrivé à 'Bertie the Brain' après l'exposition ?",
        "choix": ["Il a été vendu à un musée", "Il a été démonté et oublié", "Il a été utilisé dans des écoles", "Il a été amélioré pour d'autres expositions"],
        "reponse": "Il a été démonté et oublié"
    },
    {
        "question": "Sur quel type d'écran 'Tennis for Two' était-il affiché ?",
        "choix": ["Écran CRT", "Écran plasma", "Oscilloscope", "Écran LCD"],
        "reponse": "Oscilloscope"
    },
    {
        "question": "Quel était l'objectif principal de la création de 'Tennis for Two' ?",
        "choix": ["Divertissement pur et simple", "Démontrer les capacités des ordinateurs analogiques", "Tester les compétences en programmation", "Créer un jeu éducatif pour les enfants"],
        "reponse": "Démontrer les capacités des ordinateurs analogiques"
    }
])

# Ajout des 20 nouvelles questions sur les médias et la technologie

questions.extend([
    {
        "question": "Quel est le premier média de masse connu ?",
        "choix": ["La télévision", "La radio", "Le journal imprimé", "Internet"],
        "reponse": "Le journal imprimé"
    },
    {
        "question": "En quelle année a été inventée l'imprimerie par Gutenberg ?",
        "choix": ["1450", "1492", "1500", "1550"],
        "reponse": "1450"
    },
    {
        "question": "Quel média a joué un rôle crucial pendant la Seconde Guerre mondiale pour la diffusion des informations ?",
        "choix": ["La télévision", "La radio", "Le cinéma", "Les journaux"],
        "reponse": "La radio"
    },
    {
        "question": "Quel média a révolutionné la communication dans les années 1990 ?",
        "choix": ["La télévision", "La radio", "Internet", "Le téléphone mobile"],
        "reponse": "Internet"
    },
    {
        "question": "Quel est le premier réseau social à avoir été créé ?",
        "choix": ["Facebook", "MySpace", "LinkedIn", "Friendster"],
        "reponse": "Friendster"
    },
    {
        "question": "En quelle année a été lancé Facebook ?",
        "choix": ["2002", "2004", "2006", "2008"],
        "reponse": "2004"
    },
    {
        "question": "Quel est le rôle des influenceurs dans le marketing digital ?",
        "choix": ["Créer des produits", "Diffuser des publicités", "Promouvoir des marques", "Gérer les réseaux sociaux"],
        "reponse": "Promouvoir des marques"
    },
    {
        "question": "Quel réseau social est principalement utilisé par les professionnels pour le réseautage ?",
        "choix": ["Facebook", "Instagram", "LinkedIn", "Twitter"],
        "reponse": "LinkedIn"
    },
    {
        "question": "Quel support de stockage numérique possède la plus grande capacité ?",
        "choix": ["La disquette", "La carte SD", "Le CD", "Le Blu-ray"],
        "reponse": "Le Blu-ray"
    },
    {
        "question": "Lequel des services suivants n'est pas un système de stockage en ligne ?",
        "choix": ["Dropbox", "Google Drive", "Deezer", "OneDrive"],
        "reponse": "Deezer"
    },
    {
        "question": "Quel était le service initial proposé par Netflix ?",
        "choix": ["Streaming de vidéos", "Location de DVD", "Vente de DVD", "Location de cassettes VHS"],
        "reponse": "Location de DVD"
    },
    {
        "question": "Quel était le nom du site créé par Mark Zuckerberg à l'origine de Facebook ?",
        "choix": ["FaceMash", "TheFacebook", "Friendster", "MySpace"],
        "reponse": "TheFacebook"
    },
    {
        "question": "Quel était à l'origine l'objectif de Youtube ?",
        "choix": ["Un service de replay vidéo", "Un site de rencontres", "Un recueil de tuto de cuisine", "Un réseau social"],
        "reponse": "Un service de replay vidéo"
    },
    {
        "question": "Quel événement majeur a eu lieu en octobre 2022 concernant Twitter ?",
        "choix": ["Il a été renommé X", "Il a atteint 1 milliard d'utilisateurs", "Il a été racheté par Elon Musk", "Il a été introduit en bourse"],
        "reponse": "Il a été racheté par Elon Musk"
    },
    {
        "question": "Quelle technologie est utilisée par Pokémon GO pour superposer des éléments virtuels sur le monde réel ?",
        "choix": ["Réalité virtuelle", "Réalité augmentée", "Intelligence artificielle", "Blockchain"],
        "reponse": "Réalité augmentée"
    },
    {
        "question": "Quelle application n'utilise pas la technologie de la réalité augmentée ?",
        "choix": ["IKEA Place", "Pokémon Go", "Google Maps", "Uber eats"],
        "reponse": "Uber eats"
    },
    {
        "question": "Lequel des éléments suivants n'utilise pas la technologie de réalité virtuelle ?",
        "choix": ["Le Nintendo Labo VR Kit", "Le Google Cardboard", "Les Google Glass", "L'Oculus Rift"],
        "reponse": "Les Google Glass"
    },
    {
        "question": "Quel entreprise ne fait pas partie des 'licornes' françaises ?",
        "choix": ["Deezer", "Dailymotion", "BlaBlaCar", "Doctolib"],
        "reponse": "Dailymotion"
    },
    {
        "question": "Quelle plateforme de streaming est le numéro 1 mondial en terme d'utilisateurs actifs ?",
        "choix": ["Spotify", "Netflix", "Youtube", "Deezer"],
        "reponse": "Youtube"
    },
    {
        "question": "Pourquoi les supports de stockage magnétiques sont-ils remplacés par des supports optiques ou électroniques ?",
        "choix": ["Dégradation au fil du temps", "Consommation d'énergie élevée", "Coût de maintenance élevé", "Difficulté de mise à jour"],
        "reponse": "Dégradation au fil du temps"
    }
])











score = 0

print("Bienvenue dans le quiz de révision !\n")

for q in questions:
    print(q["question"])
    for i, choix in enumerate(q["choix"]):
        print(f"{i + 1}. {choix}")
    
    reponse_utilisateur = input("Votre réponse (numéro) : ")
    
    if q["choix"][int(reponse_utilisateur) - 1] == q["reponse"]:
        print("Bonne réponse ! ✅\n")
        score += 1
    else:
        print(f"Mauvaise réponse. La bonne réponse était : {q['reponse']} ❌\n")

print(f"Quiz terminé ! Votre score final est : {score}/{len(questions)}")

