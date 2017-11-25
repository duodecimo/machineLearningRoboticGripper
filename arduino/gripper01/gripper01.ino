#include <Servo.h>

#define svrLeftRightPort 4
#define svrUpDownPort 5
#define svrFowardBackPort 6
#define svrGripLoosePort 7

//encode servos designation
#define svrLeftRight 0
#define svrUpDown 1
#define svrFowardBack 2
#define svrGripLoose 3

#define STEP 2

// headers
void up();
void down();
void left();
void right();
void foward();
void back();
void grip();
void loose();

// create servo objects to control GripLoose servos.
// a maximum of eight servo objects can be created 
Servo svr[4];
int pos[4];
int posInc[4];
int ind = 0;
char a;

void setup() 
{
  // attach servos on logic pins
  svr[svrLeftRight].attach(svrLeftRightPort);
  pos[svrLeftRight]=70;
  posInc[svrLeftRight]=0;
  svr[svrUpDown].attach(svrUpDownPort);
  pos[svrUpDown]=80;
  posInc[svrUpDown]=0;
  svr[svrFowardBack].attach(svrFowardBackPort);
  pos[svrFowardBack]=20;
  posInc[svrFowardBack]=0;
  svr[svrGripLoose].attach(svrGripLoosePort);
  pos[svrGripLoose]=30;
  posInc[svrGripLoose]=0;
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  svr[svrLeftRight].write(pos[svrLeftRight]);
  svr[svrUpDown].write(pos[svrUpDown]);
  svr[svrFowardBack].write(pos[svrFowardBack]);
  svr[svrGripLoose].write(pos[svrGripLoose]);
  delay(1000);
}

void loop() {
  // serial comunication with computer (python)

  while(Serial.available()) {

    a = Serial.read();
    if(a == 'f') foward();
    else if(a == 'b') back();
    else if(a == 'l') left();
    else if(a == 'r') right();
    else if(a == 'u') up();
    else if(a == 'd') down();
    else if(a == 'g') grip();
    else if(a == 'o') loose();
    Serial.print("received: ");
    Serial.println(a);
    delay(60);
  }
}

void right() {
  if(posInc[svrLeftRight]>=-15+STEP) { 
    posInc[svrLeftRight] -= STEP;
    svr[svrLeftRight].write(pos[svrLeftRight]+posInc[svrLeftRight]);
  }
}

void left() {
  if(posInc[svrLeftRight]<=15-STEP) { 
    posInc[svrLeftRight] += STEP;
    svr[svrLeftRight].write(pos[svrLeftRight]+posInc[svrLeftRight]);
  }
}

void down() {
  if(posInc[svrUpDown]>=-25+STEP) { 
    posInc[svrUpDown] -= STEP;
    svr[svrUpDown].write(pos[svrUpDown]+posInc[svrUpDown]);
  }
}

void up() {
  if(posInc[svrUpDown]<=25-STEP) { 
    posInc[svrUpDown] += STEP;
    svr[svrUpDown].write(pos[svrUpDown]+posInc[svrUpDown]);
  }
}

void back() {
  if(posInc[svrFowardBack]>=-25+STEP) { 
    posInc[svrFowardBack] -= STEP;
    svr[svrFowardBack].write(pos[svrFowardBack]+posInc[svrFowardBack]);
  }
}

void foward() {
  if(posInc[svrFowardBack]<=25-STEP) { 
    posInc[svrFowardBack] += STEP;
    svr[svrFowardBack].write(pos[svrFowardBack]+posInc[svrFowardBack]);
  }
}

void loose() {
  if(posInc[svrGripLoose]>=-15+STEP) { 
    posInc[svrGripLoose] -= STEP;
    svr[svrGripLoose].write(pos[svrGripLoose]+posInc[svrGripLoose]);
  }
}

void grip() {
  if(posInc[svrGripLoose]<=15-STEP) { 
    posInc[svrGripLoose] += STEP;
    svr[svrGripLoose].write(pos[svrGripLoose]+posInc[svrGripLoose]);
  }
}


