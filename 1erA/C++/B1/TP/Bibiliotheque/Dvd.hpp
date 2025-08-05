#include <iostream>
#include <string>
#include "Document.hpp"
#pragma once
using namespace std;

class Dvd : public Document 
{
private : 
    int duration; 
    int minimumAge;

public : 
    Dvd(string newTitle, string newAuthor, int newPublicationYear, string newCodeConnexion,int newDuration, int newMinimumAge);
    void display() const;
    bool lendable();
};