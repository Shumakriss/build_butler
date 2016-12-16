from build_butler import state, wanderState
from build_butler.textToSpeech import tts
from flask import Flask, request
import logging
import time

class WaitState(state.State):

	def shutdown_server(self):
		func = request.environ.get('werkzeug.server.shutdown')
		if func is None:
			raise RuntimeError('Not running with the Werkzeug Server')
		func()

	def wait(self):
		self.shutdown_server()
		tts.say("Received build failure alert")
		self.post_body = "Post body"
		return "Alert received"

	def action(self):
		tts.say("Watching for build failures")
		log = logging.getLogger('werkzeug')
		log.setLevel(logging.ERROR)
		app = Flask(__name__)
		app.add_url_rule("/", view_func=self.wait, methods=['POST',])
		app.run()
		self.next = wanderState.WanderState(data=self.post_body)