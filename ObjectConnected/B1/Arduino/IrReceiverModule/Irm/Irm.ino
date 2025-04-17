#include <IRremote.hpp>
#include <LiquidCrystal.h>
#include <Servo.h>

#define IR_RECEIVE_PIN 3
Servo servoDeYann;
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
    Serial.begin(9600);
    IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);
    servoDeYann.attach(2);
    lcd.begin(16, 2);
    lcd.print("Appuyer bouton");
    delay(2000);
    lcd.clear();
}

void loop() {
    if (IrReceiver.decode()) { 
        Serial.print("Code IR reçu : ");
        Serial.println(IrReceiver.decodedIRData.command, HEX);

        lcd.clear();
        lcd.print("Code IR: ");
        lcd.print(IrReceiver.decodedIRData.command, HEX);
        delay(1000);

        switch (IrReceiver.decodedIRData.command) {
            case 0xC: // Bouton 1
                servoDeYann.write(0);
                lcd.clear();
                lcd.print("Servo: 0 deg");
                break;
            case 0x18: // Bouton 2
                servoDeYann.write(90);
                lcd.clear();
                lcd.print("Servo: 90 deg");
                break;
            case 0x5E: // Bouton 3
                servoDeYann.write(180);
                lcd.clear();
                lcd.print("Servo: 180 deg");
                break;
            default:
                lcd.clear();
                lcd.print("Code inconnu");
                break;
        }

        delay(2000);
        IrReceiver.resume(); // Préparer pour le prochain signal
    }
}