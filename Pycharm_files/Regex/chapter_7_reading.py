# #PhoneNumber.py
#
# def is_phone_number(text):
#     #Checks to see if string is 12 characters long
#     if len(text) != 12:
#         return False
#     #Checks if first 3 characters are numbers
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#     #Checks to see if the Checks for hyphen
#     if text[3] != '-':
#         return False
#     #Checks the second group of numbers for numerals
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     #Checks for second hyphen
#     if text[7] != '-':
#         return False
#     #Checks last number block for numerals
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     #If all checks pass, returns true
#     return True
#
# # print('415-555-4242 is a phone number:')
# # print(is_phone_number('415-555-4242'))
# # print('Moshi moshi is a phone number:')
# # print(is_phone_number('Moshi moshi'))
#
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     #Each iteration of the loop checks for 12 characters; starting at 0 and
#     #adding 1 each time until the message is complete
#   chunk = message[i:i+12]
#     #passes chunk to be checked by is_phone_number
#   if is_phone_number(chunk):
#       #Only prints if checks pass
#      print('Phone number found: ' + chunk)
# print('Done')

'''#############################################################################
# # # Matching Regex objects'''
# import re
#
# #regex is compiled
# phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
#
# #.search() looks at string passed for pattern from regex; stored in mo variable
# mo = phoneNumRegex.search('My number is 415-555-4242.')
#
# #mo.group() returns the actual matched object string
# print('Phone number found: ' + mo.group())

'''#############################################################################
#Review of regular expression matching'''

# 1. Import the regex module with import re.
#
# 2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
#
# 3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
#
# 4. Call the Match object’s group() method to return a string of the actual matched text.

'''############################################################################
# #Grouping with parentheses'''
# import re
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# #will print the first group
# print(mo.group(1))
# #prints second group
# print(mo.group(2))
# #prints all groups
# print(mo.group(0))
# print(mo.group())
# print()
# #To retreive all groups at once the plural can be used
# #multiple assignment trick can be used
#
# print(mo.groups())
# area_code, main_number = mo.groups()
# print(area_code)
# print(main_number)

'''###########################################################################
#Matching multiple groups with the pipe'''
# import re
# #Used to match one of two patterns as part of regex
# heroRegex = re.compile (r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey.')
# print(mo1.group())
# #Will return batman
#
# mo2 = heroRegex.search('Tina Fey and Batman.')
# print(mo2.group())
#
# #findall method can be called on a regex with no groups to return a list of string matches
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
#
# #Pipe can be used to match one of several patterns as part of your regex
#
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# #Will return full matched text
# print(mo.group())
# #Will only return the matched text inside parentheses
# print(mo.group(1))

'''############################################################################
#optional matching with the question mark'''

# import re
#
# #Using parentheses allows for optional pattern matching
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
#
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())
#
# #Can be used the same way for the phone number example:
# #Will return the full number
# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search('My number is 415-555-4242')
# print(mo1.group())
# print()
#
# #Will return only the main number
# mo2 = phoneRegex.search('My number is 555-4242')
# print(mo2.group())
# print()

'''##########################################################################
# # Matching zero or more with the star'''
# import re
# #Matched zero times
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
# print()
#
# #Matched once
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())
# print()
#
# #Matched many
# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo3.group())

'''########################################################################
#Greedy and nongreedy matching'''

# import re
# #Matches longest string possible by default
# greedyHaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyHaRegex.search('HaHaHaHaHa')
# print(mo1.group())
# print()
#
# #matches shortest string possible when curlys are followed by ?
# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
# print(mo2.group())
# print()

'''#######################################################################
#Character classes'''
# import re
#
# #Requires at least 1 number, a space character, and at least one "Word"
# xmasRegex = re.compile(r'\d+\s\w+')
# print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
# print()
#
# #Making your own character classes
# #Brackets can be used to create a new character class
#
# #This example finds all the vowels
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))
# print()
#
# #Ranges can also be included using a hyphen
# #using a ^ will make a negative character class; matches to everything not in brackets
# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))
# print()

'''######################################################################
#Matching everything with Dot-Star'''

# import re
#
# #pulls information that follows 'First name:' and 'Last name:' Greedy version
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))
# print()

'''######################################################################
#Matching newlines with the dot character'''

#Case sensitive matching
#To ignore case sensitive matching use the re.IGNORECASE or re.I

# import re
# robocop = re.compile(r'robocop', re.I)
# print(robocop.search('Robocop is part man, part machine, all cop.').group())
# print()
#
# print(robocop.search('ROBOCOP protects the innocent.').group())
# print()
#
# print(robocop.search('Al, why does your programming book talk about robocop so much?').group())
# print()

'''#######################################################################
#Substituting strings with the sub() method'''

# import re
# #The first string passed replaces any matches, the second is the regular expression
# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
# print()
#
# #Can be used to sub for the matched text using \1 before the sub
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

'''#######################################################################
#Managing complex regexes
#re.compile() can be told to ignore whitespace and comments making it easier to read'''
# import re
# #EX
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?            # area code
#     (\s|-|\.)?                    # separator
#     \d{3}                         # first 3 digits
#     (\s|-|\.)                     # separator
#     \d{4}                         # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#     )''', re.VERBOSE)
# mo = phoneRegex.search('my phone number is 952-649-0213')
# print(mo.group())

'''#########################################################################
Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
Can all be used at once but only with a pipe character'''

# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)