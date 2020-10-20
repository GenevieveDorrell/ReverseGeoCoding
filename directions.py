from openMap_API import getaddress, get_apikey
# Library converting latlon data to universal traverse mercator (UTM)
import utm

from math import sqrt

from numpy import arccos

from gpx_parser import get_latlon

class direction:
    def __init__(self, street, direction, distance):
        self.street = street
        self.direction = direction
        if distance is not None:
            self.distance = round(distance / 1000, 2)
        else:
            self.distance = 0.0

    def __repr__(self):
        return "{} on {} - {}km".format(self.direction, self.street, self.distance)



def get_directions(lat_lon):
    # Create a global variable so that it doesn't need to be passed into recursive call
    global lat_long
    global apikey 
    apikey = get_apikey()
    lat_long = lat_lon
    # First diection in cue sheet
    address1 = getaddress(lat_long[0][0], lat_long[0][1], 0, apikey)
    # Calculates other directions in the cue sheet
    turn_points = bin_search([address1], (0, len(lat_long) - 1))
    turn_points.append(getaddress(lat_long[-1][0], lat_long[-1][1], len(lat_long) - 1, apikey))
    # Calculates distances driven on each road
    distances = distance_processor(turn_points)
    # Calculates direction turned at each road change
    directions = direction_processor(turn_points, distances)
    for direction in directions:
        print(direction)
    return directions

""" Performs a binary search on the lat/long list to find the points where
    streets change """
# Takes in a list of turn points a pair of indices
def bin_search(turn_points, indices):
    first = indices[0]
    last = indices[1]
    midpoint = (first + last) // 2

    first_ll = lat_long[first]
    last_ll = lat_long[last]
    mid_ll = lat_long[midpoint]

    first_address = getaddress(first_ll[0], first_ll[1], first, apikey)
    last_address = getaddress(last_ll[0], last_ll[1], last, apikey)
    mid_address = getaddress(mid_ll[0], mid_ll[1], midpoint, apikey)

    first_street = first_address.street
    last_street = last_address.street
    mid_street = mid_address.street

    if (last-first==1) and first_street != last_street:
        turn_points.append(last_address)
    else:
        if first_street != mid_street:
            bin_search(turn_points, (first, midpoint))
        if mid_street != last_street:
            bin_search(turn_points, (midpoint, last))
    return turn_points

""" Calculates the distance between all adjacent points in cue sheet """
def distance_processor(turn_points):
    distances = []
    for point_index in range(len(turn_points) - 1):
        address1 = turn_points[point_index]
        address2 = turn_points[point_index + 1]
        dist = distance(address1, address2)
        distances.append(dist)
    last_point = getaddress(lat_long[-1][0], lat_long[-1][1], (len(lat_long) - 1), apikey)
    distances.append(distance(turn_points[-1], last_point))
    return distances

""" Calculates the turn direction between adjacent points in cue sheet """
def direction_processor(turn_points, distances):
    directions = []
    # Starting point
    direction1 = direction(turn_points[0].street, "Start", None)
    directions.append(direction1)

    for i in range(1, len(turn_points) - 1):
        dir = direction_calc(turn_points[i])
        direction_current = direction(turn_points[i].street, dir, distances[i-1])
        directions.append(direction_current)

    # Ending point
    last_direction = direction(turn_points[-1].street, "End", distances[-1])
    directions.append(last_direction)

    return directions

""" AUXILLIARY FUNCTION """
""" Converts latlon data to utm data to calculate distances """
def ll_to_utm(address):
    lat, lon = address_to_latlong(address)
    utm_convert = utm.from_latlon(lat, lon)
    return utm_convert

""" Calculates the euclidean distance between two points """
def distance(address1, address2):
    utm1 = ll_to_utm(address1)
    utm2 = ll_to_utm(address2)

    dist = sqrt((utm2[0] - utm1[0]) ** 2 + (utm2[1] - utm1[1]) ** 2)
    return dist

""" Calculates the turn direction between two points """
def direction_calc(address):
    # Find a point ahead of and a point behind to calculate turn direction
    ind = address.index
    """
    if ind - 3 < 0:
        index_behind = ind - 1
    elif ind - 5 < 0:
            index_behind = ind - 3
    elif ind - 10 < 0:
            index_behind = ind - 5
    else:
        index_behind = ind - 10
    """

    """
    max_ind = len(lat_long) - 1
    if ind + 3 > max_ind:
        index_ahead = ind + 1
    elif ind + 5 > max_ind:
        index_ahead = ind + 3
    elif ind + 10 > max_ind:
        index_ahead = ind + 5
    else:
        index_ahead = ind + 10
    """
    index_behind = ind - 2
    index_ahead = ind + 2

    address_behind = getaddress(lat_long[index_behind][0], lat_long[index_behind][1], index_behind, apikey)
    address_ahead = getaddress(lat_long[index_ahead][0], lat_long[index_ahead][1], index_ahead, apikey)
    
    
    utm_behind = ll_to_utm(address_behind)
    utm_current = ll_to_utm(address)
    utm_ahead = ll_to_utm(address_ahead)
    

    dir = ((utm_current[0]-utm_behind[0]) * (utm_ahead[1]-utm_behind[1])) - ((utm_current[1] - utm_behind[1]) * (utm_ahead[0]-utm_behind[0]))
    twoRoads = address_behind.street.split(';')
    if len(twoRoads) > 1: #checkes to see if change is just from street name change
        if address.street in twoRoads:
            return "Continue onto"           
    if dir > 1:
        return "Turn left"
    elif dir < -1:
        return "Turn right"
    else:
        return "Go straight"

""" Returns a latlong pair from an address object """
def address_to_latlong(address):
    return address.lat, address.lon


if __name__ == "__main__":
    latlon = get_latlon("tests/test_input_short.gpx")
    get_directions(latlon)
