#include "Square.hpp"

Square ::Square(float newLenght)
{
    lenght = newLenght;
}

void Square ::display()
{
    cout << "Un carré avec des cotés de  " << lenght << "cm" << endl;
    cout << "-  Perimeter :" << perimeter() << "cm" << endl;
    cout << "-  Area :" << area() << "cm²" << endl;
}
float Square ::perimeter()
{
    float perimeterSquare = lenght * 4;
    return perimeterSquare;
};
float Square ::area()
{
    float areaSquare = lenght * lenght;
    return areaSquare;
};