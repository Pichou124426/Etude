#include "Figure.cpp"
#include "Rectangle.cpp"
#include "Cercle.cpp"
#include "Triangle.cpp"
#include "Square.cpp"
#include <vector>

int main()
{
    vector<Figure *> figures;
    figures.push_back(new Cercle(2.0));
    figures.push_back(new Triangle(5.2, 6.0));
    figures.push_back(new Square(12.4));
    figures.push_back(new Rectangle(3.5, 16.6));

    for (int i = 0; i < figures.size(); i++)
    {
        figures[i]->Figure ::display();
        figures[i]->display();
        figures[i]->perimeter();
        figures[i]->area();
        delete figures[i];
        figures[i] = nullptr;
    };

    return 0;
};