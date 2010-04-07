'''
Created on Apr 8, 2010

@author: victorhg
'''
import urllib

DEFAULT_UNITARY_CURRENCY = "USD"
CURRENCIES = ["EUR", "GBP", "JPY", "BRL", "AUD", "CAD"]

def exchange_rate():
    result = "Exchange Rates provided by http://www.travelground.com/ \n\n"
    for currency in CURRENCIES:
        url = urllib.urlopen("http://www.exchangerate-api.com/%s/%s/%f"%(DEFAULT_UNITARY_CURRENCY,currency,1))
        exchange_rate = url.read()
        result = result + ("%s/%s - %s \n"%(DEFAULT_UNITARY_CURRENCY, currency, exchange_rate ))
    return result
    
    
    