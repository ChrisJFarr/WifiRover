import os
import io
print(os.getcwd())
from flask import Flask, render_template, request, Response
import time
try:
    from src.rover import Rover
    from src.camera_pi import Camera
    import picamera
except ImportError as e:
    print(e)
    pass

app = Flask(__name__)
rover = Rover()
camera = picamera.PiCamera()
time.sleep(2)
# Flip picture
camera.hflip = True
camera.vflip = True
stream = io.BytesIO()

@app.route("/")
def index():
    return render_template("index.html")



@app.route('/video_feed', methods=['GET','POST'])
def video_feed():
    print("getting image")
    camera.capture(stream, 'jpeg')
    stream.seek(0)
    image = stream.read()
    stream.seek(0)
    stream.truncate()
    return Response(image, mimetype='image/gif')


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
