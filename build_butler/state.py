class State:

	def action(self):
		print("undefined actioned")
		self.next = None

	def start(self):
		self.action()
		if(self.next != None):
			self.next.start()
		else:
			return

def action(self):
	print("undefined actioned")
	self.next = None

def start(self):
	self.action()
	if(self.next != None):
		self.next.start()
	else:
		return