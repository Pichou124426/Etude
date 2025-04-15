#include "Weapon.hpp"

Weapon :: Weapon ()
{
    name = "Epée en bois";
    damages = 10;
};

Weapon :: Weapon (string newName, int newDamages)
{
    name = newName;
    damages = newDamages;
};

void Weapon :: update(string newName, int newDamages) 
{
    name = newName;
    damages = newDamages;
};

void  Weapon :: display()
{
    cout << "Name: " + name << endl;
    cout << "Damage: " << damages << endl;
};

int Weapon :: getDamages() const
{
    return damages;
};
