from build_butler import state, informState, wanderState
from build_butler.textToSpeech import tts
import time

class ConfirmIdentityState(state.State):

	def action(self):
		tts.say("Yes or no")
		time.sleep(2)
		confirmed = True
		if(confirmed):
			self.next = informState.InformState()
		else:
			self.next = wanderState.WanderState()