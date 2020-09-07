#include "rover.h"
#include <VL53L0X.h>
#include <stdlib.h>
using namespace std;

// Declare constants
const int LEFT_INDEX   = 0;
const int RIGHT_INDEX  = 1;
const int SPEED_INDEX  = 2;
const int PAN_INDEX    = 3;
const int TILT_INDEX   = 4;
const int SENSOR_INDEX = 5;
const int LOOP_DELAY   = 50;

// Declare variables
int incoming[6];
bool messageWaiting;
Rover rover;
VL53L0X sensor;


// Uncomment ONE of these two lines to get
// - higher speed at the cost of lower accuracy OR
// - higher accuracy at the cost of lower speed

//#define HIGH_SPEED
#define HIGH_ACCURACY

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //start serial port
  pinMode(LED_BUILTIN, OUTPUT); // initialize digital pin LED_BUILTIN as an output.
  // Initialize rover and sensor
  rover.begin();
  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1) {}
  }


#if defined LONG_RANGE
  // lower the return signal rate limit (default is 0.25 MCPS)
  sensor.setSignalRateLimit(0.1);
  // increase laser pulse periods (defaults are 14 and 10 PCLKs)
  sensor.setVcselPulsePeriod(VL53L0X::VcselPeriodPreRange, 18);
  sensor.setVcselPulsePeriod(VL53L0X::VcselPeriodFinalRange, 14);
#endif

#if defined HIGH_SPEED
  // reduce timing budget to 20 ms (default is about 33 ms)
  sensor.setMeasurementTimingBudget(20000);
#elif defined HIGH_ACCURACY
  // increase timing budget to 200 ms
  sensor.setMeasurementTimingBudget(200000);
#endif

}

void loop() {
  // put your main code here, to run repeatedly:
  fillIncoming();
  // incoming[left, right, speed, pan, tilt]
  if (incoming[LEFT_INDEX] == 0)
  {
    digitalWrite(LED_BUILTIN, LOW);
  } else if (incoming[LEFT_INDEX] == 1)
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  if (messageWaiting)
  {
    rover.setLeftWheelDirection(incoming[LEFT_INDEX]);
    rover.setRightWheelDirection(incoming[RIGHT_INDEX]);
    rover.setWheelSpeed(incoming[SPEED_INDEX]);
    rover.adjustPan(incoming[PAN_INDEX]);
    rover.adjustTilt(incoming[TILT_INDEX]);
    if (incoming[SENSOR_INDEX] == 1){
      // Send sensor reading
      Serial.println(sensor.readRangeSingleMillimeters());
    }
    messageWaiting = false;
  }
  delay(LOOP_DELAY);
}

void fillIncoming()
{
  // Fill incoming array with Serial.read()
  while (Serial.available() >= 6)
  {
    // fill array with loop
    for (int i = 0; i < 6; i++)
    {
      incoming[i] = Serial.read();
    }
    messageWaiting = true;
  }
}
