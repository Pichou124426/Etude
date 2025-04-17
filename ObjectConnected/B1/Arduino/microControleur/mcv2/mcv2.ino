int lightPin = 0; // Pin analogique connectée à la photorésistance
int latchPin = 11; // Pin connectée à la broche LATCH du 74HC595
int clockPin = 9;  // Pin connectée à la broche CLOCK du 74HC595
int dataPin = 12;  // Pin connectée à la broche DATA du 74HC595

byte leds = 0; // Variable pour contrôler l'état des LED

void setup() {
  pinMode(latchPin, OUTPUT); // Configuration des pins en mode OUTPUT
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
}

void loop() {
  int reading = analogRead(lightPin); // Lecture de la photorésistance
  int numLEDSLit = reading / 57; // Conversion de la luminosité en nombre de LED (1kΩ)

  leds = 0; // Réinitialiser les LED
  for (int i = 0; i < numLEDSLit; i++) {
    bitSet(leds, i); // Activer le bit correspondant à la LED
  }
  updateShiftRegister(); // Mettre à jour les LED
}

void updateShiftRegister() {
  digitalWrite(latchPin, LOW); // Commencer la transmission des données
  shiftOut(dataPin, clockPin, LSBFIRST, leds); // Envoyer les données au registre
  digitalWrite(latchPin, HIGH); // Terminer la transmission des données
}