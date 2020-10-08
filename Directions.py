# import GeoMapping_API
# Library converting latlon data to universal traverse mercator (UTM)
import utm
# Used for visualizing path taken
import matplotlib.pyplot as plt

from gpx_parser import get_latlon

# What percentage of points to graph 
RESOLUTION = 0.05

latlon_list = get_latlon("test_input.gpx")

#this Code is the logic behind the directions
def ll_to_utm(lat_long):
    utm_points = []
    for point in lat_long:
        utm_conver = utm.from_latlon(point[0], point[1])
        utm_points.append((utm_conver[0], utm_conver[1]))

    return utm_points

def bin_search(test_addresses, turn_points):
    
    """
    CHANGE PARAM TO lat_long
    
    first_ll = lat_long[0]
    last_ll = lat_long[-1]
    mid_ll = lat_long[len(lat_long) // 2]
    
    first_address = functionCall(first_ll)
    last_address = functionCall(last_ll)
    mid_address = functionCall(mid_ll)
    
    first_street = first_address.street
    last_street = last_address.street
    mid_address = mid_address.street
    """
    #TestCode
    
    midpoint = len(test_addresses) // 2
    
    first_street = test_addresses[0]
    last_street = test_addresses[-1]
    mid_street = test_addresses[midpoint]
    
    if len(test_addresses) == 2:
        if first_street != last_street:
            turn_points.append(last_street)
    else:
        if first_street != mid_street:
            bin_search(test_addresses[0 : midpoint+1], turn_points)
        if mid_street != last_street:
            bin_search(test_addresses[midpoint:], turn_points)
    print(turn_points)
    return turn_points
        
    
    
def bin_search_test():
    test_addresses = ["19th", "19th", "Franklin", "Agate", "Agate"]
    bin_search(test_addresses, ["19th"])
    
bin_search_test()