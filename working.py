import requests

response = requests.get("http://192.168.1.201:5000/video_feed")
dir(response)

dir(response.raw.data)
response.json

response.raw
response.content
import imageio

url = "https://example_url.com/image.jpg"

# image is going to be type <class 'imageio.core.util.Image'>
# that's just an extension of np.ndarray with a meta attribute
from time import time

start = time()
image = imageio.imread("http://192.168.1.201:5000/video_feed")
print("%.2f" % (time() - start))

requests.get("http://192.168.1.201:5000/video_feed")


from matplotlib import pyplot as plt

plt.imshow(image)

plt.show()

image.shape


# Try to get a sensor read:
import time
# If slow: https://github.com/psf/requests/issues/4023

start = time.time()
response = requests.get("http://localhost:5000/read", headers={"Connection": "close"})
print(response.json())
print("Seconds: %.2f" % (time.time() - start))


start = time.time()
response = requests.get("http://192.168.1.157/read")
print(response.json())
print("Seconds: %.2f" % (time.time() - start))


# Set position of servo, relative to center


