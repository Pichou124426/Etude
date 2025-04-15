<script>
    var numberToFind = Math.floor(Math.random() * 100);
    var remainingAttempts = 7;
    while (remainingAttempts > 0) {
        var input = prompt("Enter a number between 0 and 100: ");
        var numberInput = parseInt(input);

        if (isNaN(numberInput)) {
            alert("Please enter a number.");
            continue;
        };
        if (numberInput < 0 || numberInput > 100) {
            alert("Please enter a number between 0 and 100.");
            continue;
        };


        if (numberInput == numberToFind) {
            alert("Congratulations, you found the right number !");
            break;
        };
        if (numberInput < numberToFind) {
            remainingAttempts--;
            alert("The number to find is greater than " + numberInput + ".");
            alert("You have " + remainingAttempts + " attempts left.");
            continue;
        };
        if (numberInput > numberToFind) {
            remainingAttempts--;
            alert("The number to find is less than " + numberInput + ".");
            alert("You have " + remainingAttempts + " attempts left.");
            continue;
        };
    };
    if (remainingAttempts == 0) {
        alert("You have no more attempts left. The number to find was " + numberToFind + ".");
    };
</script>