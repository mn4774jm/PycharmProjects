'''
Author: Thomas Mullins
Date: 4/22/19
directoryFile.py
Description: This program allows users to contribute to and view a text file
containing user names and email addresses.
'''

import os
import re


def main(): #define main function
    try: #exception handling start
        #create file if it doesn't already exist
        if not os.path.isfile('emailDirectory.txt'):
            emailFile = open('emailDirectory.txt', 'w')
            emailFile.write('mmouse mickeymouse@gmail.com\n')
            emailFile.close()

        displayMenu() #call displayMenu for print statement
        while True: #Begin if/elif to interpret user inputs
            command = input("Command: ")
            command = command.lower()
            if command == "view":
                view()
            elif command == "add":
                add()
            elif command == "add+":
                add_many()
            elif command == "main":
                main()
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
    print ("view - View username/e-mail file")
    print ("add  - Add user name/e-mail to file individually")
    print ("add+ - Add multiple users to the directory all at once")
    print ("main - Return to command menu")
    print ("exit - Exit program")
    print()

def view(): #Define view, open and read current entries in emaildirectory.txt
    userFile = open('emailDirectory.txt', 'r')#open file/ 'r'
    userContent = userFile.read()#assign read file
    print(f'\n'+userContent+f'\n')#print content
    userFile.close()#close file

# Created an additional function for users that need a little extra instruction. The bottom option seems like it could be
#     a little confusing for some.

def add(): #Define add function

    userRegex = re.compile(r'\w+')#Regex for user name
    print('You have chosen to add a new user name and e-mail address to the directory.')
    newUser = input("\tEnter new user name: ")#Create variable for new user name
    mo = userRegex.search(newUser)#Search match for regex
    while mo == None:#While loop for validation if no match found
        newUser = input('Please enter only letters and numbers; No spaces or special characters: ')
        mo = userRegex.search(newUser)

    #checks to make sure that user name is not already in directory
    existCheck = open('emailDirectory.txt', 'r') # open directory
    existTxt = existCheck.read()# read directory
    exist_regex = re.compile(f'{newUser}') #create search term using the user input
    mo = exist_regex.search(existTxt)# search txt file for match
    while mo is not None: # while loop if user name already exists in the file
        newUser = input('User name already exists. Please choose a different name: ')
        mo = exist_regex.search(newUser)
    existCheck.close()# close file

    #regex to ensure a properly formatted email is submitted
    emailRegex = re.compile(r'\w+@\w+[.]\w{2,}')#Regex for email
    newEmail = input('\tEnter the e-mail address for '+newUser+': ')#Create variable for new user email
    mo = emailRegex.search(newEmail)#Search for pattern match
    while mo == None:#Validation for email pattern match loop
        newEmail = input('Please enter a valid email address: ')
        mo = emailRegex.search(newEmail)

    newWrite = newUser+' '+newEmail #Combine user input
    newWrite = newWrite.lower() #lower case for uniformity
    newWriteFixed = newWrite+'\n' #adds newline for uniformity and easier reading
    userFile = open('emailDirectory.txt', 'a') #open file w/ append
    userFile.write(newWriteFixed) #add new data to file
    userFile.close() #close file
    print(newWrite+' Has been added to the directory.\n') #user verification
    #Repeat option
    answer = input('Would you like to add another user? Enter Y or N: ')
    while answer.upper() != 'Y' and answer.upper() != 'N':
        answer = input('Please enter Y or N: ')
    if answer.upper() == 'Y':
        print()
        add()
    else:
        print()
        return

def add_many(): #define function for adding multiple users at a time
    newRegex = re.compile(r'\w+\s\w+@\w+\.\w{2,},?')#Regular expressions for validation
    newEntry = input('You have chosen to add multiple users to the directory.\nUse this format...\n\t'
          'username email@address.com,username email@addess.com\n\t'
          '(Seperate each new contacts entry with a comma and no additional spaces): ')
    mo = newRegex.search(newEntry)#Search user entry for appropriate pattern
    while mo == None:#Loop for Validation for if no match can be made
        newEntry = input('Please use the above listed format: ')
        mo = newRegex.search(newEntry)#Recheck for match
    else:
        newEntry = newEntry.lower() #lower case for uniformity
        newEntryList = newEntry.split(',') #Change to list
        newEntryFixed = '' #new list to hold fixed items
        for u in range(len(newEntryList)): #loop for list
            newEntryList[u].strip() #strip empty space
            newEntryFixed = newEntryList[u] + '\n' #list items will now print to new lines
            userFile = open('emailDirectory.txt', 'a') #Open file with append
            userFile.write(newEntryFixed) #Write to file
            userFile.close() #close file
        print('The directory has been updated.\n') #user verification

main()

