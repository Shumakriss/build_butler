class State:

	def __init__(self, data=None):
		self.data = data

	def start(self):
		self.action()
		if(self.next != None):
			self.next.start()
		else:
			return