#include <Servo.h> //include the servo library
#include <Adafruit_MotorShield.h>
#include <Wire.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

class Robot {

    /* Declare constants */

    // motor constants

    const int FRONT_LEFT_MOTOR_PIN = 1;
    const int BACK_LEFT_MOTOR_PIN = 2;
    const int FRONT_RIGHT_MOTOR_PIN = 3;
    const int BACK_RIGHT_MOTOR_PIN = 4;

    // servo constants
    const int X_SERVO_PIN = 9;
    const int Y_SERVO_PIN = 10;
    const int SERVO_DELAY = 5; //delay to allow the servo to reach position;
    const int SERVO_SPEED = 5; // Steps per servo adjustment call
    const int X_START_POS = 90;
    const int Y_START_POS = 175;

    /* Declare Variables */
//    int message[5];  // [left, right, speed, pan delta, tilt delta]

    // motor variable
    //  Adafruit_MotorShield AFMS;
    Adafruit_MotorShield AFMS;
    Adafruit_DCMotor *frontLeftMotor, *backLeftMotor, *frontRightMotor, *backRightMotor;

    // servo variables
    Servo xServo, yServo; // create a servo object called myServo
    int xPos, yPos; //declare position of the servo

    // servo variables
public:
    Robot();
    // begin program
    void begin();
    // set left wheel direction: case message[0]: 0: backward 1: release 2: forward
    void setLeftWheelDirection(int left);
    // set right wheel direction: case message[1]: 0: backward 1: release 2: forward
    void setRightWheelDirection(int right);
    // set wheel speed: message[2]
    void setWheelSpeed(int speed);
    // set servo pan: x += message[3]
    void adjustPan(int pan);
    // set servo tilt: y += message[3]
    void adjustTilt(int tilt);

};
