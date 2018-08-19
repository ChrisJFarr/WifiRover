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


@app.route("/drive", methods=['POST'])
def drive():
    command = request.form["data"]
    switch = {
        "up_left": rover.forward_left,
        "up": rover.forward,
        "up_right": rover.forward_right,
        "left": rover.spin_left,
        "right": rover.spin_right,
        "down": rover.backward,
        "stop": rover.stop
    }
    switch[command]()
    return ""

# Route for main page
# Route for video feed (start with static image as a placeholder)
# Route for all rover operations


if __name__ == "__main__":
    app.run("0.0.0.0")
