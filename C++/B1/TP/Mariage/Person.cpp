#include "Person.hpp"
Person ::Person()
{
    firstName = "";
    lastName = "";
    age = 0;
};

Person ::Person(string newFirstName, string newLastName, int newAge)
{
    firstName = newFirstName;
    lastName = newLastName;
    age = newAge;
};

void Person ::getOld()
{
    age++;
};

string Person ::getFirstName()
{
    return firstName;
};
void Person ::setFirstName(string newFirstName)
{
    firstName = newFirstName;
};
string Person ::getLastName()
{
    return lastName;
};
void Person ::setLastName(string newLastName)
{
    lastName = newLastName;
};
int Person ::getAge()
{
    return age;
};
void Person ::setAge(int newAge) 
{
    age = newAge;
};
void Person ::display()
{
    cout << "------------------------------------" << endl;
    cout << firstName + " a " << age << " ans." <<endl;
    ;
}