// První oktáva
int laserIN01 = 21;
int laserIN02 = 22;
int laserIN03 = 23;
int laserIN04 = 24;
int laserIN05 = 25;
int laserIN06 = 26;
int laserIN07 = 27;
int laserIN08 = 28;

// Druhá oktáva
int laserIN09 = 29;
int laserIN10 = 30;
int laserIN11 = 31;
int laserIN12 = 32;
int laserIN13 = 33;
int laserIN14 = 34;
int laserIN15 = 35;
int laserIN16 = 36;

// Třetí oktáva
int laserIN17 = 37;
int laserIN18 = 38;
int laserIN19 = 39;
int laserIN20 = 40;
int laserIN21 = 41;
int laserIN22 = 42;
int laserIN23 = 43;
int laserIN24 = 44;


// První oktáva
int laser01;
int laser02;
int laser03;
int laser04;
int laser05;
int laser06;
int laser07;
int laser08;

// Druhá oktáva
int laser09;
int laser10;
int laser11;
int laser12;
int laser13;
int laser14;
int laser15;
int laser16;

// Třetí oktáva
int laser17;
int laser18;
int laser19;
int laser20;
int laser21;
int laser22;
int laser23;
int laser24;


int oktava1[8] = {laser01, laser02, laser03, laser04, laser05, laser06, laser07, laser08};
int oktava2[8] = {laser09, laser10, laser11, laser12, laser13, laser14, laser15, laser16};
int oktava3[8] = {laser17, laser18, laser19, laser20, laser21, laser22, laser23, laser24};


void setup() {                
  Serial.begin(9600);
  pinMode(laserIN01, INPUT);
  pinMode(laserIN02, INPUT);
  pinMode(laserIN03, INPUT);
  pinMode(laserIN04, INPUT);
  pinMode(laserIN05, INPUT);
  pinMode(laserIN06, INPUT);
  pinMode(laserIN07, INPUT);
  pinMode(laserIN08, INPUT);
  
  pinMode(laserIN09, INPUT);  
  pinMode(laserIN10, INPUT);
  pinMode(laserIN11, INPUT);
  pinMode(laserIN12, INPUT);
  pinMode(laserIN13, INPUT);
  pinMode(laserIN14, INPUT);
  pinMode(laserIN15, INPUT);
  pinMode(laserIN16, INPUT);
  
  pinMode(laserIN17, INPUT);
  pinMode(laserIN18, INPUT);
  pinMode(laserIN19, INPUT);
  pinMode(laserIN20, INPUT);
  pinMode(laserIN21, INPUT);
  pinMode(laserIN22, INPUT);
  pinMode(laserIN23, INPUT);  
  pinMode(laserIN24, INPUT);  
}

void loop() {

oktava1[0] = digitalRead(laserIN01);
oktava1[1] = digitalRead(laserIN02);
oktava1[2] = digitalRead(laserIN03);
oktava1[3] = digitalRead(laserIN04);
oktava1[4] = digitalRead(laserIN05);
oktava1[5] = digitalRead(laserIN06);
oktava1[6] = digitalRead(laserIN07);
oktava1[7] = digitalRead(laserIN08);
  
oktava2[0] = digitalRead(laserIN09);
oktava2[1] = digitalRead(laserIN10);
oktava2[2] = digitalRead(laserIN11);
oktava2[3] = digitalRead(laserIN12);
oktava2[4] = digitalRead(laserIN13);
oktava2[5] = digitalRead(laserIN14);
oktava2[6] = digitalRead(laserIN15);
oktava2[7] = digitalRead(laserIN16);

oktava3[0] = digitalRead(laserIN17);
oktava3[1] = digitalRead(laserIN18);
oktava3[2] = digitalRead(laserIN19);
oktava3[3] = digitalRead(laserIN20);
oktava3[4] = digitalRead(laserIN21);
oktava3[5] = digitalRead(laserIN22);
oktava3[6] = digitalRead(laserIN23);
oktava3[7] = digitalRead(laserIN24);



}
