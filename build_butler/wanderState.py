from build_butler import state, detectState
from build_butler.textToSpeech import tts
import time

class WanderState(state.State):

	def action(self):
		print(self.data)
		tts.say("Initiated pathfinding")
		time.sleep(1)
		self.next = detectState.DetectState()