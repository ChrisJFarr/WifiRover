cmake_minimum_required(VERSION 3.10)
project(WifiRover)

set(CMAKE_CXX_STANDARD 11)

add_executable(WifiRover rover_arduino.ino rover.cpp rover.h worker_list)
