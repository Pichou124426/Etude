#include<stdio.h>

int main() {
    char s1[] = { 72, 101, 108, 108, 111, 0 };
    char s2[] = { 'H', 'e', 'l', 'l', 'o', '\0' };
    char s3[] = "Hello"; // 0 sera ajouté !

    printf("%s\n", s1);
    printf("%s\n", s2);
    printf("%s\n", s3);

}
