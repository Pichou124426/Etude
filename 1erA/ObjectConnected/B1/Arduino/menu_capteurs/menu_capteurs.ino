#include <LiquidCrystal.h>
#include <DHT.h>

// Initialisation de l'écran LCD (pins 7, 8, 9, 10, 11, 12)
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

// Définition du type de capteur DHT11 et de la pin de connexion
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Définition des broches pour le HC-SR04
#define TRIGPIN 13
#define ECHOPIN 14

// Définition des broches pour le joystick
#define VRX A0
#define VRY A1
#define SW 6

// Variables pour gérer les résultats et l'affichage
int currentScreen = 0; // Indique quel capteur est affiché
int debounceDelay = 200; // Délais d'attente pour éviter les rebonds du bouton
int deadZone = 300; // Zone morte autour de la valeur centrale du joystick

void setup() {
  // Initialisation de l'écran LCD
  lcd.begin(16, 2);
  lcd.print("Coucou gabinou, JTM <3");

  // Initialisation des capteurs
  dht.begin();
  pinMode(TRIGPIN, OUTPUT);
  pinMode(ECHOPIN, INPUT);

  // Configuration du joystick
  pinMode(SW, INPUT_PULLUP);

  // Pause initiale
  delay(2000); // Temps pour lire le message initial
}

void loop() {
  // Lecture des données du joystick
  int xValue = analogRead(VRX);
  int yValue = analogRead(VRY);
  int swState = digitalRead(SW);

  // Détecte si le joystick est incliné vers la gauche ou la droite pour naviguer
  if (xValue < (512 - deadZone)) { // Gauche
    currentScreen--;
    if (currentScreen < 0) currentScreen = 2; // Retourne au dernier écran
    delay(debounceDelay);
  } else if (xValue > (512 + deadZone)) { // Droite
    currentScreen++;
    if (currentScreen > 2) currentScreen = 0; // Retourne au premier écran
    delay(debounceDelay);
  }

  // Affichage des données selon l'écran sélectionné
  lcd.clear();
  if (currentScreen == 0) {
    // Afficher les données du capteur DHT11
    float temperature = dht.readTemperature();
    float humidite = dht.readHumidity();
    if (isnan(temperature) || isnan(humidite)) {
      lcd.print("Erreur capteur");
    } else {
      lcd.print("T:");
      lcd.print(temperature);
      lcd.print("C H:");
      lcd.print(humidite);
      lcd.print("%");
    }
  } else if (currentScreen == 1) {
    // Afficher les données du HC-SR04
    digitalWrite(TRIGPIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIGPIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGPIN, LOW);
    long duree = pulseIn(ECHOPIN, HIGH);
    float distance = duree * 0.034 / 2;
    lcd.print("Dist:");
    lcd.print(distance);
    lcd.print(" cm");
  } else if (currentScreen == 2) {
    // Afficher un message statique ou autre info
    lcd.print("Joystick Ready");
    lcd.setCursor(0, 1);
    lcd.print("Move to Navigate");
  }

  // Affichage du message "Coucou yannou" en appuyant sur le bouton
  if (swState == LOW) {
    lcd.clear();
    lcd.print("Coucou gabinou <3");
    delay(1000); // Affiche le message pendant 1 seconde
  }

  delay(500); // Petit délai pour rendre l'affichage fluide
}