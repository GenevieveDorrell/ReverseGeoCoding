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

#this Code is the logic behind the directtions
   
""" This is code that loops through a list of latlon data and converts to utm """
"""     
    utm_points = []
    for point in lat_long:
        utm_conver = utm.from_latlon(point[0], point[1])
        utm_points.append((utm_conver[0], utm_conver[1]))

    # Take a subset of the points to garph
    tdeltas_graph = []
    utm_graph_x = []
    utm_graph_y = []
    num_p = int(1 / RESOLUTION)
    for i in range(0, len(utm_points), num_p):
        tdeltas_graph.append(tdeltas[i])
        utm_graph_x.append(utm_points[i][0])
        utm_graph_y.append(utm_points[i][1])

    # Graph route
    scat = plt.scatter(utm_graph_x, utm_graph_y, c=tdeltas_graph)
    plt.colorbar(scat)
    plt.show()
"""