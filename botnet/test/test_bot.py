'''
Created on Apr 1, 2010

@author: victorhg
'''
import unittest
from botnet import BotnetJabberClient


class Test(unittest.TestCase):


    def test_format_weather_result(self):
        result = {'current_condition': 'Light Rain Shower', 'current_temp': '5', 'title': 'Yahoo! Weather - Dublin, IE', 'forecasts': [{'date': '1 Apr 2010', 'high': '9', 'low': '3', 'condition': 'Light Rain Late'}, {'date': '2 Apr 2010', 'high': '9', 'low': '2', 'condition': 'Rain'}]}
        bot = BotnetJabberClient()
        expected = """Yahoo! Weather - Dublin, IE
                    5oC - Light Rain Shower
                    Forecasts
                    1 Apr 2010 -> Light Rain Late with max 9oC | min 3oC  
                    2 Apr 2010 -> Rain with max 9oC | min 2oC"""
        formated_result = bot.format_weather_result(result)
        print formated_result
        self.assertEquals(expected, formated_result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_weather_command']
    unittest.main()