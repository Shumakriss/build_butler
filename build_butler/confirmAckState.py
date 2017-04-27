from build_butler import state, waitState, requestAckState
from build_butler.textToSpeech import tts
import time
import speech_recognition as sr

class ConfirmAckState(state.State):

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
			tts.say("Good")
			time.sleep(1)
			tts.say("Fix it or be destroyed")
			time.sleep(1)
			self.next = waitState.WaitState()
		else:
			time.sleep(1)
			self.next = requestAckState.RequestAckState()