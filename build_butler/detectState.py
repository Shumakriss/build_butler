from build_butler import state, recognizeState, wanderState
from build_butler.textToSpeech import tts
import cv2
import sys

class DetectState(state.State):

	RATIO = 92/112
	CLASSIFIER_FILE = "sample_code/visual_recognition/find_my_face_live/haarcascade_frontalface_default.xml"

	def action(self):
		tts.say("Scanning for humans")

		cascPath = self.CLASSIFIER_FILE
		faceCascade = cv2.CascadeClassifier(cascPath)
		video_capture = cv2.VideoCapture(0)

		# Throw away blank first frame
		video_capture.read()
		ret, frame = video_capture.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30),
			flags=cv2.CASCADE_SCALE_IMAGE
		)

		video_capture.release()

		if(faces.size > 0):
			self.next = recognizeState.RecognizeState(data=[frame, faces])
		else:
			self.next = wanderState.WanderState()