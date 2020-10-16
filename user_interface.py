def cli():
    inputf = ""
    print("Enter the file name (including relative path) to your .gpx data (ex. data/input.gpx)")
    inputf = input("- ")
    return inputf
    
if __name__ == "__main__":
    cli()