import io
from flask import Flask, render_template, request, Response, send_file
import time
import numpy as np
import picamera

try:
    from src.rover import Rover    
except ImportError as e:
    print(e)
    pass

app = Flask(__name__)
rover = Rover()
cam_resolution = (700, 700)
camera = picamera.PiCamera(resolution=cam_resolution)
time.sleep(2)
# Flip picture
camera.hflip = True
#camera.vflip = True
camera.rotation = 90
# stream = io.BytesIO()


@app.route("/")
def index():
    return render_template("index.html")

"""
Resources for picamera/numpy/flask
Get numpy from picamera: https://www.programcreek.com/python/example/88717/picamera.array
Send numpy through flask p1: https://stackoverflow.com/questions/11017466/flask-to-return-image-stored-in-database/25150805#25150805
Send numpy through flask p2: https://stackoverflow.com/questions/54899367/send-numpy-array-as-bytes-from-python-to-js-through-flask
General fyi: https://picamera.readthedocs.io/en/release-1.13/api_array.html
"""


# @app.route('/video_feed', methods=['GET', 'POST'])
# def video_feed():
#     start = time.time()
#     camera.capture(stream, 'jpeg')
#     stream.seek(0)
#     image = stream.read()
#     stream.seek(0)
#     stream.truncate()
#     response = Response(image, mimetype='image/gif')
#     print("%.2f" % (time.time() - start))
#     return response

@app.route('/video_feed', methods=['GET', 'POST'])
def video_feed():
    start = time.time()
#     data = np.empty((cam_resolution[1],cam_resolution[0],3),dtype=np.uint8)
#     # different edge detection methods
#     camera.capture(data,'rgb') # capture image
#     response = Response(data)  # , mimetype='image/gif')
    with picamera.array.PiRGBArray(camera) as stream:
#         if isDay:
#             camera.exposure_mode = 'auto'
#             camera.awb_mode = 'auto'
#             time.sleep(motionCamSleep)   # sleep so camera can get AWB
#         else:
#             # use variable framerate_range for Low Light motion image stream
#             camera.framerate_range = (Fraction(1, 6), Fraction(30, 1))
#             time.sleep(2) # Give camera time to measure AWB
#             camera.iso = nightMaxISO
        camera.capture(stream, format='rgb')
        camera.close()
        output_arr = stream.array.tobytes()
        
    print("%.2f" % (time.time() - start))
    
    return send_file(io.BytesIO(output_arr),
                     attachment_filename='capture.png',
                     mimetype='image/png')
# TODO Try running as-is
# TODO Then, Go to canvas and checkout the challenge code for tips on picamera framerate



@app.route("/run", methods=['POST'])
def run():
    command = request.form["data"]
    switch = {
        "forward_left": rover.forward_left,
        "forward": rover.forward,
        "forward_right": rover.forward_right,
        "spin_left": rover.spin_left,
        "spin_right": rover.spin_right,
        "backward": rover.backward,
        "stop": rover.stop,
        "tilt_up": rover.tilt_up,
        "tilt_down": rover.tilt_down,
        "pan_left": rover.pan_left,
        "pan_right": rover.pan_right
    }
    switch[command]()
    return ""


# Route for main page
# Route for video feed (start with static image as a placeholder)
# Route for all rover operations


if __name__ == "__main__":
    app.run("0.0.0.0")
