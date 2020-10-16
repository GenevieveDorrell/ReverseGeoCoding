# Reverse Geocoding 

## Info-
Code Developed for reverse geocoding applications. This entails converting gps points into a cue sheet of directions. 

## Usage- 
TODO

## Requirements-
The requirements for this project include:
- requests
- utm
- gpxpy
- math
- numpy

## Setup-
TODO

## Files & Directories-
* directions.py
-The main logic file. Calculates all of the streets that the route goes on, as well as distance on each street and turn direction from that street. 

* geomapping_API.py
-Connects with the API to retrieve street addresses from the give gps points.

* gpx_parser.py .
-Parses a gpx input file and returns the latlon data in a list

* webApp.py
-Contains code for the main web interface of the project.

* static/

* templates/

* uploads/

* tests/

## Acknowledgments-
This project uses reverse geocoding serveces from https://geoservices.tamu.edu/ API to convert latlon data to street addresses. 
