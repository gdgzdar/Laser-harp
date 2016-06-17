#include <LiquidCrystal.h>
#include <Arduino.h>

class Display{
private:
	constant int X = 16;
	constant int Y = 4;
	int[6] lcdPinList;

public:

	Display(int pin1, int pin2, int pin3, int pin4, int pin5, int pin6){
		lcd.begin(X, Y);

		lcdPinList[0] = pin1;
		lcdPinList[1] = pin2;
		lcdPinList[2] = pin3;
		lcdPinList[3] = pin4;
		lcdPinList[4] = pin5;
		lcdPinList[5] = pin6;

		
	}

	void showMessage(string getLine1, string getLine2, string getLine3, string getLine4){
			lcd.setCursor(0, 1);
			lcd.print(textToCenter(getLine1));

			getLine2.lenght() <= 16){
			lcd.setCursor(1, 1);
			lcd.print(textToCenter(getLine2));

			lcd.setCursor(2, 1);
			lcd.print(textToCenter(getLine3));
		
			lcd.setCursor(3, 1);
			lcd.print(textToCenter(getLine4));

	}


	string textToCenter(string getMessage){
		int space;
		string messageForReturn = "";
		if(getMessage.lenght() <= 16){
			space = (16 - getMessage.lenght()) / 2;
			
			for(int q = 0; i < space ; q++){
				messageForReturn = messageForReturn + " ";
			}

			messageForReturn = messageForReturn + getMessage;

			for(int q = 0; i < space ; q++){
				messageForReturn = messageForReturn + " ";
			}
			return messageForReturn;
		}else{
			return "ERROR: SO LONG";
		}

	}

}
