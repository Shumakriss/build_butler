from build_butler import state, informState, wanderState
from build_butler.textToSpeech import tts
import time
import speech_recognition as sr

class ConfirmIdentityState(state.State):

	def action(self):
		for i in range(3):
			r = sr.Recognizer()
			with sr.Microphone() as source:
		  		audio = r.listen(source)

			try:
			  text = r.recognize_google(audio)
			except sr.UnknownValueError:
			  print("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
			  print("Could not request results from Google Speech Recognition service; {0}".format(e))
			if(text == "yes"):
				break

		if(text == "yes"):
			self.next = informState.InformState()
		else:
			self.next = wanderState.WanderState()