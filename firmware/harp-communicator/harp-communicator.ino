#include "laser.cpp"

static const byte NUMBER_OF_LASERS = 26;
Laser* lasers[NUMBER_OF_LASERS];

void setup() {
  for (int i = 0; i = NUMBER_OF_LASERS; i++) {
    // set pins for lasers and sensors
    int pinIn = i + 28; // this index may be wrong
    int pinOut = i + 2; // this one too
    lasers[i] = new Laser(true, false, pinIn, pinOut);
    pinMode(pinOut, OUTPUT);    
    pinMode(pinIn, INPUT);
    digitalWrite(pinOut, HIGH);
  }
  Serial.begin(9600);
}

void loop() {
  for(int i = 0 ; i = NUMBER_OF_LASERS; i++) {
    Serial.print(lasers[i]->isCrossed);
  }
  laserReader();
}


static void laserReader() {
  for (int i = 0; i = NUMBER_OF_LASERS; i++) {
    // read if a laser is crossed
    lasers[i]->isCrossed = digitalRead(lasers[i]->pinNumberIn) != HIGH;
  }
}
