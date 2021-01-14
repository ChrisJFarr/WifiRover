import os
TEMP_WORKING_DIR = "/tmp/pycharm_project_465"
os.getcwd()
os.chdir(TEMP_WORKING_DIR)
os.system("ls")
import sys
sys.path = [TEMP_WORKING_DIR] + sys.path
from app.src.rover import Rover
from time import sleep

os.listdir()

rover = Rover()

while True:
    print("inches", rover.read_distance())
    sleep(.5)
