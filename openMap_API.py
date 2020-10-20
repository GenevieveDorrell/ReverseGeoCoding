import requests
from geopy.geocoders import OpenMapQuest

#this accesses the API resource
#account balance query
#
class address:
    def __init__(self, street, lat, lon, index):
        self.street = street
        self.lat = lat
        self.lon = lon
        self.index = index

    def __repr__(self):
        return "street = % s\nlat = % s\nlon = % s\nIndex = % s\n" % (self.street,self.lat,self.lon,self.index)

url = "http://open.mapquestapi.com/geocoding/v1/reverse"
apikey = '15NPW4foGDU81YFkcoMBMLHNkLFFKCXi'

def getaddress(lat, lon, index):
    loc = str(lat) + ", " + str(lon)
    locator = OpenMapQuest(api_key=apikey)
    location = locator.reverse(loc)
    parsed = location.raw
    addres = parsed['address']
    street = addres['road']
    point = address(street, lat, lon, index)
    return point

#print(getaddress(44.587662, -123.256691, 0))
#print(getaddress(44.589523, -123.262482, 0))
