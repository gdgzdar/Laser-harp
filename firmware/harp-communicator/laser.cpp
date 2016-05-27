class Laser {
public:
 
  bool isOn;
  bool isCrossed;
  int pinNumberIn;
  int pinNumberOut;


  Laser(bool isOn, bool isCrossed, int pinNumberIn, int pinNumberOut) {
    this->isOn = isOn;
    this->isCrossed = isCrossed;
    this->pinNumberIn = pinNumberIn;
    this->pinNumberOut = pinNumberOut;
  }

};

