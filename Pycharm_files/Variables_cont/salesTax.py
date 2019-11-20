'''Author: Thomas Mullins
Date:2/3/19
salesTax.py
Definition: Write a program that askes the user to enter the price of a purchase order.'''

#Variables
purchase=float(input('What is th total price of your purchase order?'))
stateTax=purchase*0.05
countyTax=purchase*0.025
tltCost=purchase+stateTax+countyTax
#Header
print('\nCustom Delivery Sales Receipt\n')
#Script
print(f'PO Amount: \t\t${purchase:>10.2f}')
print(f'State Tax: \t\t${stateTax:>10.2f}')
print(f'County Tax:\t\t${countyTax:>10.2f}')
print(f'Total Cost:\t\t${tltCost:>10.2f}')