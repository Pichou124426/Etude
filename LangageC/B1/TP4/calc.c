#include<stdio.h>
#include <stdlib.h>

int main() {
    char c;
    double x, y, res;

    printf("Saisissez deux nombres : ");
    scanf("%lf", &x);
    scanf("%lf", &y);

    printf("Opération [+-*/] : ");
    scanf(" %c", &c);

    switch (c) {
    	case '+':
    	    res = x + y; 
    	    break; 

		case '-':
		    res = x - y; 
		   break;

		case '*':
		   res = x * y;
		   break;

		case '/':
		   res = x/y;
		   break;

		default : 
		   printf("Erreur de saisie, veuillez ressayez");
		   exit(0);
    }

    // TODO: switch / case
    // test si c est '+', '-', '*' ou '/'

    printf("Résultat: %.2lf\n", res);
}
