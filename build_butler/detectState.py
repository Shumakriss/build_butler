from build_butler import state, recognizeState, wanderState
from build_butler.textToSpeech import tts
import cv2
import sys

class DetectState(state.State):

	RATIO = 92/112
	CLASSIFIER_FILE = "build_butler/detection/haarcascade_frontalface_default.xml"

	def action(self):
		tts.say("Scanning for humans")

		cascPath = self.CLASSIFIER_FILE
		faceCascade = cv2.CascadeClassifier(cascPath)
		video_capture = cv2.VideoCapture(0)

		# Throw away the first few frames, they can be blank
		for i in range(5):
			video_capture.read()
		
		ret, frame = video_capture.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(70, 90),
			flags=cv2.CASCADE_SCALE_IMAGE
		)

		video_capture.release()

		if(type(faces) != tuple and faces.size > 0):
			self.next = recognizeState.RecognizeState(data=[frame, faces, self.data])
		else:
			self.next = wanderState.WanderState()