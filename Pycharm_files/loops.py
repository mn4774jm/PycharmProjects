#while loop example

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


#for loop example:

booksNeeded = int(input('How many textbooks do you have to buy? '))
totalCost = 0.0
for book in range(booksNeeded):
    price = int(input(f'Enter price in whole dollars for book #{book+1}: '))
    totalCost = totalCost + price
print(f'All the books cost ${totalCost :<.2f}.')
