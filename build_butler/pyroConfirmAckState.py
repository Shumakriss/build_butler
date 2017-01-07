from build_butler import state, waitState, pyroConfirmAckState
from build_butler.textToSpeech import tts
import Pyro4
import time
import speech_recognition as sr

class PyroConfirmAckState(state.State):

	def action(self):
		Pyro4.config.SERIALIZERS_ACCEPTED = set(['pickle','json', 'marshal', 'serpent'])
		Pyro4.config.SERIALIZER = 'pickle'

		audio = Pyro4.Proxy("PYRONAME:audio.text")
		test = ""
		if(type(audio) != type(None) and audio != None):
			try:
				text = audio.get_text() 
				print(text)
			except UnboundLocalError as ule:
				print("No text received")
			except NameError as ne:
				print("No text received")
		else:
			print("No text received")
				
		if(text == "yes"):
			tts.say("Good")
			time.sleep(1)
			tts.say("Fix it or be destroyed")
			time.sleep(1)
			self.next = waitState.WaitState()
		else:
			time.sleep(1)
			self.next = pyroConfirmAckState.PyroConfirmAckState()