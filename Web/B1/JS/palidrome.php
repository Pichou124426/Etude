<?php include "reverse.php" ?>

<script>
    function isPalindrome() {
        word = prompt("Enter a word: ");
        if (reverseString(word) == word) {
            alert(word + " is a palindrome.");

        } else {
            alert(word + " is not a palindrome.");

        }
    }

    isPalindrome();
</script>