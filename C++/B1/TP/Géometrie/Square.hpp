#include "Figure.hpp"

class Square : public Figure
{
private:
    float lenght;

public:
    Square(float newLenght);
    void display();
    float perimeter();
    float area();
};