from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

process = None  # global process


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/start-camera')
def start_camera():
    global process

    if process is None:
        file_path = os.path.join(os.getcwd(), "trained.py")
        process = subprocess.Popen(["python", file_path])
        return "Drowsiness Detection Started!"
    else:
        return "Already Running!"


@app.route('/stop-camera')
def stop_camera():
    global process

    if process:
        process.kill()   # 🔥 force stop
        process = None
        return "Stopped Successfully!"
    else:
        return "Not Running!"


if __name__ == '__main__':
    app.run(debug=True)