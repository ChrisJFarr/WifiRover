"""
Starter code for SSH app

Misc installation:

Open-cv
https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/

"""

# Determine if moving (if no change in sensor
# Look down until sensor starts to change

# Think about computer vision, what are some easy ones? Equipment challenge time?
import os
TEMP_WORKING_DIR = "/tmp/pycharm_project_465"
os.getcwd()
os.chdir(TEMP_WORKING_DIR)
os.system("ls")
import sys
sys.path = [TEMP_WORKING_DIR] + sys.path
import numpy as np
from app.src.rover import Rover
from time import time
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
# https://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html#:~:text=%22SSS%22%20is%20when%20we%20know,again%20to%20find%20another%20angle
# Tilt slightly to ensure accurate distance reading
# TODO Start here
# Function for determining angle of obstacle
side_c_midpoint = np.min([rover.read_distance() for _ in range(3)])
# Pan left

for _ in range(10):
    rover.pan_left()
    sleep(.15)
# Capture distance again


start = time()
side_a = np.min([rover.read_distance() for _ in range(3)])
print("%.2f" % (time() - start))
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

"""
# Steps to compute angle of wall
"""
# Measure distance from sensor to point on wall directly in front (using heading) (side D)
# Tilt slightly up and down to get a good read and avoid obstructions

# Measure distance using to obstacle ahead
# Tilt up
# Measure
# Recenter vertical
# Tilt down
# Measure
# Re-center vertical

# If computing angle from heading to the left
# Pan left
# Tilt up
# Measure
# Recenter vertical
# Tilt down
# Measure
# Re-center vertical and horizontal

# If computing angle from heading to the right
# Pan right
# Tilt up
# Measure
# Recenter vertical
# Tilt down
# Measure
# Re-center vertical and horizontal


# Pan to the left (or right) and again capture distance (side E)
# Perhaps while panning, ensure wall does not end using sensor
# If it ends then use the last known value prior to dropping off
# Calculate length of wall using pathagorem theorem (side F)
# Compute angle of the angle to the relative right of the robot (between sides D and F)


# TO use this output, this can work as a sensor reading for localization,
#  but can also be used for simple
# navigation to move about the room
# Using minimum distance from a sample seems to make sense when avoiding obstacles


"""
Function to calibrate motor speed to robot velocity
"""
# Compute the robot velocity and keep mapping to corresponding motor speed (ranges 0-255)
# Could standardize the motor speed options and calibrate each one
# May need to recalibrate depending on battery level and type of surface
# Perhaps this could also be a mechanism for measuring battery level
# Or battery needs to be determined and monitored for better localization

# Algorithm
# Align with a wall, adjust so heading is directly towards wall (90 degrees)
# Measure distance to wall (back up to allow 36 inches at least)
# Measure distance (A), ensure >= 36 inches
# Using desired calibration speed, drive towards wall for .5 seconds and stop
# Measure angle, and ensure still at 90 degrees (if not, start over? perhaps just once)
# Measure distance (B)
# Calculate velocity as inches traveled per second (A-B) / .5


"""
How does motor speed translate to rotation speed?
"""

# Measure the distance from wheel to wheel and inform robot
# Will that even help? Maybe it'll help with an estimate
# Perhaps with a quicker rotation I can compute the angle against the
#  same wall and get a more reliable reading.



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


"""

"""








