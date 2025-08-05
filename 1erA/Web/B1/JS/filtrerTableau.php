<script>
    function filtrerTableau() {
        var tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        var tableauFiltre = [];
        for (var i = 0; i < tableau.length; i++) {
            if (tableau[i] % 2 == 0) {
                tableauFiltre.push(tableau[i]);
            };
        };
        console.log(tableauFiltre);

    };
    filtrerTableau();
</script>