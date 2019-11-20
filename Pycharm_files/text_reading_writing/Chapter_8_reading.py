import os #Must be imported for any of this to work

'''########################################################################

Basic calls and functions'''

# os.getcwd() #returns current working directory
#
# os.chdir(path) #used to charge cwd
#
# os.path.join(path)
# #if individual file and folder names are passed; returns a string with a file path using correct seperators
# #ex)
# print(os.path.join('usr', 'bin', 'spam'))
# #>>> usr/bin/spam

'''########################################################################

Creating new folders w/ os.makedirs(path)'''

#If a directory is not specified; will build in CWD
# os.chdir('/users/tom/desktop')
# os.makedirs('Delicious, wallnut, waffles')

'''########################################################################

Handling Absolute and Relative paths'''

#calling os.path.abspath(path) returns a string of the absolute path
# print(os.path.abspath('.'))

#Calling os.path.isabs; returns True if argument is an absolute path (begins with root folder)
# absolute = os.path.isabs('/users/tom/pycharmprojects/Week_13')
# if absolute == True:
#     print('This is an absolute path')

#Relative paths start with the CWD
# not_absolute = os.path.isabs('./Scripts')
# if not_absolute == False:
#     print('This is an example of relative')

# # Calling os.path.relpath(path, start) will return a string of a relative path
# relpath = os.path.relpath('/users/tom/desktop')
# print(relpath)

# #calling os.path.dirname(path) will return everything before the last /
# dirname = os.path.dirname('/user/tom/desktop')
# print(dirname)
#
# #Calling os.path.basename(path) returns everything after last /
# basename = os.path.basename('/users/tom/desktop')
# print(basename)
#
# #If both are need together as a tuple
# combined = '/users/tom/desktop'
# print(os.path.split(combined))

'''########################################################################

Example of how to find total size of base dir in bytes'''

# #calling os.path.getsize(path) returns size of file in bytes
# print(os.path.getsize('/users/tom/desktop'))
#
# #calling os.listdir(path) returns a list of filename strings
# print(os.listdir('/users/tom/pycharmprojects'))

#Calling both to find the total bytes in a dir
# totalSize = 0
# for filename in os.listdir('/users/tom/pycharmprojects'):
#     totalSize += os.path.getsize(os.path.join('/users/tom/pycharmprojects', filename))
#
# print(totalSize)

'''#######################################################################

Checking Path Validity'''

# os.path.exists()

# os.path.isdir(path)
#
# os.path.isfile(path)

'''######################################################################

Steps to reading or writing files'''

# 1. Call the open() function to return a file object
# 2. Call the read() or write() method on the file object
# 3. Close the files with the close() method on the file object

'''######################################################################

# Opening files with the open() function'''
#
# hellofile = open('/users/tom/hello.txt', 'r')
# hellocontent = hellofile.read()
# print(hellocontent)
#
# #Can also use readlines() method to get a list of string values from the file;
# #one string for each line.
#
# sonnetFile = open('/users/tom/sonnet29.txt')
# print(sonnetFile.readlines())

'''#####################################################################

Writing to Files'''

#The following script writes/appends a new file to the current directory
#files must be closed after every action to be accessed by another function

# #write mode
# baconfile = open('bacon.txt', 'w')
# baconfile.write('Hello world!\n')
#
# #append mode
# baconfile.close()
# baconfile = open('bacon.txt', 'a')
# baconfile.write('Bacon is not a vegetable.')
#
# #Print statement
# baconfile.close()
# baconfile = open('bacon.txt')
# content = baconfile.read()
# baconfile.close()
# print(content)

'''####################################################################

Saving variables with the shelve module'''
# #Import shelve to access the function
# import shelve
#
# #call shelfFile and pass it a file name and store returned value in a variable
# shelfFile = shelve.open('mydata')
# #can make changes like it was a dictionary
# #Create list
# cats = ['Zophie', 'Pooka', 'Simon']
# #stores list in shelfFile
# shelfFile['cats'] = cats
# #Call close
# shelfFile.close()
#
# '''Reopening data from shelf files'''
# #open the shelfFile to make sure that data was saved correctly
# shelfFile = shelve.open('mydata')
# type(shelfFile)
# shelfFile['cats']
# shelfFile.close()
#
# '''Passing list-like returns to lists'''
#
# shelfFile = shelve.open('mydata')
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))
# shelfFile.close()

'''Saving Variables with the pprint.pformat() Function'''
# #import pprint
# import pprint
#
# #Create dictionary
# cats = cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# #Use pformat() to keep list available; converts to string
# print(pprint.pformat(cats))
# print()
# #write string to a file (must be converted to string first)
# fileObj = open('mycats.py', 'w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
# fileObj.close()
#
# #Can now import mycats as a module
# import mycats
# print(mycats.cats)
# print()
# print(mycats.cats[0]['name'])