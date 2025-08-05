#include <WiFiNINA.h>
#include <ArduinoHttpClient.h>
#include <LiquidCrystal.h>
#include <ArduinoJson.h>

LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

// Broches du capteur ultrason
const int trigPin = 14;
const int echoPin = 13;

// Paramètres Wi-Fi
char ssid[] = "Galaxy A42 5G7766";
char pass[] = "Yann0411";

// Serveur Make.com (HTTPS)
const char makeServer[] = "hook.eu2.make.com";
const int makePort = 443;
const char webhookPath[] = "/rll48fxe61ruxgz1q4j2q3uzsm5q1tuy";

// Clients Wi-Fi
WiFiSSLClient wifiSSL;

void setup() {
  lcd.begin(16, 2); // Initialiser l'écran LCD
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Connexion au Wi-Fi
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nConnecté au WiFi !");
}

void loop() {
  long duration;
  float distance;

  // Envoi de l’impulsion
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Lecture de l’écho
  duration = pulseIn(echoPin, HIGH);

  // Calcul de la distance en cm
  distance = duration * 0.034 / 2;
  lcd.setCursor(0, 0);
  lcd.print("Distance : ");
  lcd.print(distance);
  Serial.print("Distance : ");
  Serial.print(distance);
  Serial.println(" cm");

  // ----------- Envoi à Make.com avec JSON -----------

  // Créer le document JSON avec ArduinoJson
  StaticJsonDocument<128> jsonDoc;
  jsonDoc["distance"] = distance; // Ajouter la donnée de distance

  // Convertir le document JSON en texte brut
  String jsonString;
  serializeJson(jsonDoc, jsonString);

  HttpClient clientMake(wifiSSL, makeServer, makePort);

  clientMake.beginRequest();
  clientMake.post(webhookPath); // Envoyer au chemin du webhook
  clientMake.sendHeader("Content-Type", "application/json"); // Définir le type de contenu
  clientMake.sendHeader("Content-Length", jsonString.length()); // Définir la longueur du corps
  clientMake.sendHeader("Connection", "close");
  clientMake.print(jsonString); // Envoyer le JSON dans le corps
  clientMake.endRequest();

  int statusCodeMake = clientMake.responseStatusCode();
  String responseMake = clientMake.responseBody();

  Serial.print("Make.com HTTP : ");
  Serial.println(statusCodeMake);
  Serial.print("Réponse : ");
  Serial.println(responseMake);

  clientMake.stop();

  delay(2000);
}