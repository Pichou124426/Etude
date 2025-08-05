#include <Servo.h>
#include <LiquidCrystal.h>

Servo servoDeYann; 
LiquidCrystal lcd(7, 8, 9, 10, 11, 12); 
int currentScreen = 0;

void setup() {
    servoDeYann.attach(2); 
    lcd.begin(16, 2); 
    lcd.print("Coucou Yanou, JTM <3"); 
    delay(2000); // Pause avant de passer à autre chose
    lcd.clear(); // Effacer le message de bienvenue
}

void loop() {
    for (int position = 0; position <= 180; position += 1) { 
        servoDeYann.write(position); 
        lcd.clear(); // Effacer l'écran pour afficher la position actuelle
        lcd.print("Position: "); 
        lcd.print(position); 
        delay(15); 
    }

    for (int position = 180; position >= 0; position -= 1) { 
        servoDeYann.write(position); 
        lcd.clear(); 
        lcd.print("Position: "); 
        lcd.print(position); 
        delay(15); 
    }
}


