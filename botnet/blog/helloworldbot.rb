import xmpp

jid = xmpp.protocol.JID('pycon.bot@gmail.com')
pwd = 'pycon123'
server = "talk.google.com" 
port = 5222
	
conn = xmpp.Client(jid.getDomain(),debug=[])		

conn.connect([server, port])

conn.auth(jid.getNode(), pwd)

conn.send(xmpp.protocol.Message("victorhg@gmail.com", "hello world"))

conn.disconnect()
