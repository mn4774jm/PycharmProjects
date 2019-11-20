'''#area.py

measure = input('What is your measurement unit (in., ft., cm. etc).? ')
length = float(input(f'What is the length of the rectangle in {measure}? '))
width = float(input(f'What is the width of the rectangle in {measure}? '))
total = length*width
print(f'Your rectangle is {total} square {measure}.')'''

'''#salestax.py

price = float(input('What is the total price of your purchase order? '))
state = (0.05*price)
county = (0.025*price)
total = (state+county+price)
print('\nCustom Delivery Sales Receipt:')
print('{:<20}{:>3}{:7.2f}'.format('PO Amount:','$',price))
print('{:<20}{:>3}{:7.2f}'.format('State Tax:','$',state))
print('{:<20}{:>3}{:7.2f}'.format('County Tax:','$',county))
print('{:<20}{:>3}{:7.2f}'.format('Total Cost:','$',total))'''

#Math-1.py

import math
