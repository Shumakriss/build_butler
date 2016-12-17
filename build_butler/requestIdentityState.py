from build_butler import state, confirmIdentityState
from build_butler.textToSpeech import tts
import time

class RequestIdentityState(state.State):

	def action(self):
		person, data = self.data
		tts.say("Are you " + person)
		self.next = confirmIdentityState.ConfirmIdentityState(data=self.data)