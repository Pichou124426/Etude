#include "Woman.hpp"

Woman ::Woman() : Person() {};
Woman ::Woman(string newFirstName, string newLastName, int newAge) : Person(newFirstName, newLastName, newAge) {};
bool Woman ::isSingle() {
    return partner.getFirstName() == "" && partner.getLastName() == "" && partner.getAge() == 0;
};
Person Woman ::getPartner()
{
    return partner;
};
void Woman ::setPartner(Person newPartner)
{
    partner = newPartner;
};
void Woman::display() {
    Person::display();
    if (isSingle()) {
        cout << "Elle est célibataire." << endl;
    } else {
    cout << "Elle est mariée avec " << partner.getFirstName() << " " << partner.getLastName() << "." << endl;
    }
    
}
