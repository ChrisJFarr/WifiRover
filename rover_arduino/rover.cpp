#include <Servo.h> //include the servo library
#include <Adafruit_MotorShield.h>
#include <Wire.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
#include "rover.h"

Rover::Rover()
{
    // Motor setup
    AFMS = Adafruit_MotorShield();
    frontLeftMotor = AFMS.getMotor(FRONT_LEFT_MOTOR_PIN);
    backLeftMotor = AFMS.getMotor(BACK_LEFT_MOTOR_PIN);
    frontRightMotor = AFMS.getMotor(FRONT_RIGHT_MOTOR_PIN);
    backRightMotor = AFMS.getMotor(BACK_RIGHT_MOTOR_PIN);
}


// Begin AFMS
void Rover::begin()
{
    AFMS.begin();
    setWheelSpeed(0);  // Set starting speed to 0
    // Servo setup
    xServo.attach(X_SERVO_PIN);
    yServo.attach(Y_SERVO_PIN);
    xPos = X_START_POS; //declare initial position of the servo
    yPos = Y_START_POS; //declare initial position of the servo
    xServo.write(xPos);
    yServo.write(yPos);
}


// set left wheel direction: case message[0]: 0: backward 1: release 2: forward
void Rover::setLeftWheelDirection(int left){
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
void Rover::setRightWheelDirection(int right){
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
void Rover::setWheelSpeed(int speed){
    frontLeftMotor->setSpeed(speed);
    backLeftMotor->setSpeed(speed);
    frontRightMotor->setSpeed(speed);
    backRightMotor->setSpeed(speed);
}

// pan: if 0, SERVO_SPEED, if 1, no change, if 2 -SERVO_SPEED
void Rover::adjustPan(int pan){
    int newXPos;
    switch(pan)
    {
        case 0:
            newXPos = max(xPos + SERVO_SPEED, X_MIN);
            break;
        case 1:
            newXPos = xPos;
            break;
        case 2:
            newXPos = min(xPos - SERVO_SPEED, X_MAX);
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

// tilt: if 0, SERVO_SPEED, if 1, no change, if 2 -SERVO_SPEED
void Rover::adjustTilt(int tilt){
    int newYPos;
    switch(tilt)
    {
        case 0:
            newYPos = max(yPos + SERVO_SPEED, Y_MIN);
            break;
        case 1:
            newYPos = yPos;
            break;
        case 2:
            newYPos = min(yPos - SERVO_SPEED, Y_MAX);
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
