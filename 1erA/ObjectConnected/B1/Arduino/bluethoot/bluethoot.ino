#include <ArduinoBLE.h>
/* Utiliser nRF Connect */


const int ledPin = LED_BUILTIN;
BLEService ledService("19B10000-E8F2-537E-4F6C-D104768A1214");
BLEByteCharacteristic switchCharacteristic("19B10001-E8F2-537E-4F6C-D104768A1214", BLERead | BLEWrite);


void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  while (!Serial);


  if (!BLE.begin()) {
    Serial.println("Erreur d'initialisation du BLE !");
    while (1);
  }


  BLE.setLocalName("MKR1010_LED");
  BLE.setAdvertisedService(ledService);
  ledService.addCharacteristic(switchCharacteristic);
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
    }


    Serial.print("Déconnecté de : ");
    Serial.println(central.address());
  }
}