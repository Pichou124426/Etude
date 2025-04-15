#include "Livre.hpp"

Livre ::Livre(string newTitle, string newAuthor, int newPublicationYear, string newCodeConnexion, int newNumberPages) : Document(newTitle, newAuthor, newPublicationYear, newCodeConnexion)
{
    numberPages = newNumberPages;
}

void Livre ::display() const
{
    Document ::display();
    cout << "Number Page(s) : " << numberPages << endl;
}

bool Livre ::lendable()
{
    
    cout << "Le livre :" + title << " est empruntable." << endl;
    return true;
}