<form id="form2" method="GET">
    <input type="text" name="nom" placeholder="Inserer votre nom "/>
    <input type="text" name ="message" placeholder="Inserer votre message" />
    <input type="submit" name="Envoyer" />
</form>

<?php 
    $nom = $_GET['nom'];
    $messagetext = $_GET['message'];
    if ($nom and $messagetext != null) {
        echo " Bienvenue $nom, <br> Voici ton message personnalisé :$messagetext";
     } else {
        echo "Veuillez saisir toute les informations avant d'envoyer svp";

     }
   
    ?>

