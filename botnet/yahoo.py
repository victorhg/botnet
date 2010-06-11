'''
Created on Mar 31, 2010

@author: victorhg
'''
from xml.dom import minidom
import simplejson as json
import urllib

class SearchNotPlacedError(Exception):
    def __init__(self):
            self.value = "Search no placed"
        
class InvalidSearchError(Exception):
    def __init__(self):
        self.value = "Wrong search"


class YahooGeoPlanetSearch():
    YAHOO_APP_ID="4h7YbM3V34H8fWjCUpjrrpnJJ0Lb3K8E7BwVWvjKIePelC9TVM2g4RYA3x0XTc2_sm2DDNFvtz9"
    def __init__(self):
        self.YAHOO_SEARCH_URL = "http://where.yahooapis.com/v1/places.q('{0}')?format=json&appid={1}"
        self.last_search = None
        

    def place_search(self, city):
        """Set up the searcher structure with information to retrieve the Object from Yahoo! Weather engine"""
        url = self.YAHOO_SEARCH_URL.format(city, YahooGeoPlanetSearch.YAHOO_APP_ID)
        result_json = urllib.urlopen(url).read()
        
        self.last_search = json.loads(result_json)
        if self.last_search.has_key('error'):
            raise InvalidSearchError()
        return self
        
   
    def validateSearchPlaced(self):
        if(self.last_search == None):
            raise SearchNotPlacedError()

    def num_places(self):
        self.validateSearchPlaced()
        return self.last_search['places']['count']
    
    
    def woeid(self):
        self.validateSearchPlaced()
        places_attrs = self.last_search['places']
        
        if (places_attrs['count'] == 0):
            raise InvalidSearchError() 
        
        return places_attrs['place'][0]['woeid']
    
    
    
class YahooWeatherSearch():
    WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'
    WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?w={0}&u=c'

    def forecast(self, woeid):
        url = YahooWeatherSearch.WEATHER_URL.format(woeid)
        dom = minidom.parse(urllib.urlopen(url))
        forecasts = []
        for node in dom.getElementsByTagNameNS(YahooWeatherSearch.WEATHER_NS, 'forecast'):
            forecasts.append({
                'date': node.getAttribute('date'),
                'low': node.getAttribute('low'),
                'high': node.getAttribute('high'),
                'condition': node.getAttribute('text')
            })
        ycondition = dom.getElementsByTagNameNS(YahooWeatherSearch.WEATHER_NS, 'condition')[0]
        return {
            'current_condition': ycondition.getAttribute('text'),
            'current_temp': ycondition.getAttribute('temp'),
            'forecasts': forecasts,
            'title': dom.getElementsByTagName('title')[0].firstChild.data
        }
        