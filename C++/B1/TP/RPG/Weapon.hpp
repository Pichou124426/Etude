#include <iostream>
#include <string>
#pragma once 
using namespace std; 

class Weapon 
{
private:
    string name; 
    int damages;

public:
    Weapon ();
    Weapon (string newName, int newDamages);
    void update(string newName, int newDamages); 
    void display();
    int getDamages() const;
};
