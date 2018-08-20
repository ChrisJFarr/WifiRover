import serial
import struct


class Rover:

    def __init__(self):
        # Connect to arduino
        self.arduino = serial.Serial('com3', 9600, timeout=1)
        self.speed = 80

    def forward(self):
        self.arduino.write(struct.pack('>BBBBB', 2, 2, self.speed, 1, 1))
        print("forward")
        return

    def backward(self):
        self.arduino.write(struct.pack('>BBBBB', 0, 0, self.speed, 1, 1))
        print("backward")
        return

    def spin_left(self):
        self.arduino.write(struct.pack('>BBBBB', 0, 2, self.speed, 1, 1))
        print("spin_left")
        return

    def spin_right(self):
        self.arduino.write(struct.pack('>BBBBB', 2, 0, self.speed, 1, 1))
        print("spin_right")
        return

    def forward_right(self):
        self.arduino.write(struct.pack('>BBBBB', 2, 1, self.speed, 1, 1))
        print("forward_right")
        return

    def forward_left(self):
        self.arduino.write(struct.pack('>BBBBB', 1, 2, self.speed, 1, 1))
        print("forward_left")
        return

    def stop(self):
        self.arduino.write(struct.pack('>BBBBB', 1, 1, self.speed, 1, 1))
        print("stop")
        return

    def pan_left(self):
        self.arduino.write(struct.pack('>BBBBB', 1, 1, self.speed, 0, 1))
        print("pan_left")
        return

    def pan_right(self):
        self.arduino.write(struct.pack('>BBBBB', 1, 1, self.speed, 2, 1))
        print("pan_right")
        return

    def tilt_up(self):
        self.arduino.write(struct.pack('>BBBBB', 1, 1, self.speed, 1, 2))
        print("tilt_up")
        return

    def tilt_down(self):
        self.arduino.write(struct.pack('>BBBBB', 1, 1, self.speed, 1, 0))
        print("tilt_down")
        return
