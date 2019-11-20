'''Author: Thomqs Mullins
Date:2/17/19
if-1.py
Definition: Write a program that asks the user to enter a number of pennies in a jar (an integer)'''

#Variables
value = input('Enter number of pennies, please: ')
if value.isnumeric() is False:
    print('Please enter whole numeric value. Only whole pennies, good sir or ma\'am.')
else:
    value = int(value)
    dollars = value/100 # assign value for over 100 pennies
    if value == 100:
        print('You have $1')
    elif value <= 100: #Less than 100 does not require further formatting
        print(f'You have precisely $0.{value} in pennies!')

    elif value >= 100:
        print('You have saved exactly $'+format(dollars,'.2f'))

print('Thanks for playing!')

        #print("Gross Pay = $" + str(format(grossPay,'.2f')))