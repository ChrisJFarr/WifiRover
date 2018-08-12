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
    Adafruit_MotorShield AFMS = Adafruit_MotorShield();
    frontLeftMotor = AFMS.getMotor(FRONT_LEFT_MOTOR_PIN);
    backLeftMotor = AFMS.getMotor(BACK_LEFT_MOTOR_PIN);
    frontRightMotor = AFMS.getMotor(FRONT_RIGHT_MOTOR_PIN);
    backRightMotor = AFMS.getMotor(BACK_RIGHT_MOTOR_PIN);
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
    // set servo pan: x += message[3]
void Robot::addToPan(int degrees){

}
    // set servo tilt: y += message[3]
void Robot::addToTilt(int degrees){

}
