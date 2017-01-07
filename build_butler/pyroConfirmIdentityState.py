from build_butler import state, informState, wanderState
from build_butler.textToSpeech import tts
import Pyro4
import time
import speech_recognition as sr

class PyroConfirmIdentityState(state.State):

	def action(self):
		Pyro4.config.SERIALIZERS_ACCEPTED = set(['pickle','json', 'marshal', 'serpent'])
		Pyro4.config.SERIALIZER = 'pickle'

		audio = Pyro4.Proxy("PYRONAME:audio.text")

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
			self.next = informState.InformState()
		else:
			self.next = wanderState.WanderState()