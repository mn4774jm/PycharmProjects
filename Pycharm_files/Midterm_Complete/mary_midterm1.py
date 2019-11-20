'''
definition: This program calculates the total cost of a catered meal, and creates an invoice with meal price, tax,
subtotal, tip & grand total.
'''

print('Welcome to K\'s Katering!')
#Define main to call functions
def main():
    while True:#Loops so if handling triggered it returns to the beginning of main
        try:#Exception handling
            price, tip = input1()
            price, tax_total, subtotal, tip, tip_total, grand_total = processing1(price, tip)
            output1(price, tax_total, subtotal, tip, tip_total, grand_total)
        except Exception as err:
            print(err)
        #Repeat option
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break
#Collect user input data, validate for numbers, assign type
def input1():
    price = input('\nEnter the price of your meal: ')
    while price.isnumeric() is False:
        price = input('Please enter only numeric values: ')
    price = float(price)
    tip = input('Enter the tip % you want to apply: ')
    while tip.isnumeric() is False:
        tip = input('Please enter only numeric values: ')
    tip = float(tip)
    return price, tip
#All the Maths
def processing1(price, tip):
    tip_real = tip*0.01
    tip_total = tip_real*price
    tax_total = price*0.08025
    subtotal = price + tax_total
    grand_total = tip_total + subtotal
    return price, tax_total, subtotal, tip, tip_total, grand_total
#Display user tabulations
def output1(price, tax_total, subtotal, tip, tip_total, grand_total):
    print('\n\nInvoice Due')
    print('{:<25}{:>5}{:>8.2f}'.format('Meal Price', '$', price))
    print('{:<25}{:>5}{:>8.2f}'.format('  tax @ 8.025%', '$', tax_total))
    print('{:<25}{:>5}{:>8.2f}'.format('Subtotal', '$', subtotal))
    print('{:<25}{:>5}{:>8.2f}'.format(f'  Tip at {tip:0.0f}%', '$', tip_total))
    print('{:<25}{:>5}{:>8.2f}'.format('Total', '$', grand_total))
    print('\nThanks for Kalling K!')

main()