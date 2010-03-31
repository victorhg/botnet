

u = urllib.urlopen(url)



result_json = u.read()



data = json.loads(result_json)
print data['places']

for place in data:
    print data[polace]
    
    
    {'count': 1, 
     'start': 0, 
     'total': 25, 
     'place': [{
                'lang': 'en-US',
                 'admin2': '',
                 'country attrs': {'code': 'IE', 'type': 'Country'},
                 'name': 'Dublin',
                 'country': 'Ireland',
                  'areaRank': 5, 'popRank': 13, 'uri': 'http://where.yahooapis.com/v1/place/560743', 'admin1': 'Dublin', 'admin3': '', 'placeTypeName attrs': {'code': 7}, 'locality1 attrs': {'type': 'Town'}, 'locality1': 'Dublin', 'locality2': '', 'woeid': 560743, 'boundingBox': {'northEast': {'latitude': 53.440379999999998, 'longitude': -6.0438599999999996}, 'southWest': {'latitude': 53.223171000000001, 'longitude': -6.5088400000000002}}, 'centroid': {'latitude': 53.343761000000001, 'longitude': -6.24953}, 'admin1 attrs': {'code': 'IE-D', 'type': 'County'}, 'postal': '', 'placeTypeName': 'Town'}]}
