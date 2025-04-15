#include "Woman.cpp"
#include"Person.cpp"
#include "Man.cpp"

int main () 
{ 
    Man noah ("Noah","Sillaire",15);
    Man téo ("Théo","Defert",12);
    Woman melina ("Melina", "Reveret",23);
    melina.setPartner(noah);
    noah.setPartner(melina);
    melina.isSingle();
    melina.display();
    noah.display ();
    noah.getOld();
    noah.setAge(29);
    noah.display();
    Man yann ("Yann","Touron",23);
    Man raf ("Rapahel","Dumas",1);
    yann.setPartner(raf);
    yann.display();
    yann.isSingle();






    return 0;
};