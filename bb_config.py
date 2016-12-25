#!/usr/bin/env python
import cv2
import sys
from sklearn.decomposition import RandomizedPCA
import numpy as np
import glob
import cv2
import math
import os.path
import string
import time

ROOT="build_butler/detection/"

#function to get ID from filename
def ID_from_filename(filename):
    if(filename == None):
        raise "Must specify filename"
    part = filename.split('/')
    return part[1].replace("s", "")
 
def resize(x, y, w, h):
    # If it's wider
    if( w/h > RATIO):
        # Expand width
        extra_width = (92 * h / 112) - w
        w = w + extra_width
        x = x - (extra_width / 2)
    # If it's narrower
    else:
        # Expand height
        extra_height = (112 * w / 92) - h
        h = h + extra_height
        y = y - (extra_height / 2)
    return int(x), int(y), int(w), int(h)

def draw_rectangle(x, y, w, h):
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return

IMG_RES = 92 * 112 # img resolution
RATIO = 92/112

cascPath = ROOT + 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

if not os.path.exists('teammates'):
    os.makedirs('teammates')

if not os.path.exists('teammates/' + sys.argv[1]):
    os.makedirs('teammates/' + sys.argv[1])

i=0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(70, 90),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        x, y, w, h = resize(x, y, w, h)
        draw_rectangle(x, y, w, h)
        face = frame[y:y+h, x:x+w]
        resized = cv2.resize(face, (92, 112))
        grayscale = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
        cv2.imwrite('teammates/' + sys.argv[1] + '/grayscale-' + str(i) + '.png', grayscale)
        i = i+1

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
