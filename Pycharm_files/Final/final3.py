'''
Thomas Mullins
Definition: Write a program to create a .csv file that contains contact information, and reads from that file.
Final3.py
5/9/19
'''


import re, csv
phoneRegex = re.compile(r'(\d{3})\.?-?(\d{3}\.?-?\d{4})')  # Regex for phone number
emailRegex = re.compile(r'\w+@\w+\.\w{2,}')
'''***********After File is created, this is commented out as to not overwrite the original file each time***********'''
# file_start = open('final_3.csv', 'w', newline='')#Create new file
# outputWriter = csv.writer(file_start)#create writer object
# (outputWriter.writerow(['First Name', 'Last Name', 'Email', 'Phone']))#Give writerow a list
# file_start.close()#close file

def main(): #define main function
    try: #exception handling start
        displayMenu() #call displayMenu for print statement
        while True: #Begin if/elif to interpret user inputs
            command = input("\nCommand: ")
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
                print ("Not a valid command. Please try again.\n") #response if input not recognized

    except Exception as err: #exception handling
        print (err)

def displayMenu(): #Define displayMenu to offer user options
    print ("COMMAND MENU")
    print ("view - View contact file")
    print ("add  - Add contact to file")
    print ("exit - Exit program")

def view(): #Define view, open and read current entries in emaildirectory.txt
    print('Your current .csv contact list:')
    userFile = open('final_3.csv', 'r')#open file/ 'r'
    userContent = csv.reader(userFile)#assign read file
    userData = list(userContent) #Convert to list
    userFile.close()  # close file

    # For loop for each item in csv
    for lines in userData:
        # For loop to format each line w/spacing
        for item in lines:
            print(format(item, '30'), end='')
        print()


def add(): #Define add function
    nameRegex = re.compile(r'[a-zA-Z]+')#Regex for user name

    newName = input("\tEnter new contacts First name: ")#Create variable for new name
    newName = newName.title() #Title case for name (JUst to make it pretty
    mo = nameRegex.search(newName)#Search match for regex
    while mo == None:#While loop for validation if no match found
        newName = input('Please enter letters only in this format: ')
        mo = nameRegex.search(newName)
    newName = newName.title()
    nameRegex = re.compile(r'[a-zA-Z]+')  # Regex for user name

    newNameLast = input("\tEnter new contacts Last name: ")  # Create variable for new name
    newNameLast = newNameLast.title()  # Title case for name (JUst to make it pretty
    mo = nameRegex.search(newNameLast)  # Search match for regex
    while mo == None:  # While loop for validation if no match found
        newNameLast = input('Please enter letters only in this format: ')
        mo = nameRegex.search(newNameLast)
    newNameLast = newNameLast.title()
    emailRegex = re.compile(r'\w+@\w+\.\w{2,}')#Regex for email
    newEmail = input('\tEnter the e-mail address for '+newName+': ')#Create variable for new user email
    mo = emailRegex.search(newEmail)#Search for pattern match
    while mo == None:#Validation for email pattern match loop
        newEmail = input('Please enter a valid email address: ')
        mo = emailRegex.search(newEmail)

    phoneRegex = re.compile(r'(\d{3})\.?-?(\d{3}\.?-?\d{4})')#Regex for phone number
    newPhone = input('\tPlease enter phone number for '+newName+': ')
    mo = phoneRegex.search(newPhone)  # Search for pattern match
    while mo == None:  # Validation for email pattern match loop
        newPhone = input('Please enter a valid phone number: ')
        mo = phoneRegex.search(newPhone)

    #Begin writing to csv
    data_file = open('final_3.csv', 'a')#Open file and set to append mode
    data_writer = csv.writer(data_file)#Create writer object
    data_writer.writerow([newName,newNameLast,newEmail,newPhone])#Writerow
    #print(newName+' '+newNameLast+' Has been added successfully\n')#confirmation print
    data_file.close()#Close file

main()

