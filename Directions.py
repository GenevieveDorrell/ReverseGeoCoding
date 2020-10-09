from GeoMapping_API import getpoint
# Library converting latlon data to universal traverse mercator (UTM)
import utm

from math import sqrt

from gpx_parser import get_latlon

class direction:
    def __init__(self, street, direction, distance):  
        self.street = street
        self.direction = direction
        self.distance = distance

    def __repr__(self):
        return "street = % s\ndirection = % s\ndistance = % s\n" % (self.street, self.direction, self.distance)
lat_long = get_latlon("test_input_shortpi.gpx")

def directions(lat_long):
    point1 = getpoint(lat_long[0][0], lat_long[0][1], 0)
    #print(lat_long)    
    turn_points = bin_search([point1], (0, len(lat_long) - 1))
    print(turn_points)
    pass

#this Code is the logic behind the directions
def ll_to_utm(point):
    utm_convert = utm.from_latlon(point.lat, point.long)
    return utm_convert



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
        
def distance(point1, point2):
    utm1 = ll_to_utm(point1)
    utm2 = ll_to_utm(point2)
    
    dist = sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    return dist
    
def distance_processor(turn_points):
    distances = []
    
    for point_index in range(len(turn_points) - 1):
        point1 = turn_points[point_index]
        point2 = turn_points[point_index + 1]
        
        dist = distance(point1, point2)
        distances.append(dist)
        
    return distances
    
def direction_processor(lat_long, turn_points):
    return None
    
def bin_search_test():
    
    point1 = getpoint(lat_long[0][0], lat_long[0][1], 0)
    #print(lat_long)
    
    turn_points = bin_search([point1], (0, len(lat_long) - 1))
    print(turn_points)

    
bin_search_test()