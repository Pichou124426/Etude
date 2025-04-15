#include <iostream>
#include <string>
#pragma once
using namespace std;

class Document
{
protected:
    string title;
    string author;
    int publicationYear;
    string codeConnexion;

public:
    Document(string newTitle, string newAuthor, int newPublicationYear, string newCodeConnexion);
    void display() const;
    virtual bool lendable() = 0;
};