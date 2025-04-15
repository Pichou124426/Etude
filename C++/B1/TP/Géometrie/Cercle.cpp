#include "Cercle.hpp"

Cercle ::Cercle(float newRadius)
{
    radius = newRadius;
}
void Cercle :: display() 
{   
    cout << "Un cercle avec un rayon de  " << radius << "cm." << endl;
    cout << "-  Perimeter :" << perimeter() << "cm" << endl;
    cout << "-  Area :" << area() << "cm²" <<endl;
}

float Cercle ::perimeter()
{
    float perimeterCercle = 2 * π * radius;
    return perimeterCercle;
};
float Cercle ::area()
{
    float areaCercle = (radius * radius) * π;
    return areaCercle;
};