#include <iostream>
#include <string>
#pragma once
using namespace std;

class Figure
{
protected:
public:
    virtual void display();
    virtual float perimeter() = 0;
    virtual float area() = 0;
};