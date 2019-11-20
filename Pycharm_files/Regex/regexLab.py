'''
Author: Thomas Mullins
Definition: your program file should include all the examples from the previous
slides. Check that they all work, without crashing. Add comments to explain the significance of each block/ what it
does.
regexLab.py
'''

import re
#Sets the pattern and searches for matching patterns
# phoneRegex = re.compile(r'.\d{3}.\d{3}.\d{4}')
# myMessage = phoneRegex.search('You can call me at 612 234 5678')
# orMessage = phoneRegex.search('or you can call me at (651)445-0987')
# print('Phone Numbers: ' + myMessage.group())
# print('Phone Numbers: ' + orMessage.group())


#Similar to abave but lists all patterns found as opposed to just one
# #.findall
# phoneRegex = re.compile(r'.\d{3}.\d{3}.\d{4}')
# myList = (phoneRegex.findall('You can call me at 612 234 5678 or at (651)345-0987'))
# print('Here is my phone number list: ', myList)


#Creates a variable, asks the user to enter a part of the name, and matches all or part of the name. If none prints none
# nameString = 'Albert Einstein'
# searchString = input('Enter search string: ')
# print(nameString)
#
# T_F = re.match('.*'+searchString, nameString)
# print('T-F=: ', T_F)#T_F is a boolean variable
# if T_F:
#     print(T_F.group())#interpret the results returned for True
# else:
#     print(searchString, 'not found')


#Creates groups in pattern and prints either individual groups or a list
# phoneRegex = re.compile(r'.(\d{3})-(\d{3}-\d{4})')
# myMessage = phoneRegex.search('You can call me at 612-234-5678')
# print('You can call me at 612-234-5678')
# print('Pattern: .(\d\d\d)-(\d\d\d-\d\d\d\d)')
# print('group 1: ', myMessage.group(1))
# print('group 2: ', myMessage.group(2))
# print('group  : ', myMessage.group())
# print('group 0: ', myMessage.group(0))
# print('groups : ', myMessage.groups())  # what data type is returned?
# print()

#Uses the pipe in the pattern to look for Batman OR robin; returns the first found; or both with .findall()
##Using the pipe as or between multiple options
# heroRegex = re.compile(r'Batman|Robin')
# myHero1 = heroRegex.search('Batman and Robin')
# print(myHero1.group())
# myHero2 = heroRegex.search('Robin and Batman')
# print(myHero2.group())
# print(heroRegex.findall('Robin and Batman'))

#Using the ? allows you to make pattern peices optioanl
# #Using ? for optional input
# phoneRegex = re.compile(r'.(\d{3})?-?(\d{3}-\d{4})')
# print('Pattern: .(\d{3})?-?(\d{3}-\d{4})')
# myMessage1 = phoneRegex.search('You can call me at 612-234-5678')
# print('Text of msg 1: You can call me at 612-234-5678')
# print(myMessage1.group())
# myMessage2 = phoneRegex.search('You can call me at 234-5678')
# print('Text of msg 2: You can call me at 234-5678')
# print(myMessage2.group())

#Using the * alows the pattern to include zero or more occurances of the group the preceeds it
# #Matching zero or more occurances w/ *
# batRegex = re.compile(r'Bat(wo)*man')
# myBat1 = batRegex.search('Where does Batman live')
# print('Batman:', myBat1.group())
# myBat2 = batRegex.search('Where does Batwoman live')
# print('Batwoman:', myBat2.group())
# myBat3 = batRegex.search('Where does Batwowowowoman live')
# print('Batwowowowowoman:', myBat3.group())

#using + will only search the pattern if it is present one or more times
# #Mat one or more occurances with +
# batRegex = re.compile(r'Bat(wo)+man')
# myBat2 = batRegex.search('Where does Batwoman live')
# print('Batwoman:', myBat2.group())
# myBat3 = batRegex.search('Where does Batwowowoman live')
# print('Batwowowoman:', myBat3.group())
# myBat1 = batRegex.search('Where does Batman live')
# print('Batman:', myBat1)

#Compile pattern
# fullNameRegex = re.compile(r'\D{1,}\s\D{1,}\s\D{1,}', re.I)
# #Ask for user input and assign variable
# fullName = input('Enter your full name; First, Middle, and Last: ')
# #.title() to capitalize
# fullName = fullName.title()
# #Use patternMatch variable for validation
# patternMatch = fullNameRegex.search(fullName)
# #Loop to check if fullName contains a None value
# while patternMatch == None:
#     #If none found ask for input again
#     fullName = input('Please enter a first, last, and middle name: ')
#     fullName = fullName.title()
#     patternMatch = fullNameRegex.search(fullName)
# else:
#     #If string passes the check, print
#     print('Your full name is '+fullName)

# stuff = input('Type in a sentence with 3 spaces at the beginning and at the end')
# print('1'+stuff+'!')
# print('2'+stuff.strip()+'!')
# print('3'+stuff.rstrip()+'!')
# print('4'+stuff.lstrip()+'!')

name_source = input('Enter full name – First Middle Last: ').strip()
name_regex = re.compile(r'^([a-zA-Z]+-*\'*[.]*)+( [a-zA-Z]+-*\'*[.]*)+$')  # full name pattern.
found_name = name_regex.search(name_source)  # source to search in
print(found_name)

