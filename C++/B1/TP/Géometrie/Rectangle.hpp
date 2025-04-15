#include "Figure.hpp"

class Rectangle : public Figure
{
private:
    float lenght;
    float width;

public:
    Rectangle(float newLenght, float newWidth);
    void display();
    float perimeter();
    float area();
};