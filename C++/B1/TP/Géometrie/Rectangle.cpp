#include "Rectangle.hpp"

Rectangle ::Rectangle(float newLenght, float newWidth)
{
    lenght = newLenght;
    width = newWidth;
}
void Rectangle ::display()
{   
    cout << "Un rectangle avec une longueur de " << lenght << "cm  et une largeur de " << width << "cm." << endl;
    cout << "-  Perimeter :" << perimeter() << "cm" << endl;
    cout << "-  Area :" << area() << "cm²" << endl;
}
float Rectangle ::perimeter()
{
    float perimeterRectangle = (lenght + width) * 2 ;
    return perimeterRectangle;
};
float Rectangle ::area()
{
    float areaRectangle = lenght * width;
    return areaRectangle;
};