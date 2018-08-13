#include <Servo.h> //include the servo library
#include <Adafruit_MotorShield.h>
#include <Wire.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
#include "robot.h"

Robot::Robot()
{
    // Servo setup
    xServo.attach(X_SERVO_PIN);
    yServo.attach(Y_SERVO_PIN);
    xPos = X_START_POS; //declare initial position of the servo
    yPos = Y_START_POS; //declare initial position of the servo
    // Motor setup
    AFMS = Adafruit_MotorShield();
    frontLeftMotor = AFMS.getMotor(FRONT_LEFT_MOTOR_PIN);
    backLeftMotor = AFMS.getMotor(BACK_LEFT_MOTOR_PIN);
    frontRightMotor = AFMS.getMotor(FRONT_RIGHT_MOTOR_PIN);
    backRightMotor = AFMS.getMotor(BACK_RIGHT_MOTOR_PIN);
}


// Begin AFMS
void Robot::begin()
{
    AFMS.begin();
    setWheelSpeed(0);  // Set starting speed to 0
}


// set left wheel direction: case message[0]: 0: backward 1: release 2: forward
void Robot::setLeftWheelDirection(int left){
    switch(left)
    {
        case 0:
            // backwards
            frontLeftMotor->run(BACKWARD);
            backLeftMotor->run(BACKWARD);
            break;
        case 1:
            // stop
            frontLeftMotor->run(RELEASE);
            backLeftMotor->run(RELEASE);
            break;
        case 2:
            // forwards
            frontLeftMotor->run(FORWARD);
            backLeftMotor->run(FORWARD);
            break;
        default:
            break;
    }
}

// set right wheel direction: case message[1]: 0: backward 1: release 2: forward
void Robot::setRightWheelDirection(int right){
    switch(right)
    {
        case 0:
            // backwards
            frontRightMotor->run(BACKWARD);
            backRightMotor->run(BACKWARD);
            break;
        case 1:
            // stop
            frontRightMotor->run(RELEASE);
            backRightMotor->run(RELEASE);
            break;
        case 2:
            // forwards
            frontRightMotor->run(FORWARD);
            backRightMotor->run(FORWARD);
            break;
        default:
            break;
    }
}

// set wheel speed: message[2]
void Robot::setWheelSpeed(int speed){
    frontLeftMotor->setSpeed(speed);
    backLeftMotor->setSpeed(speed);
    frontRightMotor->setSpeed(speed);
    backRightMotor->setSpeed(speed);
}

// pan: if 0, -SERVO_SPEED, if 1, no change, if 2 SERVO_SPEED
void Robot::adjustPan(int pan){
    int newXPos;
    switch(pan)
    {
        case 0:
            newXPos = xPos - SERVO_SPEED;
            break;
        case 1:
            break;
        case 2:
            newXPos = xPos + SERVO_SPEED;
            break;
        default:
            break;
    }

    while(newXPos != xPos)
    {
        xServo.write(xPos); //write the position into the servo
        delay(SERVO_DELAY); //give time to the servo to reach the position
        if(xPos < newXPos)
        {
            xPos++;
        } else {
            xPos--;
        }
    }
    return;
}

// tilt: if 0, -SERVO_SPEED, if 1, no change, if 2 SERVO_SPEED
void Robot::adjustTilt(int tilt){
    int newYPos;
    switch(tilt)
    {
        case 0:
            newYPos = yPos - SERVO_SPEED;
            break;
        case 1:
            break;
        case 2:
            newYPos = yPos + SERVO_SPEED;
            break;
        default:
            break;
    }
    while(newYPos != yPos)
    {
        yServo.write(yPos); //write the position into the servo
        delay(SERVO_DELAY); //give time to the servo to reach the position
        if(yPos < newYPos)
        {
            yPos++;
        } else {
            yPos--;
        }
    }
    return;
}
