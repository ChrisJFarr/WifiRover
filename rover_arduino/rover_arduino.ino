#include "robot.h"
#include <stdlib.h>
using namespace std;

// Declare constants
const int LEFT_INDEX = 0;
const int RIGHT_INDEX = 1;
const int SPEED_INDEX = 2;
const int PAN_INDEX = 3;
const int TILT_INDEX = 4;
const int LOOP_DELAY = 50;

// Declare variables
int incoming[5];
Robot robot;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //start serial port
  robot.begin();
  pinMode(LED_BUILTIN, OUTPUT); // initialize digital pin LED_BUILTIN as an output.
}

void loop() {
  // put your main code here, to run repeatedly:
  fillIncoming();
  // incoming[left, right, speed, pan, tilt]
  if(incoming[LEFT_INDEX] == 0)
  {
    digitalWrite(LED_BUILTIN, LOW);
  } else if(incoming[LEFT_INDEX] == 1)
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  robot.setLeftWheelDirection(incoming[LEFT_INDEX]);
  robot.setRightWheelDirection(incoming[RIGHT_INDEX]);
  robot.setWheelSpeed(incoming[SPEED_INDEX]);
  robot.adjustPan(incoming[PAN_INDEX]);
  robot.adjustTilt(incoming[TILT_INDEX]);
  delay(LOOP_DELAY);
}

void fillIncoming()
{
  // Fill incoming array with Serial.read()
  while (Serial.available() >= 5)
  {
    // fill array with loop
    for (int i = 0; i < 5; i++)
    {
      incoming[i] = Serial.read();
    }
  }
}
