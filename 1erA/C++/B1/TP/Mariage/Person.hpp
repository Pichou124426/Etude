#include <iostream>
#include <string>
#pragma once
using namespace std;

class Person
{
protected:
    string firstName;
    string lastName;
    int age;

public:
    Person();
    Person(string newFirstName, string newLastName, int newAge);
    void getOld();
    string getFirstName();
    void setFirstName(string newFirstName);
    string getLastName();
    void setLastName(string newLastName);
    int getAge();
    void setAge(int newAge);
    void display();
};
