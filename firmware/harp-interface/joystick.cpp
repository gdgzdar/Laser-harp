#include <Arduino.h>

class Joystick {
private:

	int pinY;
	int pinX;
	int pinButton;
  
	const int joystickCenterValue = 530;
	const int joystickTolerance = 400;
	const char POSITION_RIGHT = 'R';
	const char POSITION_LEFT = 'L';
	const char POSITION_UP = 'U';
	const char POSITION_DOWN = 'D';
	const char POSITION_NEUTRAL = 'N';


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
		if (isJoystickBiasedRightOrUp(y)) {
			return POSITION_RIGHT;
		} else if (isJoystickBiasedLeftOrDown(y)) {
			return POSITION_LEFT;
		} else {
			return POSITION_NEUTRAL;
		}
	}

	char getX() {
		int x = getAnalogX();
		if (isJoystickBiasedRightOrUp(x)) {
			return POSITION_UP;
		} else if (isJoystickBiasedLeftOrDown(x)) {
			return POSITION_DOWN;
		} else {
			return POSITION_NEUTRAL;
		}
	}

	bool isJoystickBiasedRightOrUp(int coordinate) {
		return coordinate > (joystickCenterValue + joystickTolerance);
	}

	bool isJoystickBiasedLeftOrDown(int coordinate) {
		return coordinate < (joystickCenterValue - joystickTolerance);
	}

};
