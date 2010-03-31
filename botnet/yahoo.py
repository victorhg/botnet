'''
Created on Mar 31, 2010

@author: victorhg
'''
import simplejson as json
import urllib

class InvalidSearchError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class YahooWeatherSearch():
    YAHOO_APP_ID="4h7YbM3V34H8fWjCUpjrrpnJJ0Lb3K8E7BwVWvjKIePelC9TVM2g4RYA3x0XTc2_sm2DDNFvtz9"
    def __init__(self):
        self.YAHOO_SEARCH_URL = "http://where.yahooapis.com/v1/places.q('{0}')?format=json&appid={1}"
        pass

    def place_search(self, city):
        """Set up the searcher structure with information to retrieve the Object from Yahoo! Weather engine"""
        url = self.YAHOO_SEARCH_URL.format(city, YahooWeatherSearch.YAHOO_APP_ID)
        result_json = urllib.urlopen(url).read()
        self.last_search = json.loads(result_json)
        
    def num_places(self):
        return self.last_search['places']['count']
    
    def woeid(self):
        places_attrs = self.last_search['places']
        
        if (places_attrs['count'] == 0):
            raise InvalidSearchError("Wrong search") 
        
        return places_attrs['place'][0]['woeid']
        