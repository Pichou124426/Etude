<form id="form2" method="POST">
    <input type="text" name="nom" placeholder="Inserer votre nom "/>
    <input type="text" name ="message" placeholder="Inserer votre message" />
    <input type="submit" name="Envoyer" />
</form>

<?php 
    if ($_SERVER["REQUEST_METHOD"]=="POST"){
        $nom = $_POST['nom'];
        $messagetext = $_POST['message'];
        if ($nom !=null and $messagetext != null) {
            echo " Bienvenue $nom, <br> Voici ton message personnalisé :$messagetext";
        } else {
            echo "Veuillez saisir toute les informations avant d'envoyer svp";
    }} 
   
    ?>

