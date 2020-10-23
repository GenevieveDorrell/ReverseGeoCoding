Apikey = input("Please enter your Open Map Quest Api key:")
f = open("ApiKey.txt", "w")
f.write(Apikey)
f.close()