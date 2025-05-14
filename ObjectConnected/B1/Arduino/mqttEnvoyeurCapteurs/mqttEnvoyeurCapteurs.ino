#include <WiFiNINA.h>
#include <ArduinoMqttClient.h>
#include <DHT.h>


#define DHTPIN 2 // Le capteur est connecté au port 2
#define DHTTYPE DHT11

const char ssid[] = "iPhone (3)";
const char pass[] = "azerty01";

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);
DHT dht(DHTPIN, DHTTYPE);

const char broker[] = "test.mosquitto.org";
int port = 1883;
const char topic[] = "antoinev-hexagone";

void setup() {
  Serial.begin(9600);
  while (!Serial);

  dht.begin();

  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connexion au WiFi...");
  }
  Serial.println("Connecté au WiFi");

  mqttClient.setId("arduinoPublisher");
  mqttClient.setUsernamePassword("", "");

  if (!mqttClient.connect(broker, port)) {
    Serial.print("Échec de connexion MQTT : ");
    Serial.println(mqttClient.connectError());
    while (1);
  }
  Serial.println("Connecté au broker MQTT");
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Erreur de lecture du capteur DHT11");
    return;
  }

  mqttClient.poll();
  mqttClient.beginMessage(topic);
  mqttClient.print("Voici des données particulières ;)  ");
  mqttClient.print("Température: ");
  mqttClient.print(temperature);
  mqttClient.print("°C, Humidité: ");
  mqttClient.print(humidity);
  mqttClient.print("%");
  mqttClient.endMessage(); 

  Serial.println("Données envoyées");
  delay(30000);
}