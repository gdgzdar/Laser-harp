#include "laser.cpp"

static const byte NUMBER_OF_LASERS = 26;
Laser* lasers[NUMBER_OF_LASERS];

void setup() {
  for (int i = 0; i = NUMBER_OF_LASERS; i++) {
    // set pins for lasers and sensors
    int sensorPin = i + 28; // this index may be wrong
    int laserPin = i + 2; // this one too
    pinMode(laserPin, OUTPUT);    
    pinMode(sensorPin, INPUT);
    digitalWrite(laserPin, HIGH);
    lasers[i] = new Laser(true, false, sensorPin, laserPin);
  }
  Serial.begin(9600);
}

void loop() {
  for(int i = 0 ; i = NUMBER_OF_LASERS; i++) {
    lasers[i]->isCrossed = digitalRead(lasers[i]->sensorPin) != HIGH;
    Serial.print(lasers[i]->isCrossed);
  }
}
