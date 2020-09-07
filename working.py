"""
Starter code for SSH app

Misc installation:

Open-cv
https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/

"""

# Determine if moving (if no change in sensor
# Look down until sensor starts to change

# Think about computer vision, what are some easy ones? Equipment challenge time?
import numpy as np
from app.src.rover import Rover
from time import sleep
# rover = Rover()
#
# rover.forward()
# rover.stop()
# rover.forward_left()
#
# rover.read_distance()
# rover.stop()
#
# rover.backward()
# rover.read_distance()
# rover.stop()
# rover.speed = 200

# Move until an obstacle is close (better safe than sorry)
"""
Obstacle avoid algorithm
1. Capture starting sensor value (inches)
    a. If within 24 inches, rotate right for short time (move ~25 degrees)
    b. Continue until have moved in 360 or sensor returns >=36 inches
2. Drive forward
    a. If sensor shows > 36 feet increase speed every second
    b. If sensor shows < 36 feet set speed to 80
3. Avoid obstacles
    a. If sensor show <= 24 inches stop
    b. Rotate to right 25 degrees
    c. Continue until sensor returns >= 36 inches
"""


# Initialize rover
rover = Rover()

# Get initial distance

MIN_SENSOR_VALUE = 24
MID_SENSOR_VALUE = 36
MAX_ROVER_SPEED = 250
SPEED_INCREMENT = 10
STARTING_SPEED = 80


def rotate_25_degrees():
    rover.spin_right()
    sleep(.75)
    rover.stop()

"""
Simple obstacle avoidance
"""
while True:

    sensor_value = rover.read_distance()
    if sensor_value <= MIN_SENSOR_VALUE:
        rotate_25_degrees()
    elif sensor_value > MID_SENSOR_VALUE:
        rover.speed = min(MAX_ROVER_SPEED, rover.speed + SPEED_INCREMENT)
        rover.forward()
    else:
        rover.speed = STARTING_SPEED
        rover.forward()
    sleep(.5)


# Good start above
# By only being able to turn 25 degrees to the right, the robot can
#  get stuck in some situations

# Detecting the angle of the surface in front of the robot
# could inform which is best to turn.
# Pan to the left, if sensor reads further, then left is better
# Pan to the right, if sensor reads further, then right is better
# If straight on to an obstacle, then perhaps back up or turn 180 degrees

"""
More dynamic obstacle avoidance
"""

# Estimate angle of obstacle ahead
# Capture starting distance
# Pan left, measure
# Pan right, measure
# Determine of A-C and C-B angle
from math import acos, degrees
# https://stackoverflow.com/questions/18583214/calculate-angle-of-triangle-python
# Tilt slightly to ensure accurate distance reading
# TODO Start here
# Function for determining angle of obstacle
side_c_midpoint = np.min([rover.read_distance() for _ in range(3)])
# Pan left
for _ in range(10):
    rover.pan_left()
    sleep(.15)
# Capture distance again
side_a = np.min([rover.read_distance() for _ in range(3)])
# Pan right
for _ in range(20):
    rover.pan_right()
    sleep(.15)
# Capture distance again
side_b = np.min([rover.read_distance() for _ in range(3)])
# Restraighten
for _ in range(10):
    rover.pan_left()
    sleep(.15)



import picamera.array
import picamera
import time

cam_resolution = (200, 200)
camera = picamera.PiCamera(resolution=cam_resolution)
time.sleep(2)
# Flip picture
camera.hflip = True
# camera.vflip = True
camera.rotation = 90

start = time.time()
with picamera.array.PiRGBArray(camera) as stream:
    camera.capture(stream, format='rgb')
    output_arr = stream.array
print("%.2f" % (time.time() - start))

from matplotlib import pyplot as plt

image = plt.imshow(output_arr)
plt.show()

output_arr.shape
