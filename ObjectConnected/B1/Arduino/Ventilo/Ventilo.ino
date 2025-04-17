#include <IRremote.hpp> // Bibliothèque pour le récepteur infrarouge
#include <LiquidCrystal.h> // Bibliothèque pour l'écran LCD

#define IR_RECEIVE_PIN 3  // Broche pour le récepteur infrarouge
#define MOTOR_PIN 1       // Broche pour contrôler le moteur (PWM ou digital selon le type)

LiquidCrystal lcd(7, 8, 9, 10, 11, 12); // Initialisation de l'écran LCD
unsigned long previousMillis = 0;       // Stocke le temps écoulé pour les mises à jour
unsigned long displayMillis = 0;        // Stocke le temps écoulé pour la mise à jour de l'écran LCD
const unsigned long interval = 15;      // Intervalle pour les actions générales
const unsigned long displayInterval = 2000; // Temps pour maintenir les messages affichés sur l'écran

int motorSpeed = 0; // Stocke la vitesse actuelle du moteur
int currentCommand = -1; // Stocke la dernière commande reçue (-1 = aucune commande)

void setup() {
    Serial.begin(9600); // Initialisation de la communication série
    IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK); // Démarrage du récepteur infrarouge
    pinMode(MOTOR_PIN, OUTPUT); // Définir la broche moteur comme sortie
    lcd.begin(16, 2); // Initialiser l'écran LCD
    lcd.print("Appuyer bouton"); // Message d'accueil
    displayMillis = millis(); // Initialiser le temps d'affichage du message
}

void loop() {
    unsigned long currentMillis = millis(); // Obtenir le temps actuel

    // Gérer les signaux infrarouges
    if (IrReceiver.decode()) {
        Serial.print("Code IR reçu : ");
        Serial.println(IrReceiver.decodedIRData.command, HEX); // Affiche le code IR dans le moniteur série

        currentCommand = IrReceiver.decodedIRData.command; // Stocker la commande actuelle
        IrReceiver.resume(); // Réinitialiser le récepteur pour un nouveau signal
        displayMillis = currentMillis; // Mettre à jour le temps de l'écran pour afficher une commande
    }

    // Appliquer l'action en fonction de la commande reçue
    if (currentCommand != -1) { // Vérifier s'il y a une commande active
        switch (currentCommand) {
            case 0xC: // Bouton 1 : Démarrer le moteur à vitesse moyenne
                motorSpeed = 128; // Vitesse moyenne (valeur PWM entre 0 et 255)
                analogWrite(MOTOR_PIN, motorSpeed); // Appliquer la vitesse au moteur
                lcd.setCursor(0, 0);
                lcd.print("Moteur: Moyen    ");
                break;
            case 0x18: // Bouton 2 : Arrêter le moteur
                motorSpeed = 0; // Vitesse zéro
                analogWrite(MOTOR_PIN, motorSpeed); // Arrêt du moteur
                lcd.setCursor(0, 0);
                lcd.print("Moteur: Arret    ");
                break;
            case 0x5E: // Bouton 3 : Arrêter le moteur (sécurité)
                motorSpeed = 0; // Arrêt complet
                analogWrite(MOTOR_PIN, motorSpeed);
                lcd.setCursor(0, 0);
                lcd.print("Moteur: Secu     ");
                break;
            default: // Commande inconnue
                lcd.setCursor(0, 0);
                lcd.print("Code inconnu     ");
                break;
        }
        currentCommand = -1; // Réinitialiser la commande après son exécution
    }

    // Effacer l'écran après l'intervalle défini
    if (currentMillis - displayMillis >= displayInterval) {
        lcd.setCursor(0, 1);
        lcd.print("                  "); // Efface la seconde ligne (ou une partie)
    }
}