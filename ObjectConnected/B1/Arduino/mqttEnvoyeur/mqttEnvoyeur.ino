#include <WiFiNINA.h>
#include <ArduinoMqttClient.h>

const char ssid[] = "iPhone 12 Pro Max Yannick";
const char pass[] = "hexagone";

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);


const char broker[] = "test.mosquitto.org";
int port = 1883;
const char topic[] = "antoinev-hexagone";


void setup() {
  Serial.begin(9600);
  while (!Serial);


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
  mqttClient.poll();
  mqttClient.beginMessage(topic);
  mqttClient.print("Hello from MKR WiFi 1010");
  mqttClient.endMessage();
  Serial.println("Message envoyé");
  delay(30000);
}