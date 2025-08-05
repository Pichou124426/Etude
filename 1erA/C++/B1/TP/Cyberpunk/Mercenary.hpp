#include <iostream>
#include <string>
#pragma once
using namespace std;

class Mercenary
{
private:
    string firstName;
    string lastName;
    int lifePoint;
    int reputation;
    int money;

public:
    Mercenary(string newFirstName, string newLastName, int newLifePoint, int newReputation, int newMoney);
    void displayStats();
    void recieveDamages(int damages);
    void getMoney(int dollars);
    void getreputation(int level);
    // attack(); Méthode  virtuelle  pure  : attack()  (doit  être  redéfinie  par  les  classes dérivées).
};
