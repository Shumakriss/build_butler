from build_butler import state, pyroConfirmIdentityState
from build_butler.textToSpeech import tts
import time

class RequestIdentityState(state.State):

	def action(self):
		person, data = self.data
		tts.say("Are you " + person)
		self.next = pyroConfirmIdentityState.PyroConfirmIdentityState(data=self.data)