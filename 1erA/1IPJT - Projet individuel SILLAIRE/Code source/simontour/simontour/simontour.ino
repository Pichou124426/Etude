#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1  
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Définition des LEDs et des boutons
#define LED_ROUGE 17
#define LED_VERT 5
#define LED_BLEU 19
#define LED_JAUNE 18

#define BTN_ROUGE 14  
#define BTN_VERT 15
#define BTN_BLEU 4
#define BTN_JAUNE 2

#define BUZZER_PIN 23

// Variables de jeu
int mode = 0;  // 1 = Basique, 2 = Aléatoire
int score = 0; 
int  meilleurScore = 0; 
int sequence[100];  
int gameIndex = 0;
unsigned long chronoStart;
bool soundEnabled = true;

void jouerSonBienvenue() {
  if (!soundEnabled) return;  
  
  tone(BUZZER_PIN, 523);  // NOTE C5
  delay(200);
  tone(BUZZER_PIN, 659);  // NOTE E5
  delay(200);
  tone(BUZZER_PIN, 784);  // NOTE G5
  delay(200);
  tone(BUZZER_PIN, 1047); // NOTE C6
  delay(400);
  noTone(BUZZER_PIN);
}
 // Fonction permettant de jouer le son en cas de défaite 
void jouerSonGameOver() {
  if (!soundEnabled) return;  
  
  tone(BUZZER_PIN, 500);
  delay(300);
  tone(BUZZER_PIN, 400);
  delay(300);
  tone(BUZZER_PIN, 300);
  delay(300);
  tone(BUZZER_PIN, 200);
  delay(300);
  tone(BUZZER_PIN, 100);
  delay(300);
  noTone(BUZZER_PIN);
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C); // Initialisation de l'écran avec la bibliothéque Adafruit via le protocole I2C
// Déclaration des differents boutons et leds en sorties ou entrées
  pinMode(LED_ROUGE, OUTPUT);
  pinMode(LED_VERT, OUTPUT);
  pinMode(LED_BLEU, OUTPUT);
  pinMode(LED_JAUNE, OUTPUT);
  pinMode(BTN_ROUGE, INPUT_PULLUP);
  pinMode(BTN_VERT, INPUT_PULLUP);
  pinMode(BTN_BLEU, INPUT_PULLUP);
  pinMode(BTN_JAUNE, INPUT_PULLUP);
  pinMode(BUZZER_PIN, OUTPUT);

  afficherMessage("Bienvenue", "Sur Simontour", 2000);
  jouerSonBienvenue();  

  afficherMenu();
}
// Une fonction qui me permet une unicité de polices dans mon jeu 
void afficherMessage(String ligne1, String ligne2, int delai) {
  display.clearDisplay();
  display.setTextSize(1);  
  display.setTextColor(WHITE);
  display.setCursor(10, 10);
  display.println(ligne1);
  display.setCursor(10, 30);
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
// Utilisation de la méthode PULL UP pour detecter la pression d'un bouton 
int detecterBouton() {
  if (digitalRead(BTN_BLEU) == LOW) return 1;
  if (digitalRead(BTN_JAUNE) == LOW) return 2;
  if (digitalRead(BTN_VERT) == LOW) return 3;
  if (digitalRead(BTN_ROUGE) == LOW) return 4;
  return 0;
}
// Affichage sur l'ecran lorsque la led s'allume 
void allumerLed(int led) {
  digitalWrite(LED_ROUGE, LOW);
  digitalWrite(LED_VERT, LOW);
  digitalWrite(LED_BLEU, LOW);
  digitalWrite(LED_JAUNE, LOW);

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(10, 10);
  display.println("Sequence...");
  display.setCursor(10, 30);
  
  switch (led) {
    case 1: digitalWrite(LED_BLEU, HIGH); display.println("BLEU"); break;
    case 2: digitalWrite(LED_JAUNE, HIGH); display.println("JAUNE"); break;
    case 3: digitalWrite(LED_VERT, HIGH); display.println("VERT"); break;
    case 4: digitalWrite(LED_ROUGE, HIGH); display.println("ROUGE"); break;
  }

  display.display();

  if (soundEnabled) {
    tone(BUZZER_PIN, 500 + (led * 100));
    delay(300);
    noTone(BUZZER_PIN);
  }
  
  delay(300);
  digitalWrite(LED_ROUGE, LOW);
  digitalWrite(LED_VERT, LOW);
  digitalWrite(LED_BLEU, LOW);
  digitalWrite(LED_JAUNE, LOW);
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
void ajouterPremiereSequenceBasique() {
   int longueurInitiale = random(2,4);
  for (int i = 0; i < longueurInitiale; i++) { 
    sequence[i] = random(1, 5); 
  }
  gameIndex = longueurInitiale;
}

void ajouterPremiereSequenceAleatoire() {
  int longueurInitiale = random(2,4);
  for (int i = 0; i < longueurInitiale; i++) { 
    sequence[i] = random(1, 5); 
  }
  gameIndex = longueurInitiale;
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
  chronoStart = millis();
  score = 0;

  // Ajout des trois premières couleurs selon le mode
  if (mode == 1) {
    ajouterPremiereSequenceBasique();
  } else {
    ajouterPremiereSequenceAleatoire();
  }

  while (true) {
    if (mode == 1) {
      ajouterNouvelleCouleurBasique();
    } else {
      ajouterNouvelleCouleurAleatoire();
    }

    afficherMessage("Sequence...", "", 1000);

    for (int i = 0; i < gameIndex; i++) {
      allumerLed(sequence[i]);  
      delay(500);
    }

    afficherMessage("A toi !", "", 1000);

    for (int i = 0; i < gameIndex; i++) {
      int boutonAppuye = 0;
      while (boutonAppuye == 0) {
        boutonAppuye = detecterBouton();
      }
      allumerLed(boutonAppuye);

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