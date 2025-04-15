// BUT : Si l'âge est superieur à 42 renvoyer " BOOMER " sinon renvoyer "Time to learn Lunix" 
// ENTREE : Age de l'utilisateur
// SORTIE : TEXTE 

#include <stdio.h>
#define MAX 42 
int main(void){
	int age;

	printf("Entrez votre âge :");
	scanf("%d",&age);

	if ( age> MAX ){
		printf("Vous êtes un boomer\n");
	} else {
		printf("Time to learn Linux\n");
	}
}
