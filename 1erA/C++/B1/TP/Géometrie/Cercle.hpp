#include "Figure.hpp"

class Cercle : public Figure
{
private:
    float radius;
    float π = 3.14;

public:
    Cercle(float newRadius);
    void display();
    float perimeter();
    float area();
};