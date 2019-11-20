
# Dictionary Sample Program
def main():
    try:
        countries = {"CA" : "Canada", "US" : "United States", "MX" : "Mexico"}
        displayMenu()
        while True:
            command = input("Command: ")
            command = command.lower()
            if command == "view":
                view(countries)
            elif command == "add":
                add(countries)
            elif command == "del":
                delete(countries)
            elif command == "exit":
                print("Bye!")
                break
            else:
                print ("Not a valid command. Please try again. \n")
    except KeyError:
        print ("Key Error ")

def displayMenu():
    print ("COMMAND MENU")
    print ("view - View country name")
    print ("add - Add a country")
    print ("del - Delete a country")
    print ("exit - Exit program")
    print()

def view(countries):
    displayCodes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print("Country name: " + name + ".\n")
    else:
        print("There is no country with that code. \n")

def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(name + " is already using this code. \n")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print (name + " was added. \n")

def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print (name + " was deleted. \n")
    else:
        print ("There is no country with that code. \n")

def displayCodes(countries):
    codes = list(countries.keys())
    codes.sort()
    line = "Country codes: "
    for code in codes:
        line += code + " "
    print(line)

if __name__ == '__main__':
    main()
