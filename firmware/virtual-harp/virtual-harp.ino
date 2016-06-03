const int NUMBER_OF_STRINGS = 26;

void setup() {
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < NUMBER_OF_STRINGS; i++) {
    Serial.print(int(isTheStringPlaying()));
  }
  Serial.println();
}

boolean isTheStringPlaying() {
  return random(20) > 18;
}

