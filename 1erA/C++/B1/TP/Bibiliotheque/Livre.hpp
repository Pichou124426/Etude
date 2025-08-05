#include "Document.hpp"

class Livre : public Document
{
private:
    int numberPages;

public:
    Livre(string newTitle, string newAuthor, int newPublicationYear, string newCodeConnexion, int newNumberPages);
    void display() const;
    bool lendable();
};