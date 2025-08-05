#include "Character.cpp"
#include "Weapon.cpp"

int main()
{
    Weapon pistol ("Pistolet",20);
    Weapon pickaxe ("Pioche",10);
    Character geralt("Gerald", 100, 100,pistol);
    Character yennefer("Yennefer", 100, 100,pickaxe);
    geralt.receiveDamages(78);
    geralt.attack(yennefer);
    geralt.display();
    yennefer.display();
    pistol.display();
    yennefer.isAlive();
    pickaxe.display();
    
    return 0;
};
