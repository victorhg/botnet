'''
Created on Mar 31, 2010

@author: victorhg
'''
import unittest
from yahoo  import *

class Test(unittest.TestCase):

    
    def setUp(self):
        self.yahoo = YahooWeatherSearch()

    def test_return_woeid(self):
        woeid_dublin = 560743 #from yahoo
        self.yahoo.place_search("Dublin")
        self.assertEqual(1, self.yahoo.num_places())
        self.assertEqual(woeid_dublin, self.yahoo.woeid()) 

    def test_return_woeid_saoPaulo(self):
        woeid_dublin = 455827 #from yahoo
        self.yahoo.place_search("Sao Paulo")
        self.assertEqual(1, self.yahoo.num_places())
        self.assertEqual(woeid_dublin, self.yahoo.woeid())
        
    def test_number_places_without_search(self):
        self.assertRaises(SearchNotPlacedError, self.yahoo.num_places)
        
    
    def test_woeid_without_search(self):
        self.assertRaises(SearchNotPlacedError, self.yahoo.woeid)
        
        
    def test_invalid_search(self):
        self.yahoo.place_search("John Joe Town")
        self.assertEqual(0, self.yahoo.num_places())
        self.assertRaises(InvalidSearchError, self.yahoo.woeid)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_return_woeid']
    unittest.main()