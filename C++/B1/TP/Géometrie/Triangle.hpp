#include "Figure.hpp"

class Triangle : public Figure
{
private:
    float base;
    float height;

public:
    Triangle(float newBase, int newHeight);
    void display();
    float perimeter();
    float area();
};
