<?php
$nom = "Noah";
$age = 10;
echo "Je m'appelle $nom et j'ai $age ans.";
?>

<?php

$note = rand(min: 0, max: 20);
if ($note > 9) {
    echo "Bravo, avec une note de $note, tu as reussis l'examen";
} else {
    echo "Tu es un zeub avec ton vieux $note.";
}
$bulletin = array()
?> 

<?php
$bulletin = [];
$coefficients = [];
$total = 0;
$totalCoefficients = 0;

for ($i = 0; $i < 10; $i++) {
    $note = rand(0, 20);
    $coefficient = rand(1, 5);
    $bulletin[] = $note;
    $coefficients[] = $coefficient;
    $total += $note * $coefficient;
    $totalCoefficients += $coefficient;
}

$moyenne = $total / $totalCoefficients;

echo "Notes : " . implode(", ", $bulletin) . "\n";
echo "Coefficients : " . implode(", ", $coefficients) . "\n";
echo "Moyenne pondérée : " . number_format($moyenne, 2) . "\n";

if ($moyenne >= 10) {
    echo "Félicitations ! L'élève a réussi avec une moyenne de $moyenne.";
} else {
    echo "Dommage, l'élève a échoué avec une moyenne de $moyenne.";
}
?>
    