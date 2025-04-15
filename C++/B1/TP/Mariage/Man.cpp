#include "Man.hpp"

Man ::Man() : Person() {};
Man ::Man(string newFirstName, string newLastName, int newAge) : Person(newFirstName, newLastName, newAge) {};
bool Man ::isSingle() {
    return partner.getFirstName() == "" && partner.getLastName() == "" && partner.getAge() == 0;
};
Person Man ::getPartner()
{
    return partner;
};
void Man ::setPartner(Person newPartner)
{
    partner = newPartner;

};
void Man::display() {
    Person::display();
    if (isSingle()) {
        cout << "Il est célibataire." << endl;
    } else {
    cout << "Il est marié avec " << partner.getFirstName() << " " << partner.getLastName() << "." << endl;
    }
}
