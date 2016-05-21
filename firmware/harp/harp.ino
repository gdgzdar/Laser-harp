boolean laserReaderAction = false;

static const byte NUMBER_OF_LASERS = 26;

static int sensorList[NUMBER_OF_LASERS];
static int laserList[NUMBER_OF_LASERS];
boolean statesOfLasers[NUMBER_OF_LASERS];


void setup() {

  for(int i = 0; i <= NUMBER_OF_LASERS; i++)
  {
    sensorList[i] = i + 2;
    pinMode(sensorList[i], INPUT);
    
    laserList[i] = i + 28;
    pinMode(laserList[i], OUTPUT);
    digitalWrite(laserList[i], HIGH);

    statesOfLasers[i] = false;
  }

  Serial.begin(9600);        
}

void loop() {

  for(int i = 0 ; i < NUMBER_OF_LASERS; i++){
    pinMode(sensorList[i], INPUT);
    Serial.println(sensorList[i]);
  }
  delay(10000);
 
  if(laserReaderAction){
     LaserReader();
  }
}


static void LaserReader(){

  for (int i = 0; i < NUMBER_OF_LASERS; i++) {
    statesOfLasers[i] = sensorList[i] != HIGH;
  }
  
}
