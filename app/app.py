from flask import Flask, render_template, request
try:
    from src.rover import Rover
except ImportError:
    pass

app = Flask(__name__)
rover = Rover()


@app.route("/")
def index():
    return render_template("index.html")


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
