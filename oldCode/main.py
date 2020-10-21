
from User_interface import cli
from gpx_parser import get_latlon
from Directions import directions

def main():
    input_f = cli()
    latlon = get_latlon(input_f)
    directions(latlon)
    return

if __name__ == "__main__":
    main()