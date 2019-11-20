'''Author: Thomas Mullins
Date:1/31/19
gasCalc.py
Definfition: Create a program that invilves user input to calculate cost of trip'''
#Define variables
miles=int(input('How many miles did you drive?'))
gas=int(input('How many gallons of gas did you use?'))
price=float(input('What is the price of gas?'))
totalCost=gas*price

#Print scrpit formatting
print(f'Distance traveled:\t  {miles:>13.2f}')
print(f'Gallons of gas used:\t {gas:>10.2f}')
print(f'Cost of Gas:\t\t\t\t ${price:>0.2f}')
print(f'Total cost of trip:\t\t = ${totalCost:>0.2f}')