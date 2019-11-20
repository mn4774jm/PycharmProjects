'''
Thomas Mullins
coffee_sales_fixed.py
Definition: calculate coffee sales for various products from user input and provide a table as output
*** rewritten to include loops and lists
9/18/19
'''

def main():
    while True:
        try:
            beverages, bev_totals, prices = input1()
            each_totals, final_total, cup_totals = processing1(bev_totals, prices)
            output1(beverages, bev_totals, prices, each_totals, cup_totals, final_total)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ').upper()
        while answer != 'Y' and answer != 'N':
            answer = input('Please enter Y or N: ').upper()
        if answer == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Welcome to the coffee sales program\n')

    beverages = ['coffee', 'tea', 'cappuchino']
    bev_totals = []
    prices = []
    for i in range(len(beverages)):
        print(f'How many cups of {beverages[i]} were sold?')
        drink = getPosint()
        bev_totals.append(drink)
        print(f'How much is each {beverages[i]}?')
        amount = float_regex()
        prices.append(amount)
    return beverages, bev_totals, prices

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0:
        posInt = input('\tPlease enter a whole number, zero or greater: ')
    posInt = int(posInt)
    return posInt

def float_regex():
    import re
    floatRegex = re.compile(r'^[+|-]?\d+[.]?(\d+)?$')
    regex = input('\tEnter a numeric value: ')
    mo = floatRegex.search(regex)
    while mo == None:
        regex = input('\tEnter only numeric values: ')
        mo = floatRegex.search(regex)
    regex = float(regex)
        #regex = round(regex) Not useful in this instance
    return regex

def processing1(bev_totals, prices):
    each_totals = []
    final_total = 0
    cup_totals = 0
    for i in range(len(bev_totals)):
        totals = bev_totals[i]*prices[i]
        final_total += totals
        cup_totals += bev_totals[i]
        each_totals.append(totals)
    return each_totals, final_total, cup_totals

def output1(beverages, bev_totals, prices, each_totals, cup_totals, final_total):
    print('\nDrink Sales for Reporting Period')
    print('{:<10}{:>15}{:>14}{:>15}'.format('Drink Type', 'Cups sold', 'Price', 'Total'))
    for i in range(len(beverages)):
        print('{:<10}{:>15}{:>8}{:>6.2f}{:>8}{:>7.2f}'.format(beverages[i], bev_totals[i], '$', prices[i], '$', each_totals[i]))
    print('{:<10}{:>15}{:>22}{:>7.2f}'.format('Total', cup_totals, '$', final_total))

main()

