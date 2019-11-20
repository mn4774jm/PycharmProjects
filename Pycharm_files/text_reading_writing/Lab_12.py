import os
import shelve
import pprint
import re

# print('Using the os module and the os.path module')
# print('''Show correct path to a folder (directory) using the
# 	join function, which will return a string based
# 	on your operating system. \n''')
# print("for example: os.path.join('users', 'shared', 'android')")
# print(os.path.join('users', 'shared', 'android'))
# print()

##########################################################################

# print('Current working directory - compare yours')
# print('Command: os.getcwd()')
# print(os.getcwd())
# print()

##########################################################################

# print('''\nchdir: to change working directory for Windows,
# 	use a raw string for the path.
# 	Don't forget to change back if needed!\n''')
# os.chdir(r'/users/tom/pycharmprojects/week_13')
# print(os.getcwd())

##########################################################################

# print('Now create a precise path to a directory folder and filename')
# print("The variable myFiles is set to the list: ['accounts.txt', 'details.csv', 'friends.docx']")
# myFiles=['accounts.txt', 'details.csv', 'friends.docx']
# for fileID in range(len(myFiles)):
#     print(os.path.join(r'/users/tom/PycharmProjects/week_13/') + myFiles[fileID])
# print()

###########################################################################

# print('Try the appropriate version for your OS')
# os.chdir('/Users/NoSuchFolder/')    # OS X or Linux
# #os.chdir(r'C:\Users\NoSuchFolder\'')  # Windows
#
# #To avoid having an error stop your program, add exception handling
# try:
# 	os.chdir('/Users/NoSuchFolder/') 	# OS X or Linux
# 	#os.chdir(r'C:\Users\NoSuchFolder\'') 	# Windows
# except:
# 	print('File or folder does not exist')

############################################################################

# print('Creating new directory folders.')
# myPath = os.getcwd()	# get current working directory
# print(myPath)
# print('Create a new directory: testDir')
# os.makedirs(myPath+'/testDir')  #  Mac
# #os.makedirs(myPath+r'\testDir')  #  Windows
# print('OK I think that worked.')
# print('If so, comment out that code line – you can only use it once.')

############################################################################

# print()
# print('''Now list the files and folders in the current directory
#     with os.listdir(os.getcwd()\n''')
# print(os.listdir(os.getcwd()))
# print()

############################################################################

# myFile = open('myFile.txt','w')     # w for write mode
# myFile.write('Hello Earth!\n')
# myFile.write('Hello Mars!\n')
# myFile.close()
# print('Done!')

#############################################################################

# myFile = open('myFile.txt', 'a')     # 'a' for append mode
# myFile.write('Hello Venus!\n')
# myFile.write('Hello Jupiter!\n')
# myFile.close()
# print('Done again!')

############################################################################

# myFile = open('myFile.txt', 'r') # r for read mode
# myData = myFile.read() # read the entire file into one string
# print(myData)
# myFile.close()  # close the file
# print()   # blank line

###########################################################################

# myFile = open('myFile', 'r')    # r for read mode
# myData = myFile.readlines()       # read the entire file into a list
# print(myData)
# myFile.close()       # close the file
# print()     # blank line

###########################################################################

# myFile = open('myFile.txt', 'r')     # r for read mode
# myData = myFile.readline()        # read the first line
# print('Single line from file:' + myData)
#
# # here it's used with a loop
# while myData != '':         #  2 single quotes, remember!
# 	print(myData, end='')              # end='' overides the default newline escape code
# 	myData = myFile.readline()   # loop through a line at a time
# myFile.close()  # close the file
# print()   # blank line

##########################################################################

inviteFile = open('partyInvites.txt','w') # w for write mode
inviteFile.write('Hostess - Betty Boop\n')# initialize a txt file
inviteFile.close()
# original input is a string, with commas separating each entry
userInput = input('Enter guest names, separating each one with a comma. ')
userInputList = userInput.split(',')# change to a list
userInputFixed = ''  # a new string to hold the fixed items, so they can be written to the file
for i in range(len(userInputList)):
	userInputList[i].strip()
	userInputFixed = 'Guest ' + str(i + 1) + ' - ' + userInputList[i] + '\n'
	inviteFile = open('partyInvites.txt','a') # for append mode
	inviteFile.write(userInputFixed)
inviteFile.close()
