#include<stdio.h>

int main() {
    int tab[50];
    int n, s = 0;

    printf("Combien de nombres à saisir (max 50) : ");
    scanf("%d", &n);

    printf("Entrez %d nombres entiers :\n", n);

    for (int i = 0; i < n; i++) {
        printf("%i> ", i+1);
        scanf("%d", &tab[i]);
        s += tab[i];
    }

    printf("Valeurs : ");
    for (int i = 0; i < n; i++) {
        printf("%d ", tab[i]);
    }
    printf("\nSomme : %d\n", s);
}
