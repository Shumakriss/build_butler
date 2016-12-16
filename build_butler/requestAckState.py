from build_butler import state, confirmAckState
from build_butler.textToSpeech import tts
import time

class RequestAckState(state.State):

	def action(self):
		tts.say("Do you understand")
		self.next = confirmAckState.ConfirmAckState()