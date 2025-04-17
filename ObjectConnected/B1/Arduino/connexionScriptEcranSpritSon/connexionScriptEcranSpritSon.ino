
#include <WiFiNINA.h>
#include <ArduinoHttpClient.h>
#include <LiquidCrystal.h>




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

// Serveur ThingSpeak (HTTP)
const char tsServer[] = "api.thingspeak.com";
const int tsPort = 80;
String apiKey = "PAQNEMITDQHPF48Y";

// Clients Wi-Fi
WiFiClient wifiClient;
WiFiSSLClient wifiSSL;

void setup() {
  lcd.begin(16, 2); // Initialize the LCD screen
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
  lcd.setCursor(0, 0); // Set cursor to the first row, first column
  lcd.print("Distance : ");
  lcd.print(distance);
  Serial.print("Distance : ");
  Serial.print(distance);
  Serial.println(" cm");

  // ----------- Envoi à Make.com -----------
  HttpClient clientMake(wifiSSL, makeServer, makePort);
  String urlMake = String(webhookPath) + "?distance=" + String(distance);

  clientMake.beginRequest();
  clientMake.post(urlMake);
  clientMake.sendHeader("Content-Type", "application/x-www-form-urlencoded");
  clientMake.sendHeader("Connection", "close");
  clientMake.endRequest();

  int statusCodeMake = clientMake.responseStatusCode();
  String responseMake = clientMake.responseBody();

  Serial.print("Make.com HTTP : ");
  Serial.println(statusCodeMake);
  Serial.print("Réponse : ");
  Serial.println(responseMake);

  clientMake.stop();

  // ----------- Envoi à ThingSpeak -----------
  HttpClient clientTS(wifiClient, tsServer, tsPort);
  String urlTS = "/update?api_key=" + apiKey + "&field1=" + String(distance);

  clientTS.beginRequest();
  clientTS.get(urlTS);
  clientTS.sendHeader("Connection", "close");
  clientTS.endRequest();

  int statusCodeTS = clientTS.responseStatusCode();
  String responseTS = clientTS.responseBody();

  Serial.print("ThingSpeak HTTP : ");
  Serial.println(statusCodeTS);
  Serial.print("Réponse : ");
  Serial.println(responseTS);

  clientTS.stop();

  delay(20000);
}