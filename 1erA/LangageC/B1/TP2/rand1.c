//BUT: Renvoyer un nombre pseudo-aléatoirement compris entre sur borne max. 
//ENTREE: Borne maximum saisie par l'utilisateur. 
//SORTIE : Le nombre aléatoire. 

#include <stdio.h>
#include <stdlib.h>
int main (){ 
	int hasard;	

	hasard = rand();
	printf("Tirage : %d\n", hasard);  
	hasard = rand();
	printf("Tirage : %d\n", hasard);  
	hasard = rand();
	printf("Tirage : %d\n", hasard);  
}
