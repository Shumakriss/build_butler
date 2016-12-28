from build_butler import state, requestAckState
from build_butler.textToSpeech import tts
import time

class InformState(state.State):

	def action(self):
		tts.say("I know, I was just being polite")
		time.sleep(1)
		tts.say("You have broken the build")
		time.sleep(1)
		self.next = requestAckState.RequestAckState()