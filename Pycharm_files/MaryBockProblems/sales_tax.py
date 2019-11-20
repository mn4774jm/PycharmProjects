'''Thomas Mullins
sales_tax.py
Definition: Calculate the tax rates and final totals for a transaction from user input and provide a receipt
6/6/19'''

def main():
    while True:
        try:

            price = input1()
            state_total, county_total, grand_total = processing1(price)
            output1(price, state_total, county_total, grand_total)

        except Exception as err:
            print(err)

        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('What is the total price of your purchase order? ')
    price = float_regex()
    return price

def float_regex():
    import re
    floatRegex = re.compile(r'(-)?\d+(\.)?(\d+)?')
    regex = input('\tEnter a numeric value: ')
    mo = floatRegex.search(regex)
    while mo == None or float(regex) < 0:
        regex = input('\tEnter only positive numeric values: ')
        mo = floatRegex.search(regex)
    regex = float(regex)
    return regex

def processing1(price):
    state_tax = 0.05
    county_tax = 0.025
    state_total = state_tax*price
    county_total = county_tax*price
    grand_total = price+state_total+county_total
    return state_total, county_total, grand_total

def output1(price, state_total, county_total, grand_total):
    print('\nCustom Delivery Sales Receipt')
    print('{:<10}{:>10}{:>9.2f}'.format('PO Amount:', '$', price))
    print('{:<10}{:>10}{:>9.2f}'.format('State Tax:', '$', state_total))
    print('{:<10}{:>9}{:>9.2f}'.format('County Tax:', '$', county_total))
    print('{:<10}{:>9}{:>9.2f}'.format('Total Cost:', '$', grand_total))


main()
