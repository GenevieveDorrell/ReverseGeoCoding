# Reverse Geocoding 

## Info-
Code Developed for reverse geocoding applications. This entails converting gps points into a cue sheet of directions. 

## Setup-
run the windowBuild.bat or UnixBuild.sh depending on your OS. These scripts will put you in the virtual envirinment and start runing the program. To call the run.cmd alone you must be in the virtual environment. On windows the command to reenter the venv after it has already been built is './env\Scripts\activate.bat' and 'source env/bin/activate' for apple. There is a stop.cmd script that you can call to exit the virtual environment, alternativly you can also type deactivate.


## Usage- 
used to take .gpx files and give the user verberbal directions.

## Requirements-
You must have python and pip preinstalled on your computer for the build scripts to work. Our web aplication will then install the venv packsge and then install these other third party pachages within the environment. 
- utm
- gpxpy
- math
- numpy
- flask

## Files & Directories-
* directions.py
-The main logic file. Calculates all of the streets that the route goes on, as well as distance on each street and turn direction from that street. 

* openMap_API.py
-Connects with the API to retrieve street addresses from the give gps points.

* gpx_parser.py .
-Parses a gpx input file and returns the latlon data in a list

* webApp.py
-Contains code for the main web interface of the project.

* static/
-Contains the css style sheet for the web GUI

* templates/
-Contians the home html page.

* uploads/
-Contains gpx files that the user uploads for duration of reverse geocoding process. Files are delete after use for security reasons. 

* tests/
-Contians .gpx files that you can use to test your setup.

## Acknowledgments-
This project uses reverse geocoding serveces from https://geoservices.tamu.edu/ API to convert latlon data to street addresses. 
