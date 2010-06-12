import xmpp

jid = xmpp.protocol.JID('pycon.bot@gmail.com')
pwd = 'pycon123'
server = "talk.google.com" 
port = 5222
	
conn = xmpp.Client(jid.getDomain(),debug=[])		

conn.connect([server, port])

conn.auth(jid.getNode(), pwd)

conn.sendInitPresence()


#new part
def callback_message(conn, mess):
	message_body = mess.getBody()
	if not message_body:
		return
	reply_message = "You typed: "+message_body
	conn.send(xmpp.protocol.Message(mess.getFrom(), reply_message))


conn.RegisterHandler( 'message', callback_message)
#main loop
def idle_proc( ):
	"""This function will be called in the main loop."""
	pass

while True:
	try:
		conn.Process(1)
		idle_proc()
	except KeyboardInterrupt:
		print 'bot stopped by user request. shutting down.'
		conn.disconnect()
		break
	except xmpp.protocol.InternalServerError:
		print "Server error at Google, trying again"

