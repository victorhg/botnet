#       DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                Version 1, July 2010

#Copyright (C) 2010 VICTOR HUGO GERMANO, Earth
#Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.

import xmpp
import inspect


def botcommand(*args):
    func = args[0]
    setattr(func, '_gbot_command', func.__name__)
    return func


class GTalkBot(object):
    
    GTALK_SERVER = "talk.google.com"
    GTALK_SERVER_PORT = 5222
    
    def __init__(self, gtalk_id, password):
        self.jid = xmpp.protocol.JID(gtalk_id)
        self.password = password
        self._finalize = False
        self.conn = None
        self.register_commands()
        
    def register_commands(self):
        self.commands = {}
        for name, value in inspect.getmembers(self):
            if inspect.ismethod(value) and getattr(value, '_gbot_command', False):
                self.log('Registered command: %s' % name)
                self.commands[name] = value
    
    def presence_handler(self, conn, msg):
        """ Always accepts a subscribe request from any user. 
            Subscribe this method to change it"""
        msg_type = msg.getType()
        who = msg.getFrom()
        if msg_type == "subscribe":
            self.log('subscribe request sent by <%s>, accepting '%(who))
            conn.send(xmpp.Presence(to=who, typ='subscribed'))
            conn.send(xmpp.Presence(to=who, typ='subscribe'))
            
            
    def callback_message( self, conn, mess):
        """Messages sent to the bot will arrive here. Command handling + routing is done in this function.
            Reference: Thomas Perl <thp@thpinfo.com>"""
        text = mess.getBody()
        if not text:
            return

        self.log('Received message from %s: %s'%(mess.getFrom(), text))
        if ' ' in text:
            command, args = text.split(' ',1)
        else:
            command, args = text,''
    
        cmd = command.lower()
    
        if self.commands.has_key(cmd):
            reply = self.commands[cmd]( mess, args)
        else:
            reply = self.unknown_command( mess, cmd, args) 
            
        self.send( mess.getFrom(), reply, mess)

        
    def registerHandlers(self, conn):   
        conn.RegisterHandler('message', self.callback_message)
        conn.RegisterHandler('presence', self.presence_handler)
     
   
    def unknown_command(self, mess, cmd, args):
        return  "Unknown command: %s\n\n Type 'help' to see available commands" % cmd
        
    def send( self, user, text, in_reply_to = None):
        """Sends a simple message to the specified user."""
        mess = xmpp.Message( user, text)
        if in_reply_to:
            mess.setThread( in_reply_to.getThread())
            mess.setType( in_reply_to.getType())
        self.connect().send( mess)
        
    @botcommand
    def help(self, mess, args):
        usage = '\n'.join(sorted(['%s: %s' % (name, command.__doc__ or '(undocumented)') for (name, command) in self.commands.items() if name != 'help' and (not command.__doc__ or not command.__doc__.startswith('HIDDEN'))]))
        description = "Available commands:"
        return '%s\n\n%s' % ( description, usage, )
    
        
    def connect(self):
        if not self.conn:
            conn = xmpp.Client(self.jid.getDomain(), debug=[])  
            if not conn.connect([self.GTALK_SERVER, self.GTALK_SERVER_PORT]):
                self.log('unable to connect')
                return None
            if not conn.auth(self.jid.getNode(), self.password):
                self.log('wrong username/password')
                return None
            self.registerHandlers(conn)
            conn.sendInitPresence()
            self.conn = conn
        return self.conn
    
    
    def run_server(self):
        if self.connect():
            self.log('GTalkBot Connected...')
        else:
            self.log('leaving...')
            return
        
        while not self._finalize:
            try:
                self.conn.Process(1)
                self.idle()
            except KeyboardInterrupt:
                self.log('bot stopped by user request. shutting down.')
                break
            except xmpp.protocol.InternalServerError:
                print "Server error at Google, trying again"

    def idle(self):
        pass
    
    def log(self, str):
        print str 
