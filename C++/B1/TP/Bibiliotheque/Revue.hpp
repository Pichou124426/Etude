#include <iostream>
#include <string>
#include "Document.hpp"
#pragma once
using namespace std;

class Revue : public Document
{
private:
    int number;
    string month;

public:
    Revue(string newTitle, string newAuthor, int newPublicationYear, string newCodeConnexion, int newNumber, string newMonth);
    void display() const;
    bool lendable();
};