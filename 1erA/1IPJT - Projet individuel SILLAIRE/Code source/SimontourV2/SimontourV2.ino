#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1  
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define BTN_ROUGE 14  
#define BTN_VERT 15
#define BTN_BLEU 5 
#define BTN_JAUNE 2

#define BUZZER_PIN 23

int mode = 0;  
int score = 0;
int meilleurScore = 0;  
int sequence[100];  
int gameIndex = 0;
bool soundEnabled = true;

void jouerSonBienvenue() {
  if (!soundEnabled) return;  
  tone(BUZZER_PIN, 523); delay(200);
  tone(BUZZER_PIN, 659); delay(200);
  tone(BUZZER_PIN, 784); delay(200);
  tone(BUZZER_PIN, 1047); delay(400);
  noTone(BUZZER_PIN);
}

void jouerSonGameOver() {
  if (!soundEnabled) return;  
  tone(BUZZER_PIN, 500); delay(300);
  tone(BUZZER_PIN, 400); delay(300);
  tone(BUZZER_PIN, 300); delay(300);
  tone(BUZZER_PIN, 200); delay(300);
  tone(BUZZER_PIN, 100); delay(300);
  noTone(BUZZER_PIN);
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);

  pinMode(BTN_ROUGE, INPUT_PULLUP);
  pinMode(BTN_VERT, INPUT_PULLUP);
  pinMode(BTN_BLEU, INPUT_PULLUP);
  pinMode(BTN_JAUNE, INPUT_PULLUP);
  pinMode(BUZZER_PIN, OUTPUT);

  afficherMessage("Bienvenue", "Sur Simontour", 2000);
  jouerSonBienvenue();  
  afficherMenu();
}

void afficherMessage(String ligne1, String ligne2, int delai) {
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(10, 20);
  display.println(ligne1);
  display.setCursor(10, 40);
  display.println(ligne2);
  display.display();
  delay(delai);
}

void afficherMenu() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);

  display.setCursor(10, 10);
  display.println("1 - Mode Basique");
  display.setCursor(10, 20);
  display.println("2 - Mode Aleatoire");
  display.setCursor(10, 30);
  display.println("3 - Meilleur Score");
  display.setCursor(10, 40);
  display.println("4 - Son ON/OFF");

  display.display();
}

void afficherSequence(int led) {
  for (int i = 0; i < 3; i++) { 
    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(WHITE);
    display.setCursor(10, 20);
  
    switch (led) {
      case 1: display.println("BLEU"); break;
      case 2: display.println("JAUNE"); break;
      case 3: display.println("VERT"); break;
      case 4: display.println("ROUGE"); break;
    }

    display.display();
    delay(200);
    display.clearDisplay();
    display.display();
    delay(200);
  }
}

int detecterBouton() {
  int boutonAppuye = 0;
  while (boutonAppuye == 0) {
    if (digitalRead(BTN_BLEU) == LOW) boutonAppuye = 1;
    if (digitalRead(BTN_JAUNE) == LOW) boutonAppuye = 2;
    if (digitalRead(BTN_VERT) == LOW) boutonAppuye = 3;
    if (digitalRead(BTN_ROUGE) == LOW) boutonAppuye = 4;
  }

  afficherSequence(boutonAppuye); 
  delay(500); 
  return boutonAppuye;
}

void ajouterNouvelleCouleurBasique() {
  sequence[gameIndex] = random(1, 5);  
  gameIndex++;  
}

void ajouterNouvelleCouleurAleatoire() {
  for (int i = 0; i < gameIndex + 1; i++) {  
    sequence[i] = random(1, 5);  
  }
  gameIndex++;
}

void meilleurScoreJeu(int score) {
  if (score > meilleurScore) {  
    meilleurScore = score;  
  }

  afficherMessage("Meilleur Score", String(meilleurScore), 2000);
}

void lancerJeu(int modeChoisi) {
  mode = modeChoisi;
  gameIndex = 0;
  score = 0;

  while (true) {
    if (mode == 1) {
      ajouterNouvelleCouleurBasique();
    } else {
      ajouterNouvelleCouleurAleatoire();
    }

    afficherMessage("Sequence...", "", 1000);

    for (int i = 0; i < gameIndex; i++) {
      afficherSequence(sequence[i]);  
      delay(500);
    }

    afficherMessage("A toi !", "", 1000);

    for (int i = 0; i < gameIndex; i++) {
      int boutonAppuye = 0;
      while (boutonAppuye == 0) {
        boutonAppuye = detecterBouton();
      }
      afficherSequence(boutonAppuye);

      if (boutonAppuye != sequence[i]) {
        jouerSonGameOver();
        afficherMessage("Erreur !", "Score : " + String(score), 2000);
        return afficherMenu();
      }
    }

    score++;
  }
}

void loop() {
  int bouton = detecterBouton();

  if (bouton == 1) {
    lancerJeu(1);
  } else if (bouton == 2) {
    lancerJeu(2);
  } else if (bouton == 3) {
    meilleurScoreJeu(score);
    afficherMenu();
  } else if (bouton == 4) {
    soundEnabled = !soundEnabled;
    afficherMessage("Son:", soundEnabled ? "ON" : "OFF", 1000);
    afficherMenu();
  }
}