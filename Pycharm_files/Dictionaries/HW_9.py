'''Author: Thomas Mullins
Date: 4/1/19
authorBook.py
Definition: Write a program that creates a variable called readings,
of the dictionary data type. It stores your favorite authors and book titles, as key-value pairs.
'''
import pprint
def main(): #define main function
    try: #exception handling start
        #initializing email
        readings = {'Neil Gaiman': "Neverwhere", "David Wong" : "This book is full of spiders",
                    "Douglas Adams" : "Hitchhikers Guide to the Galaxy"}
        displayMenu() #call displayMenu for print statement
        while True: #Begin if/elif to interpret user inputs
            command = input("Command: ")
            command = command.lower()
            if command == "view":
                view(readings)
            elif command == "all":
                print_all(readings, 20, 6)
            elif command == "add":
                add(readings)
            elif command == "main":
                main()
            elif command == "edit":
                edit(readings)
            elif command == "del":
                delete(readings)
            elif command == "exit":
                print("Thank you for using the program.")
                break
            else:
                print ("Not a valid command. Please try again.") #response if input not recognized
                print('To see menu options again type \'main\'\n')
    except KeyError: #exception handling for ditionary issues
        print ("Key Error ")

def displayMenu(): #Define displayMenu to offer user options
    print ("COMMAND MENU")
    print ("all  - View all items")
    print ("view - View readings")
    print ("add  - Add a reading")
    print ('edit - Edit a reading')
    print ("del  - Delete a reading")
    print ("exit - Exit program")
    print()

def view(readings): #Define view, call displayUsers, ask for user name
    displayAuthors(readings)
    author = input("Enter author name: ").title()
    #author = author.title()#function for uniformity
    if author in readings:
        name = readings[author]
        print("Currently reading: " + name + "\n")
    else:#print statement if author name not recognized
        print("There is no author with that name in the directory.\n")


def print_all(readings, leftWidth, rightWidth):
    print('CURRANT AUTHORS AND READINGS'.center(leftWidth + rightWidth, '-'))
    for k, v in readings.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


def add(readings): #Define add function,
    author = input("Enter author\'s name: ")
    author = author.title()#function for uniformity
    if author in readings:#print if author is already in use
        print(author + " is already in the directory.\n")

    else: #if not already in use asks for current reading
        name = input("Enter the current reading for " +author+": ")
        name = name.title()#.title function for uniformity
        readings[author] = name
        print (name +' by '+author+ " was added \n")#display verification
    print()

def displayAuthors(readings):# Define display function
    authors = list(readings.keys())#use list to print out keys in dictionary
    authors.sort() #Sort keys alphabetically
    line = "Current author names: "#Print statement to preceed users in print
    for author in authors:
        line += author + ", "
    print(line)

def edit(readings): #Define edit function
    author = input('Enter author name: ')
    author = author.title()#.upper function for uniformity
    if author in readings:
        new_reading = input('Enter a new current reading: ').title()
        readings.update({author:new_reading})#.update used to modify information
        print(author+'\'s current reading has been updated to: '+new_reading+'\n')# user verification print statement
    else:
        print('There is no author by that name in the directory.\n')
    print()


def delete(readings):#Define delete()
    author = input("Enter author\'s name: ")
    author = author.title()#function for uniformity
    if author in readings:
        name = readings.pop(author)#.pop function to remove author data but keep the value
        print (author+' and '+ name + " have been deleted. \n")#User verification
    else:
        print ("There is no author with that name in the directory.\n")#print statement if author name not recognized
    print()


main()

# book_list = []
# author_dict = {}
# author_name = input("Please enter the authors name: ")
# reading = input("Please enter the name of the reading: ")
# book_list.append(reading)
# author_dict[author_name] = book_list
# moreBooks = input("Enter another reading? (Y or N)").upper()
# while moreBooks != "Y" and moreBooks != "N":
#     more = input("Please enter Y or N: ") .upper()
# if moreBooks != 'N':
#     anotherReading = input("Gimme a second book: ")
#     book_list.append(anotherReading)
#     author_dict[author_name] = book_list
# print(author_dict)





