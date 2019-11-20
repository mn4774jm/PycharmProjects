# scores = {'Al':5,'Betty':9,'Cole':8, 'Bea':2}
# scores["Dora"] = 7
# scores['Al'] = 6
# print(scores)
#
# # Remodeling? Use a list of rooms that you need to paint.
# rooms = ['Kitchen', 'Bedroom', 'Bathroom']
# # if you painted the bedroom…
# rooms.remove('Bedroom')
# # if you need to add the hallway…
# rooms.append('Hallway')
# print(rooms)

##############################################################

# # In contrast, use a dictionary to store the paint color for every room.
# roomsColors = {'Kitchen':'Blue', 'Bedroom':'Green', 'Bathroom':'Pink'}
# # painted the bedroom
# roomsColors.pop('Bedroom')
# # Need to paint the hallway
# roomsColors['Hallway'] = 'Beige'
# # What color was the kitchen supposed to be?
# kitchenColor = roomsColors['Kitchen']
# print('The kitchen will be painted ' + kitchenColor)

##############################################################
#
# # you can have strings as both keys and values
#countries = {'CA': 'Canada', 'US': 'United States',  'MX': 'Mexico', 'GB': 'Great Britain'}
#
# # you can have numbers as keys, strings as values
# numbers = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}
#
# # you can have strings as keys, mixed types as values
# book = {'name': 'Automate the Boring Stuff',  'year': 2018, 'price': 18.99 }
#
# # how to initialize a variable as an empty dictionary
# bookCatalog = {}
#
# # Code that gets a value from a dictionary
# country = countries['MX']   # "Mexico"
# #country = countries['IE']   # KeyError: Key doesn't exist
#
# # Code to re-set a value if the key is already there
# countries['GB'] = 'United Kingdom'
#
# #Code to add a key/value pair if it isn't in the dictionary
# countries['FR'] = 'France'
#
# #Syntax for checking if a key exists

#
# #Looping through keys and values
# for code in countries:
# 	print(code + '\t' + countries[code])code = 'EU'
# if code in countries:
# 	country = countries[code]
# 	print(country)
# else:
# 	print('There is no country for code: ' + code)
#
# for code in countries.keys():
# 	print(code + '\t' + countries[code])
#
# #unpacking a tuple (2 variables) for key and value
# for code, country in countries.items():
# 	print(code + '\t' + country)
#
# #Loop through values only
# for country in countries.values():
# 	print(country)
#
# #The get(method)
# country = countries.get('MX')				# "Mexico" works fine, if entry exists
# print(country)
# country = countries.get('IE')				# Doesn't exist…so, the next version is best
# print(country)
# country = countries.get('IE', 'Unknown')		# "Unknown" is returned rather than error
# print(country)
#
# #Syntax for deleting an item
# #del dictionary_name[key]
# #del countries['MX']
# #del countries['IE']		# KeyError: Key doesn't exist
#
# #Check if any key exists before deleting(To avoid the error)
# checkCode = 'IE'
# if checkCode in countries:
# 	country = countries[checkCode]
# 	del countries[checkCode]
# 	print (country + ' was deleted.')
# else:
# 	print ('There is no country for this code: ' + checkCode )
# print (countries)
#
# #Code using the pop() method - deleted value is returned
# country = countries.pop('US')			# "United States" – works because entry exists
# print(country)
# #country = countries.pop('IE')				# KeyError – entry doesn't exist
# #print(country)
# country = countries.pop('IE', 'Unknown')  	# "Unknown" – prevents error when no such code exists
# print(country)
# print(countries)
#
# #Code using the clear() method
# countries.clear()					# all deleted!
# print(countries)

##################################################################################################
#
'''Thomas Mullins
Date: 3/27/19
Definition: For your lab, you have to adapt the sample program to create a
personal contact information directory. You will need a variable called contacts,
of the dictionary data type. It stores usernames and emails as key-value pairs.
usernameEmail.py'''
#Dictionary Sample Program
def main(): #define main function
    try: #exception handling start
        #initializing email
        email_dict = {'Baxter': "stuffyGuy49@blah.com", "David" : "RodeoBoxer@...", "Arthur" : "the_answer_is@42.com"}
        displayMenu() #call displayMenu for print statement
        while True: #Begin if/elif to interpret user inputs
            command = input("Command: ")
            command = command.lower()
            if command == "view":
                view(email_dict)
            elif command == "add":
                add(email_dict)
            elif command == "edit":
                edit(email_dict)
            elif command == "del":
                delete(email_dict)
            elif command == "exit":
                print("Thank you for using the program.")
                break
            else:
                print ("Not a valid command. Please try again.") #response if input not recognized
                #print('To see menu options again type \'main\'\n')
                user_error()
    except KeyError: #exception handling for ditionary issues
        print ("Key Error ")

def displayMenu(): #Define displayMenu to offer user options
    print ("COMMAND MENU")
    print ("view - View Email by user name")
    print ("add  - Add a new user and Email address")
    print ('edit - Change a current user\'s email address')
    print ("del  - Delete a users account")
    print ("exit - Exit program")
    print()

def view(email_dict): #Define view, call displayUsers, ask for user name
    displayUsers(email_dict)
    user = input("Enter user name: ")
    user = user.title()#.upper function for uniformity
    if user in email_dict:
        name = email_dict[user]
        print("Current Email: " + name + "\n")
    else:#print statement if user name not recognized
        print("There is no user with that name.")
        user_error()

def add(email_dict): #Define add function,
    user = input("Enter user name: ")
    user = user.title()#.upper function for uniformity
    if user in email_dict:#print if address is already in use
        print(user + " is already using this address.")
        user_error()

    else: #if not already in use asks for email address
        import re
        emailRegex = re.compile(r'\w+@\w+\.\w{2,}')
        name = input("Enter email address: ")
        mo = emailRegex.search(name)
        while mo == None:
            name = input("Enter email address: ")
            mo = emailRegex.search(name)
        #name = name.title()#.title function for uniformity
        email_dict[user] = name
        print (name + " was added \n")#display verification

def edit(email_dict): #Define edit function
    user = input('Enter user name: ')
    user = user.title()#.upper function for uniformity
    if user in email_dict:
        new_address = input('Enter a new email address: ').title()
        #new_address = new_address.title()#.title function for uniformity

        #************  email_dict[user] = new_address #This is the standard that students will use   **********

        email_dict.update({user:new_address})#.update used to modify information
        print(user+'\'s Email has been updated to: '+new_address)# user verification print statement
    else:
        print('There is no user by that name.')
        user_error()

def delete(email_dict):#Define delete()
    user = input("Enter user name: ")
    user = user.title()#.upper function for uniformity
    if user in email_dict:
        name = email_dict.pop(user)#.pop function to remove user data
        print (name + " was deleted. \n")#User verification
    else:
        print ("There is no user with that name.")#print statement if user name not recognized
        user_error()

def displayUsers(email_dict):# Define display function
    users = list(email_dict.keys())#use list to print out keys in dictionary
    users.sort() #Sort keys alphabetically
    line = "Current user names: "#Print statement to preceed users in print
    for user in users:
        if user != users[-1]:
            line += user + ", "
        else:
            line += user + "."
    print(line)

def user_error(): #error statement call
    print('To see menu options again enter \'main\'\n')

if __name__ == '__main__':#If user input = main
    main() #call main

