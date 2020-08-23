"""
This is the working file for getting basic functionality to work connecting the pi to the bolt using pysphero.
https://pypi.org/project/pysphero/
"""




print("Hello")

"""
  The scripts blescan, sensortag and thingy52 are installed in '/home/pi/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  https://www.cyberciti.biz/faq/how-to-add-to-bash-path-permanently-on-linux/
"""

"""
Imports
"""
import random
from time import sleep

from pysphero.core import Sphero
from pysphero.driving import Direction
from pysphero.bluetooth.bluepy_adapter import BluepyAdapter


"""
Connectivity
"""

mac_address = "DA:F4:35:74:09:03"
adapter = BluepyAdapter
connect_to_bolt = lambda: Sphero(mac_address=mac_address, ble_adapter_cls=adapter)


"""
Working code to connect to bolt
"""


# def main():
# 
#     with Sphero(mac_address=mac_address, ble_adapter_cls=adapter) as sphero:
#         sphero.power.wake()
# 
#         for _ in range(5):
#             sleep(2)
#             speed = random.randint(50, 100)
#             heading = random.randint(0, 360)
#             print(f"Send drive with speed {speed} and heading {heading}")
# 
#             sphero.driving.drive_with_heading(speed, heading, Direction.forward)
# 
#         sphero.power.enter_soft_sleep()
# """
# THIS WORKED
# 
# Steps I took (not sure which impacted the final solution)
# 1. Installed dependencies: including gatt
# 2. Added contents described at top of page to the path
# 3. Scanned using bluetoothctl on the pi
# 4. Modified starter code and specified the mac address and BluepyAdapter
# 
# """
# 
# if __name__ == "__main__":
#     main()
    
    
from time import sleep
from typing import Dict

from pysphero.core import Sphero
from pysphero.device_api.sensor import CoreTime, Quaternion


def notify_callback(data: Dict):
    info = ", ".join("{:1.2f}".format(data.get(param)) for param in Quaternion)
    print(f"[{data.get(CoreTime.core_time):1.2f}] Quaternion (x, y, z, w): {info}")
    print("=" * 60)


def main():
    with connect_to_bolt() as sphero:
        sphero.power.wake()
        sphero.sensor.set_notify(notify_callback, CoreTime, Quaternion)
        sleep(2)
        sphero.sensor.cancel_notify_sensors()
        sphero.power.enter_soft_sleep()
# TODO Start here: Just got connectivity and reviewed the movement and sensor functions.
#  Next step is to continue building a flask API with the functions needed for localization.

# Future plan ideas:
#  * Bolt is the pup, the stationary picamera and time-of-flight sensor work together to map area


if __name__ == "__main__":
    main()


