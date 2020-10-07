import GeoMapping_API
# Library converting latlon data to universal traverse mercator (UTM)
import utm
# Used for visualizing path taken
import matplotlib.pyplot as plt

from gpx_parser import get_latlon

# What percentage of points to graph 
RESOLUTION = 0.05

latlon_list = get_latlon("test_input.gpx")
print(latlon_list)

#this Code is the logic behind the directions
def ll_to_utm(lat_long):
    utm_points = []
    for point in lat_long:
        utm_conver = utm.from_latlon(point[0], point[1])
        utm_points.append((utm_conver[0], utm_conver[1]))

    return utm_points

def bin_search(lat_long):
    first_ll = lat_long[0]
    last_ll = lat_long[-1]
    mid_ll = lat_long[len(lat_long) // 2]
    
    """
    first_address = functionCall(first_ll)
    last_address = functionCall(last_ll)
    mid_address = functionCall(mid_ll)
    
    first_street = first_address.street
    last_street = last_address.street
    mid_address = mid_address.street
    """
    
    
    
    
