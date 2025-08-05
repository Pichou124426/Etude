#include <stdio.h>
#include <stdlib.h>
#include<time.h>

	int nb, nbr;

	int main(){

	 srand(time(NULL)); 
	 printf("Veuillez saisir un chiffre");
	 scanf("%d", &nb);
      nbr= rand() % 10 + 1;

	  if (nb == nbr)
	   {
	  
	  	printf("Bravo");

	  	 }
		  else
		   {
			  	printf("Tu as perdu");
			  }
	}
