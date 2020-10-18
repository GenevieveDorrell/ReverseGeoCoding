from geoMapping_API import getpoint
# Library converting latlon data to universal traverse mercator (UTM)
import utm

from math import sqrt

from numpy import arccos

from gpx_parser import get_latlon

class direction:
    def __init__(self, street, direction, distance):
        self.street = street
        self.direction = direction
        self.distance = distance

    def __repr__(self):
        return "street = % s\ndirection =ma % s\ndistance = % s\n" % (self.street, self.direction, self.distance)

def directions(lat_long):
    # Create a global variable so that it doesn't need to be passed into recursive call
    global lat_long
    # First diection in cue sheet
    point1 = getpoint(lat_long[0][0], lat_long[0][1], 0)
    print(point1)
    # Calculates other directinos in the cue sheet
    turn_points = bin_search([point1], (0, len(lat_long) - 1))
    # Calculates distances driven on each road
    distances = distance_processor(turn_points)
    # Calculates direction turned at each road change
    directions = direction_processor(lat_long, turn_points, distances)
    #print(directions)
    return directions



""" Converts latlon data to utm data to calculate distances """
def ll_to_utm(point):
    utm_convert = utm.from_latlon(point.lat, point.lon)
    return utm_convert

""" Performs a binary search on the lat/long list to find the points where
    streets change """
def bin_search(turn_points, indices):
    first = indices[0]
    last = indices[1]
    midpoint = (first + last) // 2

    first_ll = lat_long[first]
    last_ll = lat_long[last]
    mid_ll = lat_long[midpoint]

    first_address = getpoint(first_ll[0], first_ll[1], first)
    last_address = getpoint(last_ll[0], last_ll[1], last)
    mid_address = getpoint(mid_ll[0], mid_ll[1], midpoint)

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

""" Calculates the euclidean distance between two points """
def distance(point1, point2):
    utm1 = ll_to_utm(point1)
    utm2 = ll_to_utm(point2)

    dist = sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    return dist

""" Calculates the distance between all adjacent points in cue sheet """
def distance_processor(turn_points):
    distances = []
    for point_index in range(len(turn_points) - 1):
        point1 = turn_points[point_index]
        point2 = turn_points[point_index + 1]

        dist = distance(point1, point2)
        distances.append(dist)

    return distances

""" Calculates the turn direction between two points """
def direction_calc(lat_long, point):
    index_behind = point.index - 10
    index_ahead = point.index + 10

    point_behind = getpoint(lat_long[index_behind][0], lat_long[index_behind][1], index_behind)
    point_ahead = getpoint(lat_long[index_ahead][0], lat_long[index_ahead][1], index_ahead)

    utm_behind = ll_to_utm(point_behind)
    utm_current = ll_to_utm(point)
    utm_ahead = ll_to_utm(point_ahead)

    dir = ((utm_current[0]-utm_behind[0]) * (utm_ahead[1]-utm_behind[1])) - ((utm_current[1] - utm_behind[1]) * (utm_ahead[0]-utm_behind[0]))

    if dir > 0.01:
        return "turn left"
    elif dir < -0.01:
        return "turn right"
    else:
        return "go straight"

""" Calculates the turn direction between adjacent points in cue sheet """
def direction_processor(lat_long, turn_points, distances):
    directions = []
    direction1 = direction(turn_points[0].street, "start", None)
    directions.append(direction1)

    for i in range(1, len(turn_points)):
        dir = direction_calc(lat_long, turn_points[i])
        direction_current = direction(turn_points[i].street, dir, distances[i-1])

        directions.append(direction_current)

    return directions

if __name__ == "__main__":
    latlon = get_latlon("tests/test_input.gpx")
    directions(latlon)
