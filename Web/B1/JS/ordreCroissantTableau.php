<script>
    function trierTableau() {
        tableau = [];
        for (var i = 0; i < 10; i++) {
            input = prompt("Entrez dix nombres: ");
            if (isNaN(input)) {
                alert("Veuillez entrer un nombre.");
                continue;
            };
            tableau.push(parseInt(input));
        };
        prompt("Dans quel ordre voulez-vous trier le tableau? (C = croissant/ D = décroissant)");
        
        if (prompt == "C") {
            tableau.sort(function(a, b) {
                return a - b
            });
        if (prompt == "D") {
            tableau.sort(function(a, b) {
                return b - a
            });
        };
        } else {
            alert("Veuillez entrer C ou D.");{
                return 
            };
        }
        return tableau;
    };
    document.write(trierTableau());
</script>