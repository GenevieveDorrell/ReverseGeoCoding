# Parser for gpx files

# Library for reading gpx files and parsing latlon data
import gpxpy
import gpxpy.gpx

def get_latlon(input_f): 
    gpx_f = open('input', 'r')
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
                
    return lat_long


    