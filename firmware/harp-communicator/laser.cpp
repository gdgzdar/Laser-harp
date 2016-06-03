class Laser {
public:
 
  bool isOn;
  bool isCrossed;
  int sensorPin;
  int laserPin;


  Laser(bool isOn, bool isCrossed, int sensorPin, int laserPin) {
    this->isOn = isOn;
    this->isCrossed = isCrossed;
    this->sensorPin = sensorPin;
    this->laserPin = laserPin;
  }

};
