# # Birthdays.py
#
# birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}
#
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name =='':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of '+ name)
#     else:
#         print('I do not have birthday information for '+name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

############################################

#using Data types in loops; .values(), .keys(), .items()

# spam = {'color': 'red', 'age': 42}
# #dict_keys
# # for k in spam.keys():
# #     print(k)
#
# #dict_values
# # for v in spam.values():
# #     print(v)
#
# #dict_items
# for i in spam.items():
#     print(i)

#############################################

# #multiple assignment trick
# spam = {'color': 'red', 'age': 42}
# for k, v in spam.items():
#     print('Key: ' + k + 'Value: ' + str(v))

#############################################

# #The get method; .get()
# #Because the value of cups in the dictionary is 2 it will be cups will print 2
# picnicItems = {'apples': 5, 'cups': 2}
# cups = 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
# print(cups)
#
# #because there is no key called eggs in the dictionary 0 will be printed
# eggs = 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
# print(eggs)

#############################################

#The setdefault() method
#used for setting value for a dictionary key whos value does not already exist
# spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'
# print(spam)
# print(spam.keys())

#############################################

# #characterCount.py / prettyPrinting.py
# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen'
# count = {}
#
# for character in message:
#     count.setdefault(character,0)
#     count[character] = count[character] +1
#
# print(pprint.pformat(count))

#############################################

#ticTacToe.py

# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for '+turn+'. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'
#
# printBoard(theBoard)

##############################################

#totalBought example; nested dictionary

# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#             'Bob': {'ham sandwiches': 3, 'apples': 2},
#             'Carol': {'cups': 3, 'apple pies': 1}}
#
# #Inside the loop, the string of the guest's names is assigned to k,
# #and the dictionary of picnic items is assigned to v.
# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         # if item is not present its value will default to 0
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought
#
# print('Number of things being brought:')
# print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
# print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))


