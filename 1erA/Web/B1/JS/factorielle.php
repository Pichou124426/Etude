<script>
    function factorielle(number) 
    {
        if (number == 0){
            return 1;
        }else{
            return number * factorielle(number - 1);
        }
    }
    console.log(factorielle(5));
    document.write(factorielle(5));
    
</script>