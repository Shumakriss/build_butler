from build_butler import state, recognizeState, wanderState, constants
from build_butler.textToSpeech import tts
import cv2
import sys

class DetectState(state.State):

	def action(self):
		tts.say("Scanning for humans")

		cascPath = constants.CLASSIFIER_FILE
		faceCascade = cv2.CascadeClassifier(cascPath)
		video_capture = cv2.VideoCapture(0)

		# Throw away the first few frames, they can be blank
		for i in range(5):
			video_capture.read()
		
		ret, frame = video_capture.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=constants.SCALE_FACTOR,
			minNeighbors=constants.MIN_NEIGHBORS,
			minSize=(constants.MIN_WIDTH, constants.MIN_HEIGHT),
			flags=cv2.CASCADE_SCALE_IMAGE
		)

		video_capture.release()

		if(type(faces) != tuple and faces.size > 0):
			tts.say("Face detected")
			self.next = recognizeState.RecognizeState(data=[frame, faces, self.data])
		else:
			self.next = wanderState.WanderState()