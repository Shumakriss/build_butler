import Pyro4
import cv2
import speech_recognition as sr

Pyro4.config.SERIALIZERS_ACCEPTED = set(['pickle','json', 'marshal', 'serpent'])
Pyro4.config.SERIALIZER = 'pickle'

video_capture = cv2.VideoCapture(0)
for i in range(5):
	video_capture.read()

r = sr.Recognizer()

@Pyro4.expose
class Video(object):
	def get_frame(self):
		ret, frame = video_capture.read()
		return frame

@Pyro4.expose
class Audio(object):
	def get_text(self):
		text = ""
		with sr.Microphone() as source:
			audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
			text = ""
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
			text = ""
		if(text == None or type(text) == type(None)):
			text = ""

		return text

daemon = Pyro4.Daemon("localhost")
ns = Pyro4.locateNS(broadcast=True)
video_uri = daemon.register(Video)
audio_uri = daemon.register(Audio)
ns.register("video.frame", video_uri)
ns.register("audio.text", audio_uri)
print("Finished registering Pyro objects")
daemon.requestLoop()