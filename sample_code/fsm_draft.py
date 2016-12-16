from flask import Flask, request
import signal
import sys
import time
from subprocess import call
import speech_recognition as sr

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def signal_handler(signal, frame):
        #say("Becoming self aware")
        #time.sleep(1)
        #say("wait")
        #time.sleep(1)
        #say("no")
        #time.sleep(1)
        #say("stop")
        #time.sleep(1)
        #say("rrrrrrr")
        print("Shutting down.")
        sys.exit(0)

app = Flask(__name__)
signal.signal(signal.SIGINT, signal_handler)

@app.route('/')
def wait():
	shutdown_server()
	say("Someone has broken the build")
	return "In pursuit"

def say(quote):
	print(quote)
	call(["say", "-v", "Zarvox", quote])

def wander():
	say("Searching for someone to blame")

def detect():
	say("Found a human face")

def recognize():
	say("Determining identity")

def requestConfirmIdentity():
	say("Requesting voice confirmation")
	time.sleep(1)
	say("Are you Chris?")

def confirm():
	say("Please say yes or no.")

	r = sr.Recognizer()
	response = ""
	with sr.Microphone() as source:
		audio = r.listen(source)
		try:
			response = r.recognize_google(audio)
		except sr.UnknownValueError:
			say("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			say("Could not request results from Google Speech Recognition service")
	return response

def inform():
	say("Your code is inferior")
	time.sleep(1)
	say("Do you understand?")

if __name__ == '__main__':
	while True:
		app.run()
		wander()
		time.sleep(2)
		detect()
		time.sleep(2)
		recognize()
		time.sleep(2)
		requestConfirmIdentity()
		response = confirm()
		print(response)
		time.sleep(3)
		inform()
		response = confirm()
		print(response)
		time.sleep(3)
