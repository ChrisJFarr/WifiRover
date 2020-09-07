import serial
import struct
from time import time


class Rover:

    def __init__(self):
        # Connect to arduino
        # self.arduino = serial.Serial('com3', 9600, timeout=1)
        self.arduino = self.connect()
        self.bit_str = ">BBBBBB"
        self.left = 1
        self.right = 1
        self.speed = 80
        self.pan = 1
        self.tilt = 1
        self.sense = 0

    def connect(self):
        try:
            arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        except Exception:
            try:
                arduino = serial.Serial('COM4', 9600, timeout=1)
            except Exception:
                raise Exception("Plug in that Arduino!")
        return arduino

    def write(self):
        self.arduino.write(struct.pack(self.bit_str, self.left, self.right,
                                       self.speed, self.pan, self.tilt, self.sense))
        
    def increase_speed(self):
        self.speed += 25
        
    def decrease_speed(self):
        self.speed -= 25
        self.speed = max(self.speed, 0)
        
    def forward(self):
        # self.arduino.write(struct.pack(self.bit_str, 2, 2, self.speed, 1, 1))
        self.left = 2
        self.right = 2
        self.write()
        print("forward")
        return

    def backward(self):
        # self.arduino.write(struct.pack(self.bit_str, 0, 0, self.speed, 1, 1))
        self.left = 0
        self.right = 0
        self.write()
        print("backward")
        return

    def spin_left(self):
        # self.arduino.write(struct.pack(self.bit_str, 0, 2, self.speed, 1, 1))
        self.left = 0
        self.right = 2
        self.write()
        print("spin_left")
        return

    def spin_right(self):
        # self.arduino.write(struct.pack(self.bit_str, 2, 0, self.speed, 1, 1))
        self.left = 2
        self.right = 0
        self.write()
        print("spin_right")
        return

    def forward_right(self):
        # self.arduino.write(struct.pack(self.bit_str, 2, 1, self.speed, 1, 1))
        self.left = 2
        self.right = 1
        self.write()
        print("forward_right")
        return

    def forward_left(self):
        # self.arduino.write(struct.pack(self.bit_str, 1, 2, self.speed, 1, 1))
        self.left = 1
        self.right = 2
        self.write()
        print("forward_left")
        return

    def stop(self):
        # self.arduino.write(struct.pack(self.bit_str, 1, 1, self.speed, 1, 1))
        self.left = 1
        self.right = 1
        self.write()
        print("stop")
        return

    def pan_left(self):
        # self.arduino.write(struct.pack(self.bit_str, 1, 1, self.speed, 0, 1))
        self.pan = 0
        self.write()
        self.pan = 1
        print("pan_left")
        return

    def pan_right(self):
        # self.arduino.write(struct.pack(self.bit_str, 1, 1, self.speed, 2, 1))
        self.pan = 2
        self.write()
        self.pan = 1
        print("pan_right")
        return

    def tilt_up(self):
        # self.arduino.write(struct.pack(self.bit_str, 1, 1, self.speed, 1, 2))
        self.tilt = 2
        self.write()
        self.tilt = 1
        print("tilt_up")
        return

    def tilt_down(self):
        # self.arduino.write(struct.pack(self.bit_str, 1, 1, self.speed, 1, 0))
        self.tilt = 0
        self.write()
        self.tilt = 1
        print("tilt_down")
        return

    def read_distance(self):
        print("start")
        start = time()
        self.sense = 1
        self.write()
        self.sense = 0
        print("read_distance")
        b_msg = self.arduino.readline()
        str_msg = b_msg.decode()
        print("stop")
        print("%.2f" % (time() - start))
        print("msg type", str(type(str_msg)))
        print("msg val", str(str_msg))
        return str_msg
