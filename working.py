import serial
import struct

# Raspberry Pi
# arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Ubuntu
# arduino = serial.Serial('/dev/ttyS0', 9600, timeout=1)

# Windows
arduino = serial.Serial('com3', 9600, timeout=1)

# [left, right, speed, pan, tilt]
# drive_straight_slowly = [2, 2, 50, 1, 1]


speed = 80
# Manual testing
# [left, right, speed, pan, tilt]
# forward: message[0] = 2, message[1] = 2
arduino.write(struct.pack('>BBBBB', 2, 2, speed, 1, 1))
# backward: message[0] = 0, message[1] = 0
arduino.write(struct.pack('>BBBBB', 0, 0, speed, 1, 1))
# spin_left: message[0] = 0; message[1] = 2
arduino.write(struct.pack('>BBBBB', 0, 2, speed, 1, 1))
# spin_right: message[0] = 2; message[1] = 0
arduino.write(struct.pack('>BBBBB', 2, 0, speed, 1, 1))
# forward_right: message[0] = 2; message[1] = 1
arduino.write(struct.pack('>BBBBB', 2, 1, speed, 1, 1))
# forward_left: message[0] = 1; message[1] = 2
arduino.write(struct.pack('>BBBBB', 1, 2, speed, 1, 1))
# stop: message[0] = 1; message[1] = 1
arduino.write(struct.pack('>BBBBB', 1, 1, speed, 1, 1))
# pan_left: message[3] = 0
arduino.write(struct.pack('>BBBBB', 1, 1, speed, 0, 1))
# no_pan: message[3] = 1
arduino.write(struct.pack('>BBBBB', 1, 1, speed, 1, 1))
# pan_right: message[3] = 2
arduino.write(struct.pack('>BBBBB', 1, 1, speed, 2, 1))
# tilt_up: message[4] = 2
arduino.write(struct.pack('>BBBBB', 1, 1, speed, 1, 2))
# no_tilt: message[3] = 1
arduino.write(struct.pack('>BBBBB', 1, 1, speed, 1, 1))
# tilt_down: message[4] = 0
arduino.write(struct.pack('>BBBBB', 1, 1, speed, 1, 0))

