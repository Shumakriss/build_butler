from build_butler import state, confirmIdentityState
from build_butler.textToSpeech import tts
import time

class RequestIdentityState(state.State):

	def action(self):
		tts.say("Are you " + self.data)
		self.next = confirmIdentityState.ConfirmIdentityState()