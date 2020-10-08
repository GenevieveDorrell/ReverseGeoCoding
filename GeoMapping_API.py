import requests

#this accesses the API resource

class address:
    def __init__(self, street, lat, lon, index):  
        self.street = street
        self.lat = lat
        self.lon = lon
        self.index = index

    def __repr__(self):
        return "street = % s\nlat = % s\nlon = % s\nIndex = % s\n" % (self.street,self.lat,self.lon,self.index)

url = "https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/HTTP/default.aspx"
apikey = '4fec299ee59b4b2b8a38389b3d91e249'

def getpoint(lat, lon, index):
    variables = {'lon': lon, 'lat': lat, 'format': 'csv', 'apikey': apikey, 'notStore': 'false', 'includeHeader': 'false', 'version': '4.10'}
    r = requests.get(url, params=variables)
    parsed = r.text.split(',')
    street = parsed[5].split(' ', 1)
    point = address(street[1], lat, lon, index)
    print(point)
    return point

#getpoint(44.039160,-123.079530, 0)


