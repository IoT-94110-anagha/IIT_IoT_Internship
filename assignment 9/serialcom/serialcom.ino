void setup() {
  Serial.begin(9600);
  Serial.println("UART setup is done");
}

int count = 0;

void loop() {
  Serial.print("count = ");
  Serial.println(count);
  count++;
  delay(2000);
}
