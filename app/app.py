import io
from flask import Flask, render_template, request, make_response, send_file
import time

try:
    from src.rover import Rover
    import picamera.array
    import picamera
except ImportError as e:
    print(e)
    raise e

app = Flask(__name__)
rover = Rover()
try:
    # Picamera setup
    cam_resolution = (700, 700)
    camera = picamera.PiCamera(resolution=cam_resolution)
    time.sleep(2)
    # Flip picture
    camera.hflip = True
    # camera.vflip = True
    camera.rotation = 90
except ModuleNotFoundError as e:
    print(e)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/capture', methods=['GET', 'POST'])
def capture():
    start = time.time()
    with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='rgb')
        output_arr = stream.array.tobytes()
    print("%.2f" % (time.time() - start))
    return send_file(io.BytesIO(output_arr),
                     attachment_filename='capture.png',
                     mimetype='image/png')


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
    return make_response("")

# TODO Add sensor reading
@app.route("/read", methods=['GET'])
def sensor():
    sensor_response = rover.read_distance()
    return make_response(sensor_response)

# TODO Add new camera code or uncomment

# Route for main page
# Route for video feed (start with static image as a placeholder)
# Route for all rover operations


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
