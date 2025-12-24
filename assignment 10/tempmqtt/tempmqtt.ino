#include <WiFi.h>
#include <ArduinoMqttClient.h>
#include <DHT.h>

const char *ssid = "AndroidAP_5063";
const char *password = "anaghaaa";

const char *host = "10.154.102.25";
  // FIXED
unsigned int port = 1883;

#define DHT_PIN 4
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

WiFiClient wifiClient;
MqttClient publisher(wifiClient);

void setup() {
  Serial.begin(115200);
  delay(1000);
  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  Serial.print("Connecting to MQTT...");
  if (!publisher.connect(host, port)) {
    Serial.println(" FAILED!");
    while (1);
  }
  Serial.println(" Connected!");
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

  String data = "{\"temperature\":" + String(temperature) +
                ",\"humidity\":" + String(humidity) + "}";

  publisher.beginMessage("reading/dht");
  publisher.print(data);
  publisher.endMessage();

  Serial.println("Published:");
  Serial.println(data); 

  delay(5000);
}
