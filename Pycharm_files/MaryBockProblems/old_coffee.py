'''
Thomas Mullins
coffee_sales_fixed.py
Definition: calculate coffee sales for various products from user input and provide a table as output
9/3/19
'''

def main():
    while True:
        try:

            coffee, coffee_price, tea, tea_price, cappuchino, capp_price = input1()
            coffee_total, tea_total, capp_total, final_total, cups_sold = processing1(coffee, coffee_price, tea, tea_price, cappuchino, capp_price)
            output1(coffee, coffee_price, coffee_total, tea, tea_price, tea_total, cappuchino, capp_price, capp_total, cups_sold, final_total)

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
    print('How many cups of coffee were sold? ')
    coffee = getPosint()
    print("What is the price of coffee?")
    coffee_price = float_regex()
    print('How many cups of tea were sold? ')
    tea = getPosint()
    print("What is the price of tea?")
    tea_price = float_regex()
    print('How many cappuccinos were sold? ')
    cappuchino = getPosint()
    print("What is the price of cappuchino?")
    capp_price = float_regex()
    return coffee, coffee_price, tea, tea_price, cappuchino, capp_price

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
    coffee_total = coffee_price*coffee
    tea_total = tea_price*tea
    capp_total = capp_price*cappuchino
    final_total = coffee_total+tea_total+capp_total
    cups_sold = coffee+tea+cappuchino
    return coffee_total, tea_total, capp_total, final_total, cups_sold

def output1(beverages, bev_totals, prices, each_totals, cup_totals, final_total):
    print('{:<10}{:>15}{:>14}{:>15}'.format('Drink Type', 'Cups sold', 'Price', 'Total'))
    print('{:<10}{:>15}{:>8}{:>6.2f}{:>8}{:>7.2f}'.format('Coffee', coffee, '$', coffee_price, '$', coffee_total))
    print('{:<10}{:>15}{:>8}{:>6.2f}{:>8}{:>7.2f}'.format('Tea', tea, '$', tea_price, '$', tea_total))
    print('{:<10}{:>15}{:>8}{:>6.2f}{:>8}{:>7.2f}'.format('Cappuccino', cappuchino, '$', capp_price, '$', capp_total))
    print('{:<10}{:>15}{:>22}{:>7.2f}'.format('Total', cups_sold, '$', final_total))

main()