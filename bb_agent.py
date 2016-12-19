#!/usr/bin/env python
from flask import Flask, render_template, Response
from build_butler import camera

app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return Response(gen(camera.Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/audio')
def audio():
	return "audio data"

@app.route('/sensors')
def sensors():
	return "sensors data"

@app.route('/controllers', methods=['POST'])
def controllers():
	return "Received control data"

if __name__ == '__main__':
    app.run()