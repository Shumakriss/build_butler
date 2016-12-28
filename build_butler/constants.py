import os, os.path

CLASSIFIER_FILE="build_butler/detection/haarcascade_frontalface_default.xml"
SCALE_FACTOR=1.1
MIN_NEIGHBORS=5
MIN_WIDTH=140
MIN_HEIGHT=180
HEIGHT=112
WIDTH=92
IMG_RES=WIDTH * HEIGHT
RATIO=WIDTH/HEIGHT
TEST_DIR='build_butler/recognition/test_faces/'
TRAIN_DIR='build_butler/recognition/train_faces/'
TEST_FACES='build_butler/recognition/test_faces/*'
TRAIN_FACES='build_butler/recognition/train_faces/*'
THRESHOLD=1.5
ROOT="build_butler/detection/"
CASC_PATH=ROOT + 'haarcascade_frontalface_default.xml'

teammates=[name for name in os.listdir(TRAIN_DIR) if os.path.isdir(TRAIN_DIR + name)]
NUM_TEAMMATES=len(teammates)

counts = []
for name in teammates:
	path=TRAIN_DIR+name+"/"
	counts.append(len(os.listdir(path)))

MIN_IMAGES_PER_TEAMMATE=min(counts)

NUM_EIGENFACES=MIN_IMAGES_PER_TEAMMATE
NUM_TRAINIMAGES=MIN_IMAGES_PER_TEAMMATE * NUM_TEAMMATES