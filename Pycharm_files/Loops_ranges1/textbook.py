
'''
Author: Thomas Mullins
Date:2/14/19
textbook.py
Definition: Complete the textbook.py program by picking the while loop or for loop'''

#Start of loop
while True:
#Variables
    booksNeeded = input('How many textbooks do you have to buy? ')
    bookCounter = 1
    totalCost = 0.0

#Validation
    if booksNeeded.isnumeric():
        booksNeeded = int(booksNeeded) #Assign integer
#Second loop
        while bookCounter <= booksNeeded:
            price = int(input(f'Enter price in whole dollars for book #{bookCounter}: '))
            totalCost = totalCost + price
            bookCounter = bookCounter + 1   # add 1 to the counter, each time thru the loop
        break #Breaks statement after number of books needed reaches zero

    else:print('Enter a whole, positive number, no spaces:')#If non-numeric print
print(f'All the books cost ${totalCost :<.2f}')



# while True:
# booksNeeded = int(input('How many textbooks do you have to buy? '))
# bookCounter = 1
# totalCost = 0.0
# while bookCounter <= booksNeeded:    # test the condition
#    price = int(input(f'Enter price in whole dollars for book #{bookCounter}: '))
#    totalCost = totalCost + price
#    bookCounter = bookCounter + 1   # add 1 to the counter, each time thru the loop
# print(f'All the books cost ${totalCost :<.2f}.')
#
# booksNeeded = int(input('How many textbooks do you have to buy? '))
# totalCost = 0.0
#
# for book in range(booksNeeded):
#     price = int(input(f'Enter price in whole dollars for book #{book+1}: '))
#     totalCost = totalCost + price
# print(f'All the books cost ${totalCost :<.2f}.')
