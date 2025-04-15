<?php include("header.php"); ?>
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirection</title>
    <script>
        function redirectToIndex() {

            document.getElementById("message").innerText = "The technical team thanks you for your feedback. We will get back to you as soon as possible. You will automatically return to the homepage shortly. The technical team.";

            // Redirige après 3 secondes (4000 millisecondes)
            setTimeout(() => {
                window.location.href = "index.php";
            }, 4000);
        }
    </script>
</head>

<body onload="redirectToIndex()"> <!-- execute la fonction redirectToIndex() lors du chargement de la page -->
    <div class="container">
        <h1 style="text-align: center; margin-top: 20px;">Thank you for your feedback!</h1>
        <div id="message" style="font-size: 24px; text-align: center; margin-top: 20px;"></div>
    </div>
</body>

</html>
<?php include("footer.php"); ?>