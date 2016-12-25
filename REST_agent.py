#!/usr/bin/env python
from flask import Flask, render_template, Response
from build_butler import camera
import speech_recognition as sr
import cv2

app = Flask(__name__)
video_capture = cv2.VideoCapture(0)
r = sr.Recognizer()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return Response(gen(camera.Camera(video_capture)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/audio')
def audio():
    with sr.Microphone() as source:
            audio = r.listen(source)
    return audio

@app.route('/sensors')
def sensors():
	return "sensors data"

@app.route('/controllers', methods=['POST'])
def controllers():
	return "Received control data"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
    video_capture.release()