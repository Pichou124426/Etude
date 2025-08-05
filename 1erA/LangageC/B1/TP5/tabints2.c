#include<stdio.h>

int main() {
    int tab[5];
    int n, s = 0;

    printf("Entrez cinq nombres entiers :\n");

    for (int i = 0; i < 5; i++) {
        printf("%i> ", i+1);
        scanf("%d", &tab[i]);
        s += tab[i];
    }

    printf("Valeurs : ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", tab[i]);
    }
    printf("\nSomme : %d\n", s);
}
