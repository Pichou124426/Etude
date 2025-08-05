#include <iostream>
#include <string>
#include "Person.hpp"
#pragma once
using namespace std;

class Man : public Person
{
private:
    Person partner;

public:
    Man();
    Man(string newFirstName, string newLastName, int newAge);
    bool isSingle();
    Person getPartner();
    void setPartner(Person newPartner);
    void display();
};