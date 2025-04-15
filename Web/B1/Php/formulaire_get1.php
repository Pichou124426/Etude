<form id="form1" method="GET">
    <input type="text" name="query" />
    <input type="submit" value="Envoyer" />
</form>

<?php 
    $query= $_GET['query'];
    echo $query;
    ?>