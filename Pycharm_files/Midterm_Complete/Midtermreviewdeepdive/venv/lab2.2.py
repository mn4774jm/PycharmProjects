#textbook.py using the while loop

'''booksNeeded = int(input('How many textbooks do you have to buy? '))
bookCounter = 1
totalCost = 0.0
while bookCounter <= booksNeeded:    # test the condition
   price = int(input(f'Enter price in whole dollars for book #{bookCounter}: '))
   totalCost = totalCost + price
   bookCounter = bookCounter + 1   # add 1 to the counter, each time thru the loop
print(f'All the books cost ${totalCost :<.2f}.')'''


#For loop example of textbook.py

'''booksNeeded = input('How many textbooks do you have to buy? ')
while booksNeeded.isnumeric() is False or int(booksNeeded) <= 0:
    booksNeeded = input('Please enter a whole number: ')
booksNeeded = int(booksNeeded)

totalCost = 0.0
for book in range(booksNeeded):
    price = int(input(f'Enter price in whole dollars for book #{book+1}: '))
    totalCost += price
print(f'All the books cost ${totalCost :<.2f}')'''


#While true loops and break statement
'''while True:
    print('Welcome to the coffee shop.')
    total = 0.0
    items = int(input('How many items is the customer buying? '))
    for item in range(items):
        price = int(input(f'Enter price in whole dollars for item #{item + 1}: '))
        total = total + price
        print(f'\tRunning subtotal = ${total :<.2f}')
    print(f'\nGrand total = ${total :<.2f}')
    close = input('Time to close? Enter y or n:')
    if close == 'y':
        break
print('Thanks for using the program')'''

#loop-2.py

print('Welcome to our counting program.\n It also adds up the digits as you count')
small = input('Please enter a small number, 0 or higher: ')
while small.isnumeric() is False or int(small) <= 0:
    small = input('Please enter a whole number, 0 or higher: ')
small = int(small)

large = input(f'Please enter a whole number larger than {small}: ')
while large.isnumeric() is False or int(large) <= 0:
    large = input('Please enter a whole number, 0 or higher: ')
large = int(large)

total = 0
for number in range(small, large):
    print(number)
    total += number
print(total)






