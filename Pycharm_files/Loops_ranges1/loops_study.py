'''#Adding up the price of all text books loop'''

# #First variable
# booksNeeded = int(input('Please enter the number of books needed: '))
# #Counter created
# bookCounter = 1
# #Cost counter created
# totalCost = 0.0
# #While loop begin
# while bookCounter <= booksNeeded:
#     #Second variable for book cost
#     price = int(input('Enter book cost: '))
#     #Total cost added for each loop
#     totalCost += price
#     # 1 book added for each loop
#     bookCounter += 1
# #Print for total cost of X books
# print(f'All books cost ${totalCost: <.2f}.')

'''While loops and nested loops'''

# #Used when you don't know how many times a loop will run
# while True: #While loop again
#     print('Welcome to the coffee shop.')
#     #Total initialized
#     total = 0.0
#     #Ask user for number of items
#     items = int(input('How many items is the customer buying? '))
#     #For loop for items in range
#     for item in range(items):
#         #Item +1 is used for displaying 1 instead of zero
#         price = int(input(f'ENter the price of item #{item+1}: '))
#         #Total accumulator
#         total += price
#         print(f'Running subtotal = ${total: <.2f}')
#     print(f'Grand total = ${total :<.2f}')
#     close = input('Time to close? Enter y or n:')
#     if close == 'y':
#         break
#     print('Thanks for using the program')

'''Basic use of range'''

# print('I can add up all the numbers between 50 and 100')
# total = 0
# #Establist starting and ending points
# for numbers in range(50, 100):
#     #print each number represented by loop
#     print(numbers)
#     #Accumulate
#     total += numbers
# #Print total
# print(f'The total of all the numbers is {total:d}')

'''Textbook practice program'''

# import re
#
# total = 0.0
# totalCost = 0.0
# bookRegex = re.compile(r'\d+')
# bookNeeded = input('How many books do you need to buy? ')
# mo = bookRegex.search(bookNeeded)
# while mo == None:
#     bookNeeded = input('Please enter only numerical values: ')
#
# bookNeeded = int(bookNeeded)
# for books in range(bookNeeded):
#
#     price = input(f'How much is book #{books+1}? ')
#     mo = bookRegex.search(price)
#     while mo == None:
#         price = input('Please enter only numerical values: ')
#         price = int(price)
#     total = int(total)
#     price = int(price)
#     total = price
#     totalCost = int(totalCost)
#     totalCost = totalCost + total
# print(f'All books cost ${totalCost:<.2f}')

'''Range practice'''

# # for numbers in range(0,6):
# #     print(numbers)
# total = 0
# for numbers in range(1,21):
#     print(numbers)
#     total += numbers
# print(total)


'''Loops practice'''

# total = 0
# totalAll = 0
# small = input('Enter a small number: ')
# large = input(f'Enter a number larger than {small}')
#
#
# if small.isnumeric() and large.isnumeric():
#     small = int(small)
#     large = int(large)
#     if small < large:
#         for items in range(small, large+1):
#             print(items)
#             total += items
#         totalAll += total
#     print(f'The total numbers you counted is {totalAll}.')

'''Average quiz'''
# import re
#
# regex = re.compile(r'\d+')
# studentNumber = input('How many students are taking the exam? ')
# mo = regex.search(studentNumber)
# while mo == None:
#     studentNumber = input('How many students are taking the exam? ')
#     mo = regex.search(studentNumber)
# studentNumber = int(studentNumber)
# quizNumber = input('How many quizzes will be taken? ')
# mo = regex.search(quizNumber)
# while mo == None:
#     quizNumber = input('How many quizzes will be taken? ')
#     mo = regex.search(quizNumber)
# quizNumber = int(quizNumber)
# for students in range(studentNumber):
#     total = 0
#     total = int(total)
#     print(f'Quiz info for student #{students+1}.')
#     for quiz in range(quizNumber):
#         score = input(f'\tEnter score for quiz #{quiz+1}: ')
#         score = int(score)
#         total += score
#         average = total/quizNumber
#     print(f'Total point for student #{students+1} is: {total:.2f}.')
#     print(f'Student #{students+1}\'s quiz average is {average:.2f}.')
# print('Thanks for using the program.')

'''Average Rainfall'''

import re
months = 12
total = 0
regex = re.compile(r'\d+')
years = input('How many years are in your rainfall sample? ')
mo = regex.search(years)
while mo == None:
    years = input('Enter only whole numbers: ')
    mo = regex.search(years)
years = int(years)
for avgRain in range(years):
    total = 0.0
    print(f'Rainfall data for year #{avgRain+1}:')
    for fall in range(months):
        regex = re.compile(r'\d+(.)?(\d{2})?')
        rain = input(f'\tTotal rainfall for month #{fall+1}: ')
        mo = regex.search(rain)
        while mo == None:
            rain = float(input(f'\tTotal rainfall for month #{fall + 1}: '))
            mo = regex.search(rain)
        rain = float(rain)
        total += rain
        total = float(total)
        avg = 0
        avg = float(avg)
        avg = total/12
    print(f'Total rainfall for year {avgRain+1} is {total:.2f} inches.')
    print(f'The average rainfall was {avg:.2f} inches per month.')

