'''Author: Thomas Mullins
Definition: Write a program that calculates and displays cost information for a flight special to Florida.
Date: 3/21/19
midterm1.py
 '''
#Header print statement
print('Welcome to the trip calculator!')

#assigning variables from user data
num_people = input('How many people are flying? ')
num_people = int(num_people) #assigning number of tickets as an integer
num_bag = input('How many bags do you need to check? ')
num_bag = int(num_bag)#assigning number of bags checked as an integer

#Calculations for ticket price and fees
ticket_price = (num_people * 250)
ticket_fee = (num_people * 20)
bag_price = (num_bag * 25)
total = (ticket_price + ticket_fee + bag_price)

#Print statements and formatting using tuples method
print('\nThanks for using the travel calculator!')
print('{:<20}{:>6}{:>9.2f}'.format(f'{num_people} Tickets @ $250 each:', '$', ticket_price)) #toal price for tickets
print('{:<20}{:>5}{:>9.2f}'.format(f'{num_bag} suitcases @ $25 each:', '$', bag_price))#total price for bags checked
print('{:<20}{:>6}{:>9.2f}'.format('Fees @ $20 per ticket:', '$', ticket_fee))#Total price for fees
print('{:<20}{:>4}{:>9.2f}'.format('Total due for your trip:', '$', total))#Overall total of all values
