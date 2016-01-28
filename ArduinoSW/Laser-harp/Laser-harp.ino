String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;


// První oktáva
int laser01 = 21;
int laser02 = 22;
int laser03 = 23;
int laser04 = 24;
int laser05 = 25;
int laser06 = 26;
int laser07 = 27;
int laser08 = 28;

// Druhá oktáva
int laser09 = 29;
int laser10 = 30;
int laser11 = 31;
int laser12 = 32;
int laser13 = 33;
int laser14 = 34;
int laser15 = 35;
int laser16 = 36;

// Třetí oktáva
int laser17 = 37;
int laser18 = 38;
int laser19 = 39;
int laser20 = 40;
int laser21 = 41;
int laser22 = 42;
int laser23 = 43;
int laser24 = 44;

int oktava1[8];
int oktava2[8];
int oktava3[8];


void setup() {                
  // initialize serial:
  Serial.begin(9600);
  inputString.reserve(200);
  
  pinMode(laser01, INPUT);
  pinMode(laser02, INPUT);
  pinMode(laser03, INPUT);
  pinMode(laser04, INPUT);
  pinMode(laser05, INPUT);
  pinMode(laser06, INPUT);
  pinMode(laser07, INPUT);
  pinMode(laser08, INPUT);

  pinMode(laser09, INPUT);  
  pinMode(laser10, INPUT);
  pinMode(laser11, INPUT);
  pinMode(laser12, INPUT);
  pinMode(laser13, INPUT);
  pinMode(laser14, INPUT);
  pinMode(laser15, INPUT);
  pinMode(laser16, INPUT);
  
  pinMode(laser17, INPUT);
  pinMode(laser18, INPUT);
  pinMode(laser19, INPUT);
  pinMode(laser20, INPUT);
  pinMode(laser21, INPUT);
  pinMode(laser22, INPUT);
  pinMode(laser23, INPUT);  
  pinMode(laser24, INPUT);  
}

void loop() {

oktava1[0] = digitalRead(laser01);
oktava1[1] = digitalRead(laser02);
oktava1[2] = digitalRead(laser03);
oktava1[3] = digitalRead(laser04);
oktava1[4] = digitalRead(laser05);
oktava1[5] = digitalRead(laser06);
oktava1[6] = digitalRead(laser07);
oktava1[7] = digitalRead(laser08);
  
sendOktava(oktava1);

oktava2[0] = digitalRead(laser09);
oktava2[1] = digitalRead(laser10);
oktava2[2] = digitalRead(laser11);
oktava2[3] = digitalRead(laser12);
oktava2[4] = digitalRead(laser13);
oktava2[5] = digitalRead(laser14);
oktava2[6] = digitalRead(laser15);
oktava2[7] = digitalRead(laser16);

sendOktava(oktava2);

oktava3[0] = digitalRead(laser17);
oktava3[1] = digitalRead(laser18);
oktava3[2] = digitalRead(laser19);
oktava3[3] = digitalRead(laser20);
oktava3[4] = digitalRead(laser21);
oktava3[5] = digitalRead(laser22);
oktava3[6] = digitalRead(laser23);
oktava3[7] = digitalRead(laser24);

sendOktava(oktava3);

delay(1000);



serialEvent(); //call the function
  // print the string when a newline arrives:
  if (stringComplete) {
    inputString.trim();
    Serial.println(inputString);
    
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}



void sendOktava(int* oktava) {
  for (int x=0; x<8; x++) {
    Serial.print(oktava[x]);      
  }
  Serial.println();
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

