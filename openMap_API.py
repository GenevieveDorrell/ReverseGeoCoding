
from geopy.geocoders import OpenMapQuest
from geopy.exc import GeocoderAuthenticationFailure

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
#our apikey is 15NPW4foGDU81YFkcoMBMLHNkLFFKCXi

def get_apikey():
    try:
        f = open("ApiKey.txt", "r")
        apikey = f.read()
        f.close()
        return apikey
    except:
        print("error no apikey file specified try running command \'python .\getApiKey.py\'")
        exit(1)

def getaddress(lat, lon, index, apikey):
    try:
        loc = str(lat) + ", " + str(lon)
        locator = OpenMapQuest(api_key=apikey)
        print(locator.reverse(loc))
        location = locator.reverse(loc)
        parsed = location.raw
        addres = parsed['address']
        street = addres['road']
        point = address(street, lat, lon, index)
        return point
    except:
        print("You have an incorrect API or are out of credits to configure a new api key run \'python .\getApiKey.py\'")
        exit(1)
#print(getaddress(44.587662, -123.256691, 0, 'asdkfjasldf'))
#print(getaddress(44.589523, -123.262482, 0))
#print(get_apikey())