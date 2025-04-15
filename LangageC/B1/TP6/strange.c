#include<stdio.h>
#include<stdlib.h>

// slen : longueur d'une chaîne

int slen(char s[]) {
    int l = 0;
    char *p; // pointeur vers char

    p = s; // se place au début
    while ( *p++ ) { // ou *p et p++ en fin de bloc
        l++;
    }
    return l;
}

int slen2(char s[]) {
    int l = 0;
    int i = 0;
    while ( s[i++] ) {
       l++;
    }
    return l;
}

// p++ ça augment p de 1 (passe à l'elt suivant)
// ça a quel valeur : la valeur de p AVANT l'ajout de 1
// "post incrémentation" (le ++ est après p)

int main() {
    char txt1[50];

    printf("Saisisez un mot : ");
    scanf("%s", txt1); // pas de & ?
                       // pourquoi ?
    printf("Vous avez saisi : %s\n", txt1);
    printf(" de longueur : %d\n", slen(txt1));
    printf(" de longueur : %d\n", slen2(txt1));
