'''
Created on Apr 8, 2010

@author: victorhg
'''
import urllib

API_KEY="MRVir-wHSZu-gzddf"
DEFAULT_UNITARY_CURRENCY = "USD"
CURRENCIES = ["EUR", "GBP", "JPY", "BRL", "AUD", "CAD"]
API_URL = "http://www.exchangerate-api.com/%s/%s/%f"

def exchange_rate():
    result = "Exchange Rates provided by http://www.travelground.com/ \n\n"
    for currency in CURRENCIES:
        url = urllib.urlopen(API_URL%(DEFAULT_UNITARY_CURRENCY,currency,1) + "?k="+API_KEY)
        exchange_rate = url.read()
        result = result + ("%s/%s - %s \n"%(DEFAULT_UNITARY_CURRENCY, currency, exchange_rate ))
    return result
    
    
    