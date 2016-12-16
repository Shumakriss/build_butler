from build_butler import state, waitState, confirmAckState
from build_butler.textToSpeech import tts
import time

class ConfirmAckState(state.State):

	def action(self):
		tts.say("Yes or no")
		time.sleep(2)
		tts.say("Good")
		time.sleep(1)
		tts.say("Fix the build or you will be vaporized")
		time.sleep(1)
		ack = True
		if(ack):
			self.next = waitState.WaitState()
		else:
			time.sleep(1)
			self.next = confirmAckState.ConfirmAckState()