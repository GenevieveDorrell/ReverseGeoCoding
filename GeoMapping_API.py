import requests

#this accesses the API resource

class address:
    def __init__(self, street, lat, lon, index):  
        self.street = street
        self.lat = lat
        self.lon = lon
        self.index = index
    def __repr__(self):
        return "number = % s\nstreet = % s\ncity = % s\nstate = % s\nzipCode = % s\nlat = % s\nlon = % s\n" % (self.number,self.street,self.city,self.state,self.zipCode,self.lat,self.lon)

url = "https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/HTTP/default.aspx"
apikey = '4fec299ee59b4b2b8a38389b3d91e249'

def getpoint(lat, lon, index):
    variables = {'lon': lon, 'lat': lat, 'format': 'csv', 'apikey': apikey, 'notStore': 'false', 'includeHeader': 'false', 'version': '4.10'}
    r = requests.get(url, params=variables)
    parsed = r.text.split(',')
    street = parsed[5].split(' ', 1)
    point = address(street[0], street[1], parsed[6], parsed[7], parsed[8], lat, lon)
    print(point)
    return point

getpoint(44.039160,-123.079530)


