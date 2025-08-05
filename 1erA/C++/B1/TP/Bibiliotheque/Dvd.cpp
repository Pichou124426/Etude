#include "Dvd.hpp"

Dvd ::Dvd(string newTitle, string newAuthor, int newPublicationYear, string newCodeConnexion, int newDuration, int newMinimumAge) : Document(newTitle, newAuthor, newPublicationYear, newCodeConnexion)
{
    duration = newDuration;
    minimumAge = newMinimumAge;
};
void Dvd ::display() const
{
    Document ::display();
    cout << "Duration : " << duration << " minute(s)" << endl;
    cout << "Minimum Age : " << minimumAge << endl;
};
bool Dvd ::lendable()
{
    cout << "Entrez votre âge :";
    int userAge = 0;
    cin >> userAge;

    if (userAge < minimumAge)
    {
        cout << "Désolé, vous ne pouvez pas emprunter ce DVD, l'age requis est " + minimumAge << "et vous avez que " + userAge << "ans." << endl;
        return false;
    }
    else
    {
        cout << "Le Dvd est disponible à l'emprunt." << endl;
        return true;
    };
};
