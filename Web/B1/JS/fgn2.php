<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FindGoodNumber</title>
</head>

<body>
    <div id="game-messages"></div>
    <script>
        var numberToFind = Math.floor(Math.random() * 100);
        var remainingAttempts = 7;
        var messagesDiv = document.getElementById("game-messages");

        function addMessage(message) {
            var p = document.createElement("p");
            p.textContent = message;
            messagesDiv.appendChild(p);
        }

        while (remainingAttempts > 0) {
            var input = prompt("Enter a number between 0 and 100: ");
            var numberInput = parseInt(input);

            if (isNaN(numberInput)) {
                addMessage("Please enter a number.");
                continue;
            }
            if (numberInput < 0 || numberInput > 100) {
                addMessage("Please enter a number between 0 and 100.");
                continue;
            }

            if (numberInput == numberToFind) {
                addMessage("Congratulations, you found the right number!");
                break;
            }
            if (numberInput < numberToFind) {
                remainingAttempts--;
                addMessage("The number to find is greater than " + numberInput + ".");
                addMessage("You have " + remainingAttempts + " attempts left.");
                continue;
            }
            if (numberInput > numberToFind) {
                remainingAttempts--;
                addMessage("The number to find is less than " + numberInput + ".");
                addMessage("You have " + remainingAttempts + " attempts left.");
                continue;
            }
        }
        if (remainingAttempts == 0) {
            addMessage("You have no more attempts left. The number to find was " + numberToFind + ".");
        }
    </script>
</body>

</html>