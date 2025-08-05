#include <iostream>
#include <string>
#include "Person.hpp"
#pragma once
using namespace std;

class Woman : public Person
{
private:
    Person partner;

public:
    Woman();
    Woman(string newFirstName, string newLastName, int newAge);
    bool isSingle();
    Person getPartner();
    void setPartner(Person newPartner);
    void display();
};