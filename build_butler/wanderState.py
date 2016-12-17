from build_butler import state, detectState
from build_butler.textToSpeech import tts
import time

class WanderState(state.State):

	def action(self):
		tts.say("Initiated pathfinding")
		time.sleep(1)
		self.next = detectState.DetectState(data=self.data)