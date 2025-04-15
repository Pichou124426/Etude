#include "Triangle.hpp"

Triangle ::Triangle(float newBase, int newHeight)
{
    base = newBase;
    height = newHeight;
}

void Triangle ::display()
{
    cout << "Un Triangle avec une base de  " << base << "cm  et une hauteur de " << height << "cm." << endl;
    cout << "-  Perimeter :" << perimeter() << "cm" << endl;
    cout << "-  Area :" << area() << "cm²" << endl;
}

float Triangle ::perimeter()
{
    float perimeterTriangle = base * (height * 2);
    return perimeterTriangle;
}

float Triangle ::area()
{
    float areaTriangle = (base * height) / 2;
    return areaTriangle;
}