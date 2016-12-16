from build_butler import state, recognizeState, wanderState
from build_butler.textToSpeech import tts
import time

class DetectState(state.State):

	def action(self):
		tts.say("Scanning for humans")
		time.sleep(1)
		detected = True
		if(detected):
			self.next = recognizeState.RecognizeState()
		else:
			self.next = wanderState.WanderState()