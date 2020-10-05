# Parser for gpx files

# Library for reading gpx files and parsing latlon data
import gpxpy
import gpxpy.gpx
# Library converting latlon data to universal traverse mercator (UTM)
import utm
# Library for calculating distances
import geopy
# Used for visualizing path taken
import matplotlib.pyplot as plt

# What percentage of points to graph, 
RESOLUTION = 0.05

gpx_f = open('test_input.gpx', 'r')
gpx = gpxpy.parse(gpx_f)


# "0" point to calculate time since initial point
point_1 = gpx.tracks[0].segments[0].points[0]
time_1 = point_1.time

tdeltas = []
lat_long = []
# Parse latlon data and store it as a list of tuples
for tracks in gpx.tracks:
    for segment in tracks.segments:
        for point in segment.points:
            lat_long.append((point.latitude, point.longitude))
            tdeltas.append((point.time - time_1).total_seconds())

# Convert latlon data to utm data to work with grid representation
# TODO: considering converting to utm in earlier loop      
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
    