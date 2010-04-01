'''
Created on Apr 1, 2010

@author: victorhg
'''
from jabberbot import JabberBot, botcmd
from yahoo import YahooGeoPlanetSearch, YahooWeatherSearch

BOT_USER = 'bot.internet@jabber-br.org'
BOT_PASS = '123456'
class BotnetJabberClient(JabberBot):

    def __init__(self):
        self.geoPlanet = YahooGeoPlanetSearch()
        self.yahooWeather = YahooWeatherSearch()
        JabberBot.__init__(self, BOT_USER, BOT_PASS)

    @botcmd
    def weather(self, mess, args):
        woeid = self.geoPlanet.place_search(args).woeid()
        return self.yahooWeather.forecast(woeid)
        
    
    @botcmd
    def hello(self, mess, args):
        """Greetings"""
        return "Hi! how can I help you? Type 'help' to see available commands"
    
    
    def run(self):
        self.serve_forever()