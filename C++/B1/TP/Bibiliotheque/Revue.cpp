#include "Revue.hpp"
#include <chrono>
#include <ctime>

Revue ::Revue(string newTitle, string newAuthor, int newPublicationYear, string newCodeConnexion, int newNumber, string newMonth) : Document(newTitle, newAuthor, newPublicationYear, newCodeConnexion)
{
    number = newNumber;
    month = newMonth;
};
void Revue ::display() const
{
    Document ::display();
    cout << "Number :" << number << endl;
    cout << "Month :" + month << endl;
};
bool Revue ::lendable()
{
    auto currentTime = std::chrono::system_clock::now();                  // Obtenir l'heure système actuelle
    std::time_t time = std::chrono::system_clock::to_time_t(currentTime); // Convertir en type time_t
    std::tm *localTime = std::localtime(&time);                           // Convertir en struct tm pour des informations détaillées

    if (publicationYear < (1900 + localTime->tm_year))
    {
        cout << "La revue : " + title + " est disponible à l'emprunt." << endl;
        return true;
    }
    else
    {
        cout << "Malheursement, la revue : " + title + "n'est pas disponible à l'emprunt." << endl;
        return false;
    }
};