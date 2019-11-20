'''
Thomas Mullins
gas_calc.py
Definition: Program that calculates MPG and cost of fuel from user input
6/6/19
'''

def main():
    while True:
        try:

            miles, gas_used, price = input1()
            MPG, cost=processing1(miles, gas_used, price)
            output1(MPG, cost)

        except Exception as err:
            print(err)

        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Welcome to the Gas Calculator Program\n')
    print('How many miles did you drive? ')
    miles = float_regex()
    print('How many gallons of gas did you use? ')
    gas_used = float_regex()
    print('What is the current price of gas per gallon? ')
    price = float_regex()
    return miles, gas_used, price

def float_regex():
    import re
    floatRegex = re.compile(r'(-)?\d+(\.)?(\d+)?')
    regex = input('\tEnter a numeric value: ')
    mo = floatRegex.search(regex)
    while mo == None or float(regex) < 0:
        regex = input('\tEnter only numeric values: ')
        mo = floatRegex.search(regex)
    regex = float(regex)
    return regex

def processing1(miles, gas_used, price):
    MPG = miles/gas_used
    cost = gas_used*price
    return MPG, cost

def output1(MPG, cost):
    print('\nHere are some fun facts about your trip!')
    print('{:<10}{:>15.2f}'.format('MPG', MPG))
    print('{:<10}{:>10}{:>3.2f}'.format('Trip cost', '$', cost))

main()