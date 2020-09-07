import requests
import numpy as np
from matplotlib import pyplot as plt
from time import time

"""
Working file for client-side app

Build an app class that an AI can work with.

"""

pi_address = "http://192.168.1.201:80/"
capture = pi_address + "capture"
sense = pi_address + "read"
move = pi_address + "run"

"""
Get sensor read
"""
start = time()
response = requests.get(sense)
print(response.json())
print("%.2f" % (time() - start))

"""
Get image array
"""
start = time()
response = requests.get(capture)
check = np.frombuffer(response.content, dtype=np.uint8)
check = np.reshape(check, newshape=(200, 200, 3))
print("%.2f" % (time() - start))

plt.imshow(check)
plt.show()

"""
Drive
"""
# Send post with data
requests.post(move, data={"data": "stop"})

requests.post(move, data={"data": "forward"})
requests.post(move, data={"data": "forward_left"})
requests.post(move, data={"data": "forward_right"})
requests.post(move, data={"data": "spin_left"})
requests.post(move, data={"data": "spin_right"})
requests.post(move, data={"data": "backward"})
requests.post(move, data={"data": "tilt_up"})
requests.post(move, data={"data": "tilt_down"})
requests.post(move, data={"data": "pan_left"})
requests.post(move, data={"data": "pan_right"})

requests.post(move, data={"data": "increase_speed"})
requests.post(move, data={"data": "decrease_speed"})

plt.imshow(check)
plt.show()



requests.get("http://192.168.1.201:5000/video_feed")






