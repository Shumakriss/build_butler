from time import time
import cv2

class Camera(object):

	def get_frame(self):
		video_capture = cv2.VideoCapture(0)
		# Throw away first frames while webcam adjusts
		for i in range(5):
			video_capture.read()
		ret, frame = video_capture.read()
		video_capture.release()
		cv2.imwrite("frame.jpg", frame)
		image = open('frame.jpg', 'rb').read()
		return image