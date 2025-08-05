#include <Servo.h>
#include <LiquidCrystal.h>

Servo servoDeYann; // Création de l'objet Servo
LiquidCrystal lcd(7, 8, 9, 10, 11, 12); // Initialisation de l'écran LCD
unsigned long previousMillisPosition = 0; // Stocke le temps écoulé
unsigned long intervalPosition = 15;      // Intervalle de mise à jour de la position du servo

void setup() {
    servoDeYann.attach(2);          // Attacher le servo à la broche 2
    lcd.begin(16, 2);               // Initialiser l'écran LCD (16x2 caractères)
    lcd.print("Coucou Yanou, JTM <3"); // Message de bienvenue
    delay(2000);                    // Pause avant de passer à autre chose
    lcd.clear();                    // Effacer le message de bienvenue
}

void loop() {
    unsigned long currentMillis = millis(); // Obtenir le temps actuel

    // Mouvement du servo de 0 à 180 degrés
    if (currentMillis - previousMillisPosition >= intervalPosition) {
        for (int position = 0; position <= 180; position += 1) {
            servoDeYann.write(position);  // Déplacer le servo à la position
            lcd.clear();                  // Effacer l'écran
            lcd.print("Position: ");      // Afficher le texte
            lcd.print(position);          // Afficher la position
                     
        }
        previousMillisPosition = currentMillis; // Mettre à jour le temps précédent
    }

    // Mouvement du servo de 180 à 0 degrés
    if (currentMillis - previousMillisPosition >= intervalPosition) {
        for (int position = 180; position >= 0; position -= 1) {
            servoDeYann.write(position);  // Déplacer le servo à la position
            lcd.clear();                  // Effacer l'écran
            lcd.print("Position: ");      // Afficher le texte
            lcd.print(position);          // Afficher la position
        }
        previousMillisPosition = currentMillis; // Mettre à jour le temps précédent
    }
}