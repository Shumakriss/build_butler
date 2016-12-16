class State:

	def start(self):
		self.action()
		if(self.next != None):
			self.next.start()
		else:
			return