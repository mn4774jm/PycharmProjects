'''booksNeeded = int(input('How many textbooks do you have to buy? '))
bookCounter = 1
totalCost = 0.0
while bookCounter <= booksNeeded:    # test the condition
   price = int(input(f'Enter price in whole dollars for book #{bookCounter}: '))
   totalCost = totalCost + price
   bookCounter = bookCounter + 1   # add 1 to the counter, each time thru the loop
print(f'All the books cost ${totalCost :<.2f}.')


while True:
    print('Welcome to the coffee shop.')
    total = 0.0
    items = int(input('How many items is the customer buying? '))
    for item in range(items):
        price = int(input(f'Enter price in whole dollars for item #{item + 1}: '))
        total = total + price
        print(f'Running subtotal = ${total :<.2f}')
    print(f'Grand total = ${total :<.2f}')
    close = input('Time to close? Enter y or n:')
    if close == 'y':
        break
print('Thanks for using the program')


questions = int(input('How many questions did you ask Grumpy Cat? '))
print('This program thinks that Grumpy Cat answered as follows: ')
for question in range(questions):
    print('NO.')


print('Counting Program')
for number in range(10):
    print(number)


print('I can add up all the numbers between 50 and 100.')
total = 0
for number in range(50, 101):
    print(number)
    total = total + number
print(f'The total of all the numbers is: {total:,d}.')'''


myCollege = 'Minneapolis'
for letter in myCollege:
    print(letter)
print('Acronym = ' + myCollege[0] + 'C')

