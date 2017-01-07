from build_butler import state, recognizeState, wanderState, constants
from build_butler.textToSpeech import tts
import Pyro4
import cv2
import sys

class PyroDetectState(state.State):

	def action(self):
		tts.say("Scanning for humans")

		cascPath = constants.CLASSIFIER_FILE
		faceCascade = cv2.CascadeClassifier(cascPath)
		video = Pyro4.Proxy("PYRONAME:video.frame")
		Pyro4.config.SERIALIZERS_ACCEPTED = set(['pickle','json', 'marshal', 'serpent'])
		Pyro4.config.SERIALIZER = 'pickle'
		
		frame = video.get_frame()
		
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=constants.SCALE_FACTOR,
			minNeighbors=constants.MIN_NEIGHBORS,
			minSize=(constants.MIN_WIDTH, constants.MIN_HEIGHT),
			flags=cv2.CASCADE_SCALE_IMAGE
		)

		video._pyroRelease()

		if(type(faces) != tuple and faces.size > 0):
			tts.say("Face detected")
			self.next = recognizeState.RecognizeState(data=[frame, faces, self.data])
		else:
			self.next = wanderState.WanderState()