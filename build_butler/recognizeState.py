from build_butler import state, requestIdentityState, wanderState, constants, vision
from build_butler.textToSpeech import tts
from sklearn.decomposition import RandomizedPCA
import numpy as np
import time
import cv2
import glob

class RecognizeState(state.State):

	def __init__(self, data):
		self.data = data
		X = np.zeros([constants.NUM_TRAINIMAGES, constants.IMG_RES], dtype='int8')
		self.Y = []

		folders = glob.glob(constants.TRAIN_FACES)

		c = 0
		for x, folder in enumerate(folders):
			train_faces = glob.glob(folder + '/*')[0:constants.NUM_EIGENFACES]
			for i, face in enumerate(train_faces):
				X[c,:] = vision.prepare_image(face)
				self.Y.append(vision.ID_from_filename(face))
				c = c + 1

		self.pca = RandomizedPCA(n_components=constants.NUM_EIGENFACES, whiten=True).fit(X)
		self.X_pca = self.pca.transform(X)

	def action(self):
		tts.say("Identifying human")
		recognized = False

		frame, faces, post_body = self.data

		for (x, y, w, h) in faces:
			# This looks like what I would need if I wasn't writing the file
			#x, y, w, h = vision.resize(x, y, w, h)
			#face = frame[y:y+h, x:x+w]
			#resized = cv2.resize(face, (constants.WIDTH, constants.HEIGHT))
			#grayscale = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
			person = vision.find_person(self.Y, self.pca, self.X_pca)
			print("Recognized person as '", person, "'")
			if(person == post_body):
				recognized = True

		if(recognized):
			self.next = requestIdentityState.RequestIdentityState(data=[person, self.data])
		else:
			self.next = wanderState.WanderState()