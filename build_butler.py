import poplib
import json
import sys
from email import parser
poplib._MAXLINE=20480

with open('build_butler.json') as config_file:
	options = json.load(config_file)

def get_messages():
	print 'building connection object'
	pop_conn = poplib.POP3_SSL(options['server'])
	pop_conn.user(options['email'])
	pop_conn.pass_(options['password'])
	print 'built connection object'

	print 'pop_conn.list()', pop_conn.list()
	print 'pop_conn.list()[1]', pop_conn.list()[1]
	print 'len(pop_conn.list()[1] + 1)', len(pop_conn.list()[1] + 1)
	sys.exit(0)

	print 'retrieving messages'
	#Get messages from server:
	messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
	print 'retrieved messages'
	print 'formatting messages'
	# Concat message pieces:
	messages = ["\n".join(mssg[1]) for mssg in messages]
	print 'formatted messages'
	print 'parsing messages'
	#Parse message intom an email object:
	messages = [parser.Parser().parsestr(mssg) for mssg in messages]
	print 'parsed messages count'
	print len(messages)
	print 'closing connection'
	pop_conn.quit()
	print 'connection closed, exiting...'
	return messages

def get_build_messages(messages):
	print "get_build_messages is not finished"
	print messages
	return messages

def get_uscis_messages(messages):
	print "get_uscis_messages is not finished"
	print messages
	return messages

def get_latest_message(messages):
	print "get_latest_message is not finished"
	print messages
	return messages[0]

def get_status(message):
	print "get_status is not finished"
	print message
	return message.status

def disable_leds():
	print "disable leds is not finished"

def enable_leds(color):
	print "enable leds is not finished"
	print color

def update_leds(status):
	print "update_leds is not finished"
	print status
	disable_leds
	if(status == 'SUCCESS'):
		enable_leds('green')

def play_freq_for(freq, duration):
	print "play_freq_for is not finished"
	print freq, duration

def make_status_tone(status):
	print "make_status_tone is not finished"
	print status
	if(status == 'SUCCESS'):
		play_freq_for(126, 3000)

class Message():

	def __init__(self, content):
		print "Message constructor is not finished"
		self.status = content

	def status():
		self.status

i=0
##### Do stuff with messages
while(options['limit'] and i < options['num_attempts']):
	i = i+1
	# Fetch messages
	messages = get_messages()
	# Filter for automated myuscis messages
	build_messages = get_build_messages(messages)
	# Filter by some specific project/build pipeline - hardcoded/configurable
	uscis_messages = get_uscis_messages(build_messages)
	# Find latest status update
	latest_message = get_latest_message(uscis_messages)
	# Parse the email for status
	status = get_status(latest_message)
	# Update the LEDs by status
	update_leds(status)
	## Disable previous LEDs by color
	## Enable new LEDs by color
	# Play a tone by status
	make_status_tone(status)
