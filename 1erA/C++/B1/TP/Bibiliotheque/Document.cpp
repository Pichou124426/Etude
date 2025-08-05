#include "Document.hpp"

Document ::Document(string newTitle, string newAuthor, int newPublicationYear, string newCodeConnexion)
{
    title = newTitle;
    author = newAuthor;
    publicationYear = newPublicationYear;
    codeConnexion = newCodeConnexion;
}

void Document ::display() const
{
    cout << "----------------------------------" << endl;
    cout << "Title : " + title << endl;
    cout << "Author : " + author << endl;
    cout << "Year Publication : " << publicationYear << endl;
    cout << "Code Connexion :" + codeConnexion << endl;
}