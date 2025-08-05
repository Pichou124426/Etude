#include "Character.hpp"

Character::Character()
{
    name = "";
    life = 100;
    mana = 100;
};

Character ::Character(string newName, int newLife, int newMana, Weapon newEquipedWeapon)
{
    name = newName;
    life = newLife;
    mana = newMana;
    equipedWeapon = newEquipedWeapon;
};

Character ::~Character()
{
    cout << "Le destructeur a été appelé ici !" << endl;
};

void Character ::receiveDamages(int damages)
{
    life -= damages;
    if (life < 0)
    {
        life = 0;
    };
};

void Character ::attack(Character &target)
{
    int currentDamage = equipedWeapon.getDamages();
    target.receiveDamages(currentDamage);
};

void Character ::takeLifePotion(int lifePoints)
{
    life += lifePoints;
    if (life > 100)
    {
        life = 100;
    };
};

void Character ::switchWeapon(string weaponName, int weaponDamages)
{
    equipedWeapon.update(weaponName, weaponDamages);
};

bool Character ::isAlive()
{
    if (life == 0)
    {
        cout << "Vous êtes mort !" << endl; 
        return false;
    }
    else
    {
        cout << "Vous êtes toujours en vie " << endl;
        return true;
    };
};

void Character ::display()
{
    cout << "Name :" + name << endl;
    cout << "Life :" << life << endl;
    cout << "Mana :" << mana << endl;
}