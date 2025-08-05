//ENTREE : chaine de cractere qui est le mots saisies pas l'UT 
//SORTIE un booleen palindrime du moys 
//BUT : Le programme renvoie si le mot saisie est un palindromes ou non 


#include <stdio.h>

#define max 50

char mot [max];
char *debut,*fin;

int main () {
	printf ("Saisir votre mot : \n");
	scanf ("%s",mot);

	debut = fin  = mot ;
	
	
   
	while (*fin) {
		*fin++ ;
	}
	*fin--;
	



	while (*debut  == *fin  ){
		*debut++, *fin-- ;	}

		if (fin - debut < 1 ) {
		printf ("%s est un palindrome.",mot);
			
		}else{
			printf ("%s n' est pas un palindrome.",mot);
		}
		

		




	
}
