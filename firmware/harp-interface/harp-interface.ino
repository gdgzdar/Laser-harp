#include "joystick.cpp"

Joystick* joystick;

void setup() {
  joystick = new Joystick(A4, A5, 13);
  Serial.begin(9600);
}

void loop() {
  Serial.print(joystick->getY());
  Serial.print("\n");
  Serial.print(joystick->getX());
  Serial.print("\n");
  Serial.print(joystick->getButtonState());
  Serial.print("\n");
  delay(500);
}
