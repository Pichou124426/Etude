#include<stdio.h>

int main() {
    int n, val;
    int s = 0;

    printf("Entrez cinq nombres entiers :\n");
    
    for (int i = 0; i < 5; i++) {
        printf("%i> ", i+1);
        scanf("%d", &val);
        s += val;
    }

    printf("Somme : %d\n", s);
}
