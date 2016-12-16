from build_butler import state, wanderState
from build_butler.textToSpeech import tts
import time

class WaitState(state.State):

	def action(self):
		tts.say("Watching for build failures")
		time.sleep(1)
		tts.say("Received build failure alert")
		time.sleep(1)
		self.next = wanderState.WanderState()