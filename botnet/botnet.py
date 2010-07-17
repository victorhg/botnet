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
'''
Created on Apr 1, 2010

@author: victorhg
'''
import finance
from eliza import eliza
from pyconireland import PyconIreland
from gtalkbot import GTalkBot, botcommand
from yahoo import YahooGeoPlanetSearch, YahooWeatherSearch, InvalidSearchError

class BotnetJabberClient(GTalkBot):

    BOT_USER = 'pycon.bot@gmail.com'
    BOT_PASS = 'pycon123'
    
    def __init__(self):
        self.eliza = eliza()
        super(BotnetJabberClient,self).__init__(self.BOT_USER, self.BOT_PASS)
        self.geoPlanet = YahooGeoPlanetSearch()
        self.yahooWeather = YahooWeatherSearch()
        self.pyconIreland = PyconIreland()

    @botcommand
    def weather(self, mess, args):
        """Returns the forecasts for any place. Usage: weather [City Name]"""
        try:
            woeid = self.geoPlanet.place_search(args).woeid()
            result = self.format_weather_result(self.yahooWeather.forecast(woeid))
            return result.encode("utf-8")
        except InvalidSearchError:
            return "Invalid Search, plz try again"
        except Exception:
            return "Unknow error... sorry about that"

    @botcommand
    def currency(self, mess, args):
        """Returns updated information about Dollar currency"""
        return finance.exchange_rate()
        
        
    @botcommand
    def talk(self, mess, args):
        "Retrieves information about talks at Pycon Ireland 2010. Search for the authors name or the talks name"
        return self.pyconIreland.find_talk(args)
    
    @botcommand
    def speaker(self, mess, args):
        """Returns Information about any of the speakers at Pycon Ireland 2010"""
        return self.pyconIreland.find_speaker(args)
        
    def unknown_command( self, mess, cmd, args):
        """Putting some Mojo here to make the bot answer as Eliza when wrong command is given""" 
        return self.eliza.respond(mess.getBody())
        
    
    def format_weather_result(self, result):
        model_header = "{0}\n {1} C - {2} \n Forecasts\n"
        model_forecasts = "{0} -> {1} with max {2} C | min {3} C\n"  
        
        forecast_result = model_header.format(result['title'], result['current_temp'], result['current_condition'])
        for forecast in result['forecasts']:
            forecast_result += model_forecasts.format(forecast['date'], forecast['condition'], forecast['high'], forecast['low'])
        
        return forecast_result
    
