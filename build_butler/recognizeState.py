from build_butler import state, requestIdentityState, wanderState
from build_butler.textToSpeech import tts
import time

class RecognizeState(state.State):

	def action(self):
		tts.say("Identifying human")
		time.sleep(1)
		recognized = True
		if(recognized):
			self.next = requestIdentityState.RequestIdentityState(data="Chris")
		else:
			self.next = wanderState.WanderState()