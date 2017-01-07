import Pyro4
import speech_recognition as sr
import picamera
import numpy as np

Pyro4.config.SERIALIZERS_ACCEPTED = set(['pickle','json', 'marshal', 'serpent'])
Pyro4.config.SERIALIZER = 'pickle'

r = sr.Recognizer()

@Pyro4.expose
class Video(object):
    def get_frame(self):
        output = None
        with picamera.PiCamera() as camera:
                camera.resolution = (320, 240)
                camera.framerate = 24
                output = np.empty((240, 320, 3), dtype=np.uint8)
                camera.capture(output, 'rgb')
        return output

@Pyro4.expose
class Audio(object):
	def get_text(self):
		text = ""
		with sr.Microphone(device_index=2,chunk_size=512,sample_rate=44100) as source:
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

daemon = Pyro4.Daemon("192.168.1.12")
ns = Pyro4.locateNS(broadcast=True)
audio_uri = daemon.register(Audio)
video_uri = daemon.register(Video)
ns.register("audio.text", audio_uri)
ns.register("video.frame", video_uri)
print("Finished registering Pyro objects")
daemon.requestLoop()