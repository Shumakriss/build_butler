from subprocess import call

def say(quote):
	print(quote)
	call(["say", "-v", "Zarvox", quote])