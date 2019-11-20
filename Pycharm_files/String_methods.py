####picnicTable.py########

#Program uses justified text and fill characters to create a neatly organized table

# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
#
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

####################################################################

#Join() and split() method examples
#used to join together litems in a list into a single value

# join_ex1 = ', '.join(['cats', 'rats', 'bats'])
# print(join_ex1)
# #
# join_ex2 = ' '.join(['My', 'name', 'is', 'Simon'])
# print(join_ex2)
#
# join_ex3 = 'ABC'.join(['My', 'name', 'is', 'Simon'])
# print(join_ex3)
#
###################################################################

#Used to break up single values into list forms
split_ex1 = 'My name is Simon'.split()
print(split_ex1)

#can use a delimenator to choose where split occurs
split_ex2 = 'MyABCnameABCisABCSimon'.split('ABC')
print(split_ex2)

#####################################################################

#using strip(), lstrip(), and rstrip() methods to remove whitespace

# spam = '    Hello World     '
# strip_ex1 = spam.strip()
# print(strip_ex1)

# strip_ex2 = spam.lstrip()
# print(strip_ex2)
#
# strip_ex3 = spam.rstrip()
# print(strip_ex3)

#Can be used to eliminate specific parts of strings

# spam = 'SpamSpamBaconSpamEggsSpamSpam'
# strip_ex4 = spam.strip('ampS')
# print(strip_ex4)
#
# #####################################################################
# #Additional string methods;
#
# .upper() - converts and return all uppercase letters
#
# .lower() - converts and returns all lowercase letters
#######################################################################
# .isupper() and .islower() - used to check if a string variable is all uppercase or all lowercase
#
# whisper = 'hello'
# shout = whisper.upper()
# print(shout)
# print(shout.isupper())
#
# shout = 'THIS is me SHOUTING'
# whisper = shout.lower()
# print(whisper)
# print(whisper.islower())

#########################################################################
# #isX string methods; used for validation
# isalpha() - True if only letters
# isalnum() - True if only letters and numbers
# isdecimal(), isnumeric(), isdigit() - True if only numeric, 0-9 only
# isspace() - True if only spaces, tabs, and new lines
# istitle() - True if all words start with a capital letter

#####################################################################

#Startswith() / endswith() methods
#used to check if the begginning or end of a string end with a specific value

# spam = 'Hello world!'
# print(spam.startswith('Hello'))
#
# print(spam.endswith('world!'))

#######################################################################
# .replace()
# spellingMistakes = 'I am going too school too learn programming'
# correct = spellingMistakes.replace('too', 'to')
# print(correct)
# sentence = 'My ca=t pres==ses= the equals= key= when I ty=pe'
# newSentence = sentence.replace('=', '')
# print(newSentence)

