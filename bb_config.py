#!/usr/bin/env python
import cv2
import sys
from sklearn.decomposition import RandomizedPCA
import cv2
import os.path
import string
import time
from build_butler import constants, vision
from build_butler.textToSpeech import tts

if(len(sys.argv) < 2 or sys.argv[1] == ""):
    print("Please enter a name")
    exit()

NAME=sys.argv[1]

faceCascade = cv2.CascadeClassifier(constants.CASC_PATH)

video_capture = cv2.VideoCapture(0)

if not os.path.exists(constants.TRAIN_DIR):
    os.makedirs(constants.TRAIN_DIR)

if not os.path.exists(constants.TRAIN_DIR + '/' + NAME):
    os.makedirs(constants.TRAIN_DIR + '/' + NAME)

tts.say("Hello, I am the build butler")
tts.say("Welcome to the team")
tts.say("To begin, please look at the camera with a neutral expression")
tts.say("Once your face is selected, slowly change your expression, lighting and tilt")

i=0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=constants.SCALE_FACTOR,
        minNeighbors=constants.MIN_NEIGHBORS,
        minSize=(constants.MIN_WIDTH, constants.MIN_HEIGHT),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        x, y, w, h = vision.resize(x, y, w, h)
        vision.draw_rectangle(frame, x, y, w, h)
        face = frame[y:y+h, x:x+w]
        resized = cv2.resize(face, (constants.WIDTH, constants.HEIGHT))
        grayscale = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
        write_filename=constants.TRAIN_DIR + NAME + '/grayscale-' + str(i) + '.png'
        print(write_filename)
        cv2.imwrite(write_filename, grayscale)
        i = i+1

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
