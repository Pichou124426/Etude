#include "Mercenary.cpp"

int main() 
{
    Mercenary noah ("Noah","Sillaire",100,64,1000);
    noah.displayStats();
    noah.getMoney(99);
    noah.displayStats();
    noah.getreputation(12);
    noah.recieveDamages(123);
    noah.displayStats();
    
    return 0;
};