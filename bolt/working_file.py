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


# from time import sleep
# 
# from pysphero.utils import toy_scanner
# 
# 
# def main():
#     with toy_scanner(timeout=50.0) as sphero:
#         sphero.power.wake()
#         sleep(2)
#         sphero.power.enter_soft_sleep()
# 
# 
# if __name__ == '__main__':
#     main()
# 
# from time import sleep
# 
# from pysphero.constants import Toy
# from pysphero.utils import toy_scanner
# from pysphero.core import Sphero
# # https://github.com/EnotYoyo/pysphero/blob/master/pysphero/core.py
# # ble_adapter_cls
# def main():
#     with Sphero(mac_address="DA:F4:35:74:09:03", toy_type=Toy.Sphero) as sphero:
#         sphero.power.wake()
#         sleep(2)
#         sphero.power.enter_soft_sleep()
#     pass
# 
# if __name__ == "__main__":
#     main()

 
import random
from time import sleep

from pysphero.core import Sphero
from pysphero.driving import Direction
from pysphero.bluetooth.bluepy_adapter import BluepyAdapter

def main():
    mac_address = "DA:F4:35:74:09:03"
    adapter = BluepyAdapter
    with Sphero(mac_address=mac_address, ble_adapter_cls=adapter) as sphero:
        sphero.power.wake()

        for _ in range(5):
            sleep(2)
            speed = random.randint(50, 100)
            heading = random.randint(0, 360)
            print(f"Send drive with speed {speed} and heading {heading}")

            sphero.driving.drive_with_heading(speed, heading, Direction.forward)

        sphero.power.enter_soft_sleep()
"""
THIS WORKED

Steps I took (not sure which impacted the final solution)
1. Installed dependencies: including gatt
2. Added contents described at top of page to the path
3. Scanned using bluetoothctl on the pi
4. Modified starter code and specified the mac address and BluepyAdapter

"""

if __name__ == "__main__":
    main()

