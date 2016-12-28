from subprocess import call

def say(quote):
	print(quote)
	# Robot
	#call(["say", "-v", "Zarvox", quote])

	# Australian
	call(["say", "-v", "Karen", quote])
	
	# British
	#call(["say", "-v", "Daniel", quote])