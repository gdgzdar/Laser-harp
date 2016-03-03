
boolean laserField[26] = {false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false};
boolean laserReaderAction = false;

int sensor1 = 1;

//First oktava
int sensor2 = 2;
int sensor3 = 3;
int sensor4 = 4;
int sensor5 = 5;
int sensor6 = 6;
int sensor7 = 7;
int sensor8 = 8;
int sensor9 = 9;

//Second oktava
int sensor10 = 10;
int sensor11 = 11;
int sensor12 = 12;
int sensor13 = 13;
int sensor14 = 14;
int sensor15 = 15;
int sensor16 = 16;
int sensor17 = 17;

//thirst oktava

int sensor18 = 18;
int sensor19 = 19;
int sensor20 = 20;
int sensor21 = 21;
int sensor22 = 22;
int sensor23 = 23;
int sensor24 = 24;
int sensor25 = 25;

int sensor26 = 26;

//--------------------------------------------------------------

int laser1 = 27;

int laser2 = 28;
int laser3 = 29;
int laser4 = 30;
int laser5 = 31;
int laser6 = 32;
int laser7 = 33;
int laser8 = 34;
int laser9 = 35;

int laser10 = 36;
int laser11 = 37;
int laser12 = 38;
int laser13 = 39;
int laser14 = 40;
int laser15 = 41;
int laser16 = 42;
int laser17 = 43;

int laser18 = 44;
int laser19 = 45;
int laser20 = 46;
int laser21 = 47;
int laser22 = 48;
int laser23 = 49;
int laser24 = 50;
int laser25 = 51;

int laser26 = 52;


void setup() {
	Serial.begin(115200); 

       pinMode(sensor1, INPUT);
       
       pinMode(sensor2, INPUT); 
       pinMode(sensor3, INPUT); 
       pinMode(sensor4, INPUT); 
       pinMode(sensor5, INPUT); 
       pinMode(sensor6, INPUT); 
       pinMode(sensor7, INPUT); 
       pinMode(sensor8, INPUT); 
       pinMode(sensor9, INPUT);
       
       pinMode(sensor10, INPUT); 
       pinMode(sensor11, INPUT);
       pinMode(sensor12, INPUT);
       pinMode(sensor13, INPUT); 
       pinMode(sensor14, INPUT); 
       pinMode(sensor15, INPUT); 
       pinMode(sensor16, INPUT);
       pinMode(sensor17, INPUT); 
       pinMode(sensor18, INPUT); 
       
       pinMode(sensor19, INPUT);
       pinMode(sensor20, INPUT);
       pinMode(sensor21, INPUT);
       pinMode(sensor22, INPUT);
       pinMode(sensor23, INPUT);
       pinMode(sensor24, INPUT);
       pinMode(sensor25, INPUT);
       
       pinMode(sensor26, INPUT);
       
  //------------------------------------------------------
  
       pinMode(laser1, INPUT);
       
       pinMode(laser2, INPUT); 
       pinMode(laser3, INPUT); 
       pinMode(laser4, INPUT); 
       pinMode(laser5, INPUT); 
       pinMode(laser6, INPUT); 
       pinMode(laser7, INPUT); 
       pinMode(laser8, INPUT); 
       pinMode(laser9, INPUT);
       
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
       pinMode(laser25, INPUT);
       
       pinMode(laser26, INPUT);
       
        
}
void loop() {
 
 
 
  if(laserReaderAction){
     LaserReader();
  }
}


static void LaserReader(){
  
  if(sensor1 == HIGH){
      laserField[0] = false;
  }else{
    laserField[0] = true;
  }
  
  
   if(sensor2 == HIGH){
      laserField[1] = false;
  }else{
    laserField[1] = true;
  }
  
  
   if(sensor3 == HIGH){
      laserField[2] = false;
  }else{
    laserField[2] = true;
  }
  
  
   if(sensor4== HIGH){
      laserField[3] = false;
  }else{
    laserField[3] = true;
  }
  
  
   if(sensor5 == HIGH){
      laserField[4] = false;
  }else{
    laserField[4] = true;
  }
  
   if(sensor6 == HIGH){
      laserField[5] = false;
  }else{
    laserField[5] = true;
  }
  
   if(sensor7 == HIGH){
      laserField[6] = false;
  }else{
    laserField[6] = true;
  }
  
   if(sensor8 == HIGH){
      laserField[7] = false;
  }else{
    laserField[7] = true;
  }
  
   if(sensor9 == HIGH){
      laserField[8] = false;
  }else{
    laserField[8] = true;
  }
  
   if(sensor10 == HIGH){
      laserField[9] = false;
  }else{
    laserField[9] = true;
  }
  
   if(sensor11 == HIGH){
      laserField[10] = false;
  }else{
    laserField[10] = true;
  }
  
   if(sensor12 == HIGH){
      laserField[11] = false;
  }else{
    laserField[11] = true;
  }
  
   if(sensor13 == HIGH){
      laserField[12] = false;
  }else{
    laserField[12] = true;
  }
  
   if(sensor14 == HIGH){
      laserField[13] = false;
  }else{
    laserField[13] = true;
  }
  
   if(sensor15 == HIGH){
      laserField[14] = false;
  }else{
    laserField[14] = true;
  }
  
   if(sensor16 == HIGH){
      laserField[15] = false;
  }else{
    laserField[15] = true;
  }
  
   if(sensor17 == HIGH){
      laserField[16] = false;
  }else{
    laserField[16] = true;
  }
  
   if(sensor18 == HIGH){
      laserField[17] = false;
  }else{
    laserField[17] = true;
  }
  
   if(sensor19 == HIGH){
      laserField[18] = false;
  }else{
    laserField[18] = true;
  }
  
   if(sensor20 == HIGH){
      laserField[19] = false;
  }else{
    laserField[19] = true;
  }
  
   if(sensor21 == HIGH){
      laserField[20] = false;
  }else{
    laserField[20] = true;
  }
  
   if(sensor22== HIGH){
      laserField[21] = false;
  }else{
    laserField[21] = true;
  }
  
   if(sensor23 == HIGH){
      laserField[22] = false;
  }else{
    laserField[22] = true;
  }
  
   if(sensor24 == HIGH){
      laserField[23] = false;
  }else{
    laserField[23] = true;
  }
  
   if(sensor25 == HIGH){
      laserField[24] = false;
  }else{
    laserField[24] = true;
  }
  
   if(sensor26 == HIGH){
      laserField[25] = false;
  }else{
    laserField[25] = true;
  }
  
}
