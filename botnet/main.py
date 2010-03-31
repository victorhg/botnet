
'''
Created on Mar 28, 2010

@author: victorhg
'''
from jabberbot import JabberBot, botcmd
import datetime

class SystemInfoJabberBot(JabberBot):
    
    
    @botcmd
    def hello(self, mess, args):
        """Greetings"""
        return "Hi! how can I help you? Type 'help' to see available commands"
    
 
 
username = 'bot.internet@jabber-br.org'
password = '123456'
bot = SystemInfoJabberBot(username,password)
bot.serve_forever()