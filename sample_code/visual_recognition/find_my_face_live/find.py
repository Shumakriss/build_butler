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

#function to get ID from filename
def ID_from_filename(filename):
    if(filename == None):
        raise "Must specify filename"
    part = filename.split('/')
    return part[1].replace("s", "")
 
#function to convert image to right format
def prepare_image(filename):
    img_color = cv2.imread(filename)
    #img_gray = cv2.cvtColor(img_color, cv2.cv.CV_RGB2GRAY)
    #Updated for opencv3
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    return img_gray.flat

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

def find_person(Y):
    #print("Attemping to recognize face")
    # load test faces (usually one), located in folder test_faces
    test_faces = glob.glob('test_faces/*')

    # Create an array with flattened images X
    X = np.zeros([len(test_faces), IMG_RES], dtype='int8')
     
    # Populate test array with flattened imags from subfolders of train_faces 
    # This looks wrong to me
    for i, face in enumerate(test_faces):
        X[i,:] = prepare_image(face)

    # run through test images (usually one)
    for j, ref_pca in enumerate(pca.transform(X)):
        distances = []
        # Calculate euclidian distance from test image to each of the known images and save distances
        for i, test_pca in enumerate(X_pca):
            dist = math.sqrt(sum([diff**2 for diff in (ref_pca - test_pca)]))
            distances.append((dist, Y[i]))
            
        eigenDistance = min(distances)[0]
        found_ID = min(distances)[1]

        if(eigenDistance < 1.5):
            print("Confidence is high: " + str(eigenDistance))
            print("Best Match: " + str(found_ID))
        #else:
        #    print("Confidence is low: " + str(eigenDistance))
        #    print("Best Match: " + str(found_ID))

        #print "Identified (result: "+ str(found_ID) +" - dist - " + str(min(distances)[0])  + ")"
    return

IMG_RES = 92 * 112 # img resolution
RATIO = 92/112
NUM_EIGENFACES = 10 # images per train person
NUM_TRAINIMAGES = 120 # total images in training set

#loading training set from folder train_faces
folders = glob.glob('train_faces/*')
 
# Create an array with flattened images X
# and an array with ID of the people on each image y
X = np.zeros([NUM_TRAINIMAGES, IMG_RES], dtype='int8')
Y = []

# Populate training array with flattened imags from subfolders of train_faces and names
c = 0
for x, folder in enumerate(folders):
    train_faces = glob.glob(folder + '/*')
    for i, face in enumerate(train_faces):
        X[c,:] = prepare_image(face)
        Y.append(ID_from_filename(face))
        c = c + 1

# perform principal component analysis on the images
pca = RandomizedPCA(n_components=NUM_EIGENFACES, whiten=True).fit(X)
X_pca = pca.transform(X)

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

i=0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        #minSize=(70, 90),
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        x, y, w, h = resize(x, y, w, h)
        draw_rectangle(x, y, w, h)
        #cv2.imwrite('last_frame.png', frame)
        face = frame[y:y+h, x:x+w]
        resized = cv2.resize(face, (92, 112))
        #cv2.imwrite('last_roi.png', resized)
        grayscale = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
        #cv2.imwrite('test_faces/last_grayscale' + str(time.time()) + '.png', grayscale)
        cv2.imwrite('test_faces/last_grayscale.png', grayscale)
        find_person(Y)
        cv2.imwrite('copy_faces/grayscale-' + str(i) + '.png', grayscale)
        i = i+1

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
