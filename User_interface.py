def cli():
    inputf = ""
    while(inputf != "exit"):
        try:
            print("Enter the file name (including relative path) to your .gpx \ 
                  data (ex. data/input.gpx)")
            inputf = input("- ")
            if inputf == "exit":
                exit(1)
        except FileNotFoundError:
            print("Could not find file " + inputf + ", please try again or type 'exit'")
            continue
        
        print(inputf)
        get_latlon(inputf)
    
    
if __name__ == "__main__":
    cli()