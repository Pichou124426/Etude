#include <IRremote.hpp> // Bibliothèque pour le récepteur infrarouge
#include <LiquidCrystal.h> // Bibliothèque pour l'écran LCD
#include <Servo.h> // Bibliothèque pour le servo moteur

#define IR_RECEIVE_PIN 3 // Broche pour le récepteur infrarouge
Servo servoDeYann; // Création de l'objet Servo
LiquidCrystal lcd(7, 8, 9, 10, 11, 12); // Initialisation de l'écran LCD

unsigned long previousMillis = 0; // Stocke le temps écoulé
const unsigned long interval = 15; // Intervalle de mise à jour de l'écran et du servo
int targetPosition = -1; // Position cible du servo (-1 signifie aucune commande active)

void setup() {
    Serial.begin(9600); // Initialisation de la communication série
    IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK); // Démarrage du récepteur infrarouge
    servoDeYann.attach(2); // Lier le servo à la broche 2
    lcd.begin(16, 2); // Initialiser l'écran LCD
    lcd.print("Appuyer bouton"); // Afficher un message d'accueil
    delay(2000); // Pause pour laisser le message affiché
    lcd.clear(); // Effacer l'écran après l'accueil
}

void loop() {
    unsigned long currentMillis = millis(); // Récupérer le temps actuel

    // Décoder le signal infrarouge s'il y en a un
    if (IrReceiver.decode()) {
        Serial.print("Code IR reçu : ");
        Serial.println(IrReceiver.decodedIRData.command, HEX); // Affiche le code IR dans le moniteur série

        lcd.clear();
        lcd.print("Code IR: ");
        lcd.print(IrReceiver.decodedIRData.command, HEX); // Affiche le code IR reçu

        // Met à jour la position cible en fonction de la commande IR
        switch (IrReceiver.decodedIRData.command) {
            case 0xC: // Bouton 1
                targetPosition = 0;
                lcd.clear();
                lcd.print("Servo: 0 deg");
                break;
            case 0x18: // Bouton 2
                targetPosition = 90;
                lcd.clear();
                lcd.print("Servo: 90 deg");
                break;
            case 0x5E: // Bouton 3
                targetPosition = 180;
                lcd.clear();
                lcd.print("Servo: 180 deg");
                break;
            default:
                targetPosition = -1; // Code inconnu, pas de changement
                lcd.clear();
                lcd.print("Appuyer sur un bouton : 1 - 2 - 3");
                break;
        }
        IrReceiver.resume(); // Réinitialiser le récepteur pour recevoir un autre signal
    }

    // Vérifier si le temps est écoulé pour effectuer une action
    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis; // Réinitialiser le temps précédent

        // Si une position cible est définie, déplacer le servo
        if (targetPosition != -1) {
            servoDeYann.write(targetPosition); // Déplacer le servo à la position cible
            targetPosition = -1; // Réinitialiser après l'exécution
        }
    }
}