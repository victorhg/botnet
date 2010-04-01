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
        """Returns the forecasts for any place. Usage: weather [City Name]"""
        woeid = self.geoPlanet.place_search(args).woeid()
        result = self.format_weather_result(self.yahooWeather.forecast(woeid))
        return result
        
    def format_weather_result(self, result):
        model_header = "{0}\n {1} C - {2} \n Forecasts\n"
        model_forecasts = "{0} -> {1} with max {2} C | min {3} C\n"  
        
        forecast_result = model_header.format(result['title'], result['current_temp'], result['current_condition'])
        for forecast in result['forecasts']:
            forecast_result += model_forecasts.format(forecast['date'], forecast['condition'], forecast['high'], forecast['low'])
        
        return forecast_result
    
    @botcmd
    def hello(self, mess, args):
        """Greetings"""
        return "Hi! how can I help you? Type 'help' to see available commands"
    
    
    def run(self):
        self.serve_forever()
