from time import time
import cv2

class Camera(object):

	def __init__(self, video_capture):
		self.video_capture = video_capture
		# Throw away first frames while webcam adjusts
		for i in range(5):
			video_capture.read()

	def get_frame(self):
		ret, frame = self.video_capture.read()
		cv2.imwrite("frame.jpg", frame)
		image = open('frame.jpg', 'rb').read()
		return image