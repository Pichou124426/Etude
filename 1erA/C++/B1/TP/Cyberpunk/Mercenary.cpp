#include "Mercenary.hpp"

Mercenary :: Mercenary(string newFirstName, string newLastName, int newLifePoint, int newReputation, int newMoney)
{
    firstName = newFirstName;
    lastName = newLastName;
    lifePoint = newLifePoint;
    reputation = newReputation;
    money = newMoney;
};
void Mercenary :: displayStats()
{
    cout << "------------------------------------" << endl;
    cout << "Your name : " + firstName + " " + lastName << endl;
    cout << "Your health : " << lifePoint << " Pv" << endl;
    cout << "Your reputation : " << reputation << " levels" << endl;
    cout << "Your money : " << money << " dollars" << endl;
    cout << "------------------------------------" << endl;
};
void Mercenary :: recieveDamages(int damages)
{
    lifePoint -= damages;
    if (lifePoint < 0)
    {
        lifePoint = 0;
    };
};
void Mercenary :: getMoney(int dollars)
{
    money += dollars;
};
void Mercenary :: getreputation(int level)
{
    reputation += level;
};