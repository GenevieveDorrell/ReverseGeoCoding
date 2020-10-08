# import GeoMapping_API
# Library converting latlon data to universal traverse mercator (UTM)
import utm
# Used for visualizing path taken
import matplotlib.pyplot as plt

from math import sqrt

from gpx_parser import get_latlon

class direction:
    def __init__(self, fisrt_point, second_point, direction, distance, time):  
        self.fisrt_point = fisrt_point
        self.second_point = second_point
        self.direction = direction
        self.time = time

    def __repr__(self):
        return "direction = % s\ndistance = % s\ntime = % s\n" % (self.direction, self.distance, self.time)

# What percentage of points to graph 
RESOLUTION = 0.05

def directions(latlon_list)
    #bin_search(latlon_lit, ...)

#this Code is the logic behind the directions
def ll_to_utm(point):
    utm_convert = utm.from_latlon(point.lat, point.long)
    return utm_convert

def bin_search(lat_long, turn_points, indices):
    first = indices[0]
    last = indices[1]
    midpoint = (first + last) // 2
    
    first_ll = lat_long[first]
    last_ll = lat_long[last]
    mid_ll = lat_long[midpoint]
    
    first_address = getpoint(first_ll[0], first_ll[1], first)
    last_address = getpoint(last_ll[0], last_ll[1], last)
    mid_address = getpoint(mid_ll[0], mid_ll[1], midpoint)
    """
    
    first_street = first_address.street
    last_street = last_address.street
    mid_street = mid_address.street
    
    if len(lat_long) == 2 and first_street != last_street:
        turn_points.append(last_street)
    else:
        if first_street != mid_street:
            bin_search(lat_long, turn_points, (first, midpoint))
        if mid_street != last_street:
            bin_search(lat_long, turn_points, (midpoint, last))
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
    test_addresses = ["19th", "19th", "Franklin", "Agate", "Agate"]
    bin_search(test_addresses, ["19th"])

    
bin_search_test()