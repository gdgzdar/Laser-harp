byte byteRead;
int randNumber = 0;
boolean laserField[26] = {false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false};

void setup() {                
// Turn the Serial Protocol ON
  Serial.begin(9600);
}

void loop() {

    laserField[random(26)] = random(2);


     for (int i = 0; i < 26; i++) {
        Serial.print(laserField[i]);
     }
     
      Serial.println("");
      for (int i = 0; i < 26; i++) {
        laserField[i] = false;
    }
    
}
