def cli():
    inputf = ""
    while(inputf != "exit"):
        print("Enter the file name (including relative path) to your .gpx data (ex. data/input.gpx)")
        inputf = input("- ")
        if inputf == "exit":
            exit(1)

    return inputf
    
    
if __name__ == "__main__":
    cli()