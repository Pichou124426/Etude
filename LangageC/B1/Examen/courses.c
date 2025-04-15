#include <stdio.h>

typedef struct prod prod;
struct prod {
    char name[50];
    double price;
    int quantity;
};


void mescourses(prod tab[], int size) {
    double total_general = 0.0;
    printf("----------------\n");        //en-tête
    printf("  Mes courses\n");
    printf("----------------\n");

    for (int i = 0; i < size; i++) {
        double total_produit = tab[i].price * tab[i].quantity;
        total_general += total_produit; 

        printf("%s\n", tab[i].name);
        printf("  Prix   : %.2f\n", tab[i].price);
        printf("  Nombre : %d\n", tab[i].quantity);
        printf("  Total  : %.2f\n", total_produit);
    }
    printf("----------------\n");                //pied de page
    printf("TOTAL    : %.2f\n", total_general);
}

int main() {
    prod courses[] = { //tableau pour prix et qté
        { "Pommes", 2.23, 4 }, 
        { "Poires", 3.10, 5 }, 
        { "Cerises", 6.15, 10 } 
    };
    mescourses(courses, 3);
}
