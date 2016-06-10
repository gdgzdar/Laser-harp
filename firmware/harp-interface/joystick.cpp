#include <Arduino.h>

class Joystick {
private:

	int pinY;
	int pinX;
	int pinButton;
  
	const int joystickCenterValue = 530;
	const int joystickTolerance = 400;

public:
	Joystick(int getPinY, int getPinX, int getPinButton) {
		this->pinY = getPinY;
		this->pinX = getPinX;
		this->pinButton = getPinButton;
	}

	int getAnalogY() {
		return analogRead(pinY);
	}

	int getAnalogX() {
		return analogRead(pinX);
	}

	bool getButtonState() {
		return (digitalRead(pinButton) == 0);
	}

	char getY() {
		int y = getAnalogY();
		if (y > (joystickCenterValue + joystickTolerance)) {
			return 'R';
		} else if (y < (joystickCenterValue - joystickTolerance)) {
			return 'L';
		} else {
			return 'N';
		}
	}

	char getX() {
		int x = getAnalogX();
		if (x > (joystickCenterValue + joystickTolerance)) {
			return 'U';
		} else if (x < (joystickCenterValue - joystickTolerance)) {
			return 'D';
		} else {
			return 'N';
		}
	}

};
