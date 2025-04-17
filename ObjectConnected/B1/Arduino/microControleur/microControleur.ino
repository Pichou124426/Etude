
int latchPin = 11; // Pin connectée à la broche LATCH du 74HC595
int clockPin = 9;  // Pin connectée à la broche CLOCK du 74HC595
int dataPin = 12;  // Pin connectée à la broche DATA du 74HC595

byte leds = 0;     // Variable pour contrôler l'état des LED (0 = toutes éteintes)

void setup() {
  pinMode(latchPin, OUTPUT); // Configuration des pins en mode OUTPUT
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
}

void loop() {
  leds = 0; // Toutes les LED éteintes au début
  updateShiftRegister();
  delay(500);

  // Boucle pour allumer les LED une par une
  for (int i = 0; i < 8; i++) {
    bitSet(leds, i); // Modifier le bit correspondant à la LED
    updateShiftRegister();
    delay(500); // Pause entre chaque allumage/extinction
  }
}

void updateShiftRegister() {
  digitalWrite(latchPin, LOW); // Commencer la transmission des données
  shiftOut(dataPin, clockPin, LSBFIRST, leds); // Envoyer les données au registre
  digitalWrite(latchPin, HIGH); // Terminer la transmission des données
}