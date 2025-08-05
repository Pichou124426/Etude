#include<stdio.h>

int main() {
    int tab[50];
    int n, s = 0;
    int max, min;

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

    // Calcul minimum et maximum
    // Suppose que le tableau n'est pas vide
    max = tab[0];
    min = tab[0];
    for (int i = 1; i < n; i++) {
        if (tab[i] > max) {
            max = tab[i];
        }
        if (tab[i] < min) {
            min = tab[i];
        }
    }
    printf("Minimum : %d\n", min);
    printf("Maximum : %d\n", max);
}
