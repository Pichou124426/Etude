<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jeu Simple</title>
</head>

<body>
    <button id="buttonStart">Commencer</button>
    <button class="button" id="button2">Cliquez ici</button>
    <button class="button" id="button3">Cliquez ici</button>
    <button class="button" id="button4">Cliquez ici</button>
    <button class="button" id="button5">Cliquez ici</button>
    <button class="button" id="button6">Cliquez ici</button>
    <button id="buttonReset">Reset</button>
    <p id="resultat"></p>

    <script>
        const buttons = document.querySelectorAll(".button");
        const buttonStart = document.getElementById("buttonStart");
        const buttonReset = document.getElementById("buttonReset");
        const resultat = document.getElementById("resultat");
        let timeoutID; // Déclare timeoutID pour le timer globalement
        let jeuActif = false; // Variable pour vérifier si le jeu est actif

        // Désactiver un bouton après clic
        buttons.forEach(function (button) {
            button.addEventListener("click", function () {
                if (jeuActif) {
                    button.disabled = true;
                    console.log(`${button.id} désactivé !`);
                    verifierVictoire();
                }
            });
        });

        // Démarrer le jeu avec un timer
        buttonStart.addEventListener("click", function () {
            if (!jeuActif) {
                jeuActif = true; // Le jeu commence
                resultat.textContent = ""; // Réinitialiser le message
                timeoutID = setTimeout(function () {
                    if (jeuActif) {
                        resultat.textContent = "Perdu !  Temps écoulé.";
                        arreterJeu();
                    }
                }, 4000);
            }
        });

        // Réinitialiser le jeu
        buttonReset.addEventListener("click", function () {
            clearTimeout(timeoutID);
            jeuActif = false; // Arrêter le jeu
            resultat.textContent = ""; // Effacer les messages précédents

            // Réactiver tous les boutons
            buttons.forEach(function (button) {
                button.disabled = false;
            });
        });

        // Vérifier si tous les boutons sont désactivés
        const tousDesactives = () => {
            return Array.from(buttons).every(button => button.disabled);
        };

        // Vérifier la victoire
        const verifierVictoire = () => {
            if (tousDesactives() && jeuActif) {
                resultat.textContent = "Gagné ! 🎉Tous les boutons désactivés à temps.";
                arreterJeu();
            }
        };

        // Arrêter le jeu
        const arreterJeu = () => {
            clearTimeout(timeoutID); // Arrêter le timer
            jeuActif = false; // Désactiver le jeu
        };
    </script>
</body>

</html>