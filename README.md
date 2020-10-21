# Reverse Geocoding 

## Info-
Code Developed for reverse geocoding applications. This entails converting gps points into a cue sheet of directions. 

## Setup-
TODO
run the windowBuild.bat or UnixBuild.bash depending on your OS. 
Then run the run 

## Usage- 
TODO

## Requirements-
You must have python and pip preinstalled on your computer for the build scripts to work. Our web aplication will then install the venv packsge and then install these other third party pachages within the environment. 
- utm
- gpxpy
- math
- numpy
- flask
When you run the build script it will automatically call the run.cmd to call the run.cmd alone you must be in the virtual environment. There is a stop cmd that you can call the exit the virtual environment, alternativly you can also type deactivate.

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
-Contains gpx files that the user uploads for duration of reverse geocoding process.

* tests/

## Acknowledgments-
This project uses reverse geocoding serveces from https://geoservices.tamu.edu/ API to convert latlon data to street addresses. 
