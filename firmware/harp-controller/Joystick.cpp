class Joystick {
private:

	int pinY;
	int pinX;
	int pinButton;

	

	bool buttonPushed;

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

	int getButtonState() {
		return digitalRead(pinButton);
	}

	char getY() {
		int y = analogRead(pinY);

		if (y < 112){
			return 'L';
		}else if (y > 912){
			return 'R';
		}else{
			return 'N';
		}

	}

	char getX() {
		int x = analogRead(pinX);

		if (x < 112){
			return 'U';
		}else if (x > 912){
			return 'D';
		}else{
			return 'N';
		}
	}



};