#Used to initialize the txt; will write to the current directory

import os #Required to function
#initialize/create file
emailFile = open('emailDirectory.txt', 'w')
emailFile.write('mmouse mickeymouse@gmail.com\n')
emailFile.close()

#Viewing txt
def view(): #Define view, open and read current entries in emaildirectory.txt
    userFile = open('emailDirectory.txt', 'r')#open file/ 'r'
    userContent = userFile.read()#assign read file
    print(f'\n'+userContent+f'\n')#print content
    userFile.close()#close file

#Adding
userFile = open('emailDirectory.txt', 'a')  # open file w/ append
userFile.write(newWriteFixed)  # add new data to file
userFile.close()  # close file
print(newWrite + ' Has been added to the directory.\n')  # user verification


#Csv
import csv
#Initializing a new csv
file_start = open('data_collection.csv', 'w', newline='')#Create new file
outputWriter = csv.writer(file_start)#create writer object
(outputWriter.writerow(['Name', 'Email', 'Phone']))#Give writerow a list
file_start.close()#close file

#Viewing a csv

def view(): #Define view, open and read current entries in emaildirectory.txt
    userFile = open('data_collection.csv', 'r')#open file/ 'r'
    userContent = csv.reader(userFile)#assign read file
    userData = list(userContent) #Convert to list
    userFile.close()  # close file

    # For loop for each item in csv
    for lines in userData:
        # For loop to format each line w/spacing
        for item in lines:
            print(format(item, '30'), end='')
        print()

#Adding to csv

#Begin writing to csv
    data_file = open('data_collection.csv', 'a')#Open file and set to append mode
    data_writer = csv.writer(data_file)#Create writer object
    data_writer.writerow([newName,newEmail,newPhone])#Writerow
    print(newName+' Has been added successfully\n')#confirmation print
    data_file.close()#Close file
