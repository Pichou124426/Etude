#include "Document.cpp"
#include "Livre.cpp"
#include "Dvd.cpp"
#include "Revue.cpp"

int main()
{
    Dvd noah("Titre","Noah",2000,"noah",34,3);
    Livre bible("Bible","Pape",2000,"deg",234);
    Revue yann("Coucou","Yannou",2020,"icgic",24,"janvier");
    
    noah.display();
    noah.lendable(); 
    bible.display();
    bible.lendable(); 
    yann.display();
    yann.lendable();

    return 0;
};