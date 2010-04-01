'''
Created on Apr 1, 2010

@author: victorhg
'''
import unittest
from botnet import BotnetJabberClient


class Test(unittest.TestCase):


    def test_weather_command(self):
        bot = BotnetJabberClient()
        bot.weather("", ["Dublin"])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_weather_command']
    unittest.main()