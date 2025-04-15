#include <stdio.h>

int n_digits( char *s) {


	int compteur =0 ; 


	while ( *s ) {
		if (*s >= '0' && *s <= '9'){

			compteur++;         // conditions respecté donc le compteur augmente 
		}

		s++;  // Je me déplace de 1 vers la droite 
	}

	return compteur; 

}

int main ( int arg, char *argv[]) {

	if ( arg != 2) {
	
		printf("Erreur");

		return 1;
	}

	int total = n_digits(argv[1]);

	printf("%d\n", total);

	return 0; 
}
