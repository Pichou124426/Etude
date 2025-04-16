#include <LiquidCrystal.h>
#include <DHT.h>
#include <WiFi.h>
#include <ThingSpeak.h>

// Initialisation de l'écran LCD (pins 7, 8, 9, 10, 11, 12)
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

// Définition du capteur DHT11
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

// Informations pour la connexion Wi-Fi et ThingSpeak
const char* ssid = "Galaxy A42 5G7766";     // Remplacez par votre nom de réseau Wi-Fi
const char* password = "Yann0411";          // Remplacez par votre mot de passe Wi-Fi
const char* apiKey = "S4RYLKHMMK9ZVSAU";    // Remplacez par votre clé API ThingSpeak
unsigned long channelNumber = 2921646;      // Numéro de canal ThingSpeak

WiFiClient client;

// Variables pour gérer le menu et le joystick
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

  // Connexion au Wi-Fi
  lcd.setCursor(0, 1);
  lcd.print("Connexion WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    lcd.setCursor(0, 1);
    lcd.print(".");
  }
  lcd.clear();
  lcd.print("WiFi Connecte!");
  delay(2000);

  // Initialisation de ThingSpeak
  ThingSpeak.begin(client);
}

void loop() {
  // Lecture des données du joystick
  int xValue = analogRead(VRX);
  int yValue = analogRead(VRY);
  int swState = digitalRead(SW);
 

  // Navigation dans le menu avec le joystick
  if (xValue < (512 - deadZone)) { // Incliné vers la gauche
    currentScreen--;
    if (currentScreen < 0) currentScreen = 2; // Retourne au dernier écran
    delay(debounceDelay);
  } else if (xValue > (512 + deadZone)) { // Incliné vers la droite
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
    // Écran statique ou message personnalisé
    lcd.print("Joystick Ready");
    lcd.setCursor(0, 1);
    lcd.print("Move to Navigate");
  }

  // Affichage du message spécial en appuyant sur le bouton
  if (swState == LOW) {
    lcd.clear();
    lcd.print("Coucou gabinou <3");
    delay(1000); // Affiche le message pendant 1 seconde
  }

  // Envoi des données à ThingSpeak
  float temperature = dht.readTemperature();
  float humidite = dht.readHumidity();
  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGPIN, LOW);
  long duree = pulseIn(ECHOPIN, HIGH);
  float distance = duree * 0.034 / 2;

  ThingSpeak.setField(1, temperature); // Champ 1 : Température
  ThingSpeak.setField(2, humidite);    // Champ 2 : Humidité
  ThingSpeak.setField(3, distance);    // Champ 3 : Distance

  ThingSpeak.writeFields(channelNumber, apiKey);

  delay(20000); // Temps avant le prochain envoi (limite ThingSpeak)
}
