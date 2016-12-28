from build_butler import constants
import glob
import numpy as np
import math
import cv2

def ID_from_filename(filename):
    if(filename == None):
        raise "Must specify filename"
    part = filename.split('/')
    return part[3]
 
def prepare_image(filename):
    img_color = cv2.imread(filename)
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    return img_gray.flat

def resize(x, y, w, h):
    if( w/h > constants.RATIO):
        extra_width = (constants.WIDTH * h / constants.HEIGHT) - w
        w = w + extra_width
        x = x - (extra_width / 2)
    else:
        extra_height = (constants.HEIGHT * w / constants.WIDTH) - h
        h = h + extra_height
        y = y - (extra_height / 2)
    return int(x), int(y), int(w), int(h)

def draw_rectangle(frame, x, y, w, h):
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return

def find_person(Y, pca, X_pca):
    test_faces = glob.glob(constants.TEST_FACES)
    print('test_faces=', test_faces)

    X = np.zeros([len(test_faces), constants.IMG_RES], dtype='int8')

    for i, face in enumerate(test_faces):
        X[i,:] = prepare_image(face)

    for j, ref_pca in enumerate(pca.transform(X)):
        distances = []

        for i, test_pca in enumerate(X_pca):
            dist = math.sqrt(sum([diff**2 for diff in (ref_pca - test_pca)]))
            distances.append((dist, Y[i]))

        eigenDistance = min(distances)[0]
        found_ID = min(distances)[1]

        if(eigenDistance < constants.THRESHOLD):
            return str(found_ID)
        else:
            return None