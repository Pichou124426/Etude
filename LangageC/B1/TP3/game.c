#include<stdio.h>
#include<stdlib.h>
#include<time.h>


int main() {
	int secret, guess, found=0;
	int tries =0;

	srand(time(NULL));
	secret = rand() % 100 + 1;

	printf("J'ai choisi un nombre au hasard entre 1 et 100 :\n");


		while (!found)
		 { 

		
			printf("Votre proposition :\n");
			scanf("%d", &guess);
			tries = tries +1;
			
		if ( secret > guess) {
				printf("Le nombre est trop petit\n");
				 
		    	}
			else  if ( secret < guess ) {
			 printf ("Le nombre est trop grand\n");
			 
			    }
			else { found =1; 
				printf("Trouvé !\n");
				}
		}
}

		 
	
	
