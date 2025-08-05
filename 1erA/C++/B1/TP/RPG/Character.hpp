#include <iostream>
#include <string> 
#include "Weapon.hpp"
#pragma once 
using namespace std;

class Character
{
private : 
    string name;
    int life;
    int mana;
    Weapon equipedWeapon;

public :
    Character();
    Character(string newName, int newLife, int newMana, Weapon equipedWeapon );
    void receiveDamages(int damages); 
    void attack(Character &target); 
    void takeLifePotion(int lifePoints); 
    void switchWeapon(string weaponName, int weaponDamages); 
    bool isAlive(); 
    void display();
    void switchWeapon();

    ~Character();

};