#include <ArduinoBLE.h>
#include <DHT.h>

const int ledPin = LED_BUILTIN;
const int dhtPin = 2;
DHT dht(dhtPin, DHT11);

BLEService ledService("906b4f26-fe64-4859-bed7-203a97d34783");
BLEByteCharacteristic switchCharacteristic("906b4f26-fe64-4859-bed7-203a97d34783", BLERead | BLEWrite);
BLECharacteristic tempCharacteristic("00002a1f-0000-1000-8000-00805f9b34fb", BLERead | BLEWrite | BLENotify, 20);
BLECharacteristic humCharacteristic("00002a6f-0000-1000-8000-00805f9b34fb", BLERead | BLEWrite | BLENotify, 20);

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  while (!Serial);

  if (!BLE.begin()) {
    Serial.println("Erreur d'initialisation du BLE !");
    while (1);
  }

  dht.begin();

  BLE.setLocalName("MKR1010_Antoine");
  BLE.setAdvertisedService(ledService);
  ledService.addCharacteristic(switchCharacteristic);
  ledService.addCharacteristic(tempCharacteristic);
  ledService.addCharacteristic(humCharacteristic);
  BLE.addService(ledService);

  switchCharacteristic.writeValue(0);
  BLE.advertise();

  Serial.println("Périphérique BLE prêt");
}

void loop() {
  BLEDevice central = BLE.central();

  if (central) {
    Serial.print("Connecté à : ");
    Serial.println(central.address());

    while (central.connected()) {
      if (switchCharacteristic.written()) {
        if (switchCharacteristic.value()) {
          Serial.println("LED ON");
          digitalWrite(ledPin, HIGH);
        } else {
          Serial.println("LED OFF");
          digitalWrite(ledPin, LOW);
        }
      }

      float temperature = dht.readTemperature();
      float humidity = dht.readHumidity();

      if (isnan(temperature) || isnan(humidity)) {
        Serial.println("Échec de la lecture du capteur DHT11");
      } else {
        String tempStr = String(temperature, 2);
        String humStr = String(humidity, 2);

        String tempMessage = "Temp: " + tempStr + " °C";
        String humMessage = "Hum: " + humStr + " %";

        tempCharacteristic.setValue(tempMessage.c_str());
        humCharacteristic.setValue(humMessage.c_str());

        Serial.print("Température: ");
        Serial.print(tempStr);
        Serial.print(" °C\tHumidité: ");
        Serial.print(humStr);
        Serial.println(" %");

        delay(2000);
      }
    }

    Serial.print("Déconnecté de : ");
    Serial.println(central.address());
  }
}