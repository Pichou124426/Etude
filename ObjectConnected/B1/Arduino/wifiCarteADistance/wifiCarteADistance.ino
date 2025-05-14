#include <WiFiNINA.h>

char ssid[] = "noahnoah";         // Nom du réseau Wi-Fi créé
char pass[] = "12345678";         // Mot de passe du réseau

int status = WL_IDLE_STATUS;
WiFiServer server(80);
int ledPin = LED_BUILTIN;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  while (!Serial);

  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Module WiFi non détecté");
    while (true);
  }

  Serial.print("Création du point d'accès nommé : ");
  Serial.println(ssid);

  status = WiFi.beginAP(ssid, pass);
  if (status != WL_AP_LISTENING) {
    Serial.println("Échec de la création du point d'accès");
    while (true);
  }

  delay(10000); // Attente de la stabilisation du point d'accès

  server.begin();
  printWifiStatus();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("Nouveau client");
    String currentLine = "";

    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);

        if (c == '\n') {
          if (currentLine.length() == 0) {
            // Envoi de la réponse HTTP avec une page HTML complète
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html;charset=utf-8");
            client.println();
            client.println("<!DOCTYPE html>");
            client.println("<html><head><title>Contrôle LED</title></head><body>");
            client.println("<h1>Contrôle de la LED</h1>");
            client.println("<p><a href=\"/A\">Allumer</a> | <a href=\"/E\">Éteindre</a></p>");
            client.println("</body></html>");
            client.println();
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }

        // Contrôle de la LED via l'URL
        if (currentLine.endsWith("GET /A")) {
          digitalWrite(ledPin, HIGH);
        }
        if (currentLine.endsWith("GET /E")) {
          digitalWrite(ledPin, LOW);
        }
      }
    }

    client.stop();
    Serial.println("Client déconnecté");
  }
}

void printWifiStatus() {
  Serial.print("SSID : ");
  Serial.println(WiFi.SSID());

  IPAddress ip = WiFi.localIP();
  Serial.print("Adresse IP : ");
  Serial.println(ip);
}