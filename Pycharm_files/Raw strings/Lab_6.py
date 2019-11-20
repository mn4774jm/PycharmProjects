# #Using raw strings
#
# string = 'Alice\'s cat. It\'s a \ttabby'
# print(string)
#
# string = r'Alice\'s cat. It\'s a \ttabby'      # using r for raw string
#
# print(string)        # raw strings print \ as a character, but it still escapes the ' or "

#############################################################

#Multiline strings using triple quotes
#Usful for making comments in the middle of a line

# print('''
# Dear Alice,
#
# 	Eve's cat has been very naughty.
#
# Happy Catnaps,
# Mo
# ''')

############################################################
# #More things you can do with strings
# phone = 'Android'
# print(phone[5])
# print(phone[3])
# print(phone[1])
#
# #############################################################
#String characters with index numbers shown
#Strings work much like a list
# phone = 'Android '
# length = len(phone)
# print(length)

################################################################

# # Index of the last character is not the same as the length of the string
# phone = 'Android'
# length = len(phone)            # returns 7
# lastLetter = phone[length-1]  # causes index error
# print(lastLetter)
#
# # shorthand to print the last letter in a string variable
# print(phone[len(phone)-1])

###############################################################

#the in operator

# name = input('Enter a name: ')
# if 'e' in name:
# 	print('This name has the letter e.')
# else:
# 	print('No letter e in this name.')

# email = input('Enter your email address: ')
# if '.edu' in email:
# 	print('This is a school email.')
# elif '.com' in email:
#     print('This is a commerce email address')
# elif '.gov' in email:
#     print('This is a government email address')
# else:
#     print('This is not a recognized email address')

###############################################################
#isupper() and islower()

# whisper = 'hello'
# shout = whisper.upper()
# print(shout)
# print(shout.isupper())
#
# shout = 'THIS is me SHOUTING'
# whisper = shout.lower()
# print(whisper)
# print(whisper.islower())

###############################################################

# #.replace()
# spellingMistakes = 'I am going too school too learn programming'
# correct = spellingMistakes.replace('too', 'to')
# print(correct)
# sentence = 'My ca=t pres==ses= the equals= key= when I ty=pe'
# newSentence = sentence.replace('=', '')
# print(newSentence)

##############################################################

#Splitting strings into lists
#
# sentence = 'This is a sentence. It can also become a list.'
#
# allWords = sentence.split('.')
# allWords.pop() #used to remove the last item in a list
# print(allWords)

#################################################################
#working with the list
#after creating list use loop to perform a task for every word in the list

# sentence = input('Please enter a sentence: ')
# allWords = sentence.split()
# print('Here are all the words you typed – capitalized.')
# for index in range(len(allWords)):
# 	print(allWords[index].title())
#
# #Use conditional logic in your loop to control printing of items
#
# for index in range(len(allWords)):
# 	if index < len(allWords)-1:
# 		print(allWords[index].title(), end = ' ')
# 	else:
# 		print(allWords[index].title(), end='.')

####################################################################
########################################################################



