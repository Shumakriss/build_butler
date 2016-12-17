from build_butler import state, requestIdentityState, wanderState
from build_butler.textToSpeech import tts
from sklearn.decomposition import RandomizedPCA
import numpy as np
import time
import cv2
import glob
import math

class RecognizeState(state.State):

	IMG_RES = 92 * 112 # img resolution
	RATIO = 92/112
	NUM_EIGENFACES = 10 # images per train person
	NUM_TRAINIMAGES = 120 # total images in training set

	#function to get ID from filename
	def ID_from_filename(self, filename):
	    if(filename == None):
	        raise "Must specify filename"
	    part = filename.split('/')
	    return part[3].replace("s", "")
	 
	#function to convert image to right format
	def prepare_image(self, filename):
	    img_color = cv2.imread(filename)
	    img_gray = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
	    img_gray = cv2.equalizeHist(img_gray)
	    return img_gray.flat

	def resize(self, x, y, w, h):
	    # If it's wider
	    if( w/h > self.RATIO):
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

	def draw_rectangle(self, x, y, w, h):
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		return

	def find_person(self, Y):
		# load test faces (usually one), located in folder test_faces
		test_faces = glob.glob('build_butler/recognition/test_faces/*')

		# Create an array with flattened images X
		X = np.zeros([len(test_faces), self.IMG_RES], dtype='int8')

		# Populate test array with flattened imags from subfolders of train_faces 
		# This looks wrong to me
		for i, face in enumerate(test_faces):
			X[i,:] = self.prepare_image(face)

		# run through test images (usually one)
		for j, ref_pca in enumerate(self.pca.transform(X)):
			distances = []
			# Calculate euclidian distance from test image to each of the known images and save distances
			for i, test_pca in enumerate(self.X_pca):
				dist = math.sqrt(sum([diff**2 for diff in (ref_pca - test_pca)]))
				distances.append((dist, Y[i]))

			eigenDistance = min(distances)[0]
			found_ID = min(distances)[1]

			if(eigenDistance < 1.5):
				return str(found_ID)
			else:
				return None

	def action(self):
		tts.say("Identifying human")
		recognized = False

		frame, faces, post_body = self.data

		# Create an array with flattened images X
		# and an array with ID of the people on each image y
		X = np.zeros([self.NUM_TRAINIMAGES, self.IMG_RES], dtype='int8')
		Y = []

		#loading training set from folder train_faces
		folders = glob.glob('build_butler/recognition/train_faces/*')

		# Populate training array with flattened imags from subfolders of train_faces and names
		c = 0
		for x, folder in enumerate(folders):
			train_faces = glob.glob(folder + '/*')
			for i, face in enumerate(train_faces):
				X[c,:] = self.prepare_image(face)
				Y.append(self.ID_from_filename(face))
				c = c + 1

		# perform principal component analysis on the images
		self.pca = RandomizedPCA(n_components=self.NUM_EIGENFACES, whiten=True).fit(X)
		self.X_pca = self.pca.transform(X)

		for (x, y, w, h) in faces:
			x, y, w, h = self.resize(x, y, w, h)
			face = frame[y:y+h, x:x+w]
			resized = cv2.resize(face, (92, 112))
			grayscale = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
			person = self.find_person(Y)
			recognized = person == post_body

		if(recognized):
			self.next = requestIdentityState.RequestIdentityState(data=[person, self.data])
		else:
			self.next = wanderState.WanderState()