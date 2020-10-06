import requests
#import input

#this accesses the API resource

class address:
    def __init__(number, street, state, zipCode):
        self.number = number    
        self.street = street
        self.state = state
        self.zipCode = zipCode

url = "https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/HTTP/default.aspx"
apikey = '	4fec299ee59b4b2b8a38389b3d91e249'

variables = {'lon': '-123.0817087', 'lat': '44.039158', 'format': 'csv', 'apikey': apikey, 'notStore': 'false', 'includeHeader': 'true', 'version': '4.10'}
r = requests.get(url, params=variables)
parsed= r.text.split(',')
print(parsed)
