#include <WiFiNINA.h>
#include <ArduinoMqttClient.h>


const char ssid[] = "iPhone (3)";
const char pass[] = "azerty01";


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


  mqttClient.setId("arduinoSubscriber");
  mqttClient.setUsernamePassword("", "");


  if (!mqttClient.connect(broker, port)) {
    Serial.print("Échec de connexion MQTT : ");
    Serial.println(mqttClient.connectError());
    while (1);
  }
  Serial.println("Connecté au broker MQTT");


  mqttClient.subscribe(topic);
  Serial.println("Abonné au topic : " + String(topic));
}

void loop() {
  mqttClient.poll();
  int messageSize = mqttClient.parseMessage();
  if (messageSize) {
    Serial.print("Message reçu [");
    Serial.print(mqttClient.messageTopic());
    Serial.print("]: ");
    while (mqttClient.available()) {
      char c = (char)mqttClient.read();
      Serial.print(c);
    }
    Serial.println();
  }
}


