'''Thomas Mullins
Date: 5/2/19
practice3.py
Definition: Create a program where the user can choose to view or add to a .txt
 file. The file will contain 5 numbers, as well as the sum of those numbers.
'''

import os
import re
#Created and initialized new txt file
emailFile = open('numberfile.txt', 'w')
emailFile.write('{:<1}{:>11}{:>11}{:>11}{:>11}{:>10}'.format('1st #', '2nd #', '3rd #', '4th #', '5th #', '\tTotal\n'))
emailFile.close()


def main(): #define main function
    while True: #exception handling start
        displayMenu() #call displayMenu for print statement
        try: #Begin if/elif to interpret user inputs
            command = input("Command: ")
            command = command.lower()
            if command == "view":
                view()
            elif command == "add":
                add()
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
        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break 


def displayMenu(): #Define displayMenu to offer user options
    print ("COMMAND MENU")
    print ("view - View username/e-mail file")
    print ("add  - Add user name/e-mail to file individually")
    print ("main - Return to command menu")
    print ("exit - Exit program")
    print()

def view(): #Define view, open and read current entries in emaildirectory.txt
    userFile = open('numberfile.txt', 'r')#open file/ 'r'
    userContent = userFile.read()#assign read file
    print(f'\n'+userContent+f'\n')#print content
    userFile.close()#close file


def add(): #define function for adding multiple users at a time
    newRegex = re.compile(r'\d+,\d+,\d+,\d+,\d+')#Regular expressions for validation
    newEntry = input('You have chosen to add five numbers to the .txt file.\nUse this format...\n\tnumber,number,number,'
                     'number,number >>>')
    #print('\tnumber,number,number,number,number')
    mo = newRegex.search(newEntry)#Search user entry for appropriate pattern
    while mo == None:#Loop for Validation for if no match can be made
        newEntry = input('Enter only 5 numbers seperated by commas: ')
        mo = newRegex.search(newEntry)#Recheck for match
    else:

        newEntryList = newEntry.split(',') #Change to list
        newEntryFixed = '' #new list to hold fixed items
        total = 0
        for u in range(len(newEntryList)): #loop for list
            newEntryList[u].strip() #strip empty space
            total += u
            newEntryFixed = newEntryList[u] + f'{"":^10}' #list items will now print to new lines
            userFile = open('numberfile.txt', 'a') #Open file with append
            userFile.write(newEntryFixed) #Write to file
            userFile.close() #close file
        userFile = open('numberfile.txt', 'a')
        userFile.write(f'{total:<}')
        userFile.close()
        print('\tThe directory has been updated.\n') #user verification


main()
