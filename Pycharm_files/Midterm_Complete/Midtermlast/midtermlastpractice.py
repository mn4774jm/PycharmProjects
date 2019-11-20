# #Basics
#
# print('Welcome to Bob\'s Diner!')
#
# meal = input('Enter the price of your meal: ')
# meal = float(meal)
# tip_percent = input('Enter tip percent -> .15, .20, etc.: ')
# tip_percent = float(tip_percent)
#
# tip_value = (meal*tip_percent)
# tax = (meal * 0.075)
# total = tip_value + tax + meal
#
# print('{:<15}{:^1}{:>7.2f}'.format('Meal price','$', meal))
# print('{:<15}{:^1}{:>7.2f}'.format(f'Tip @ {tip_percent*100}%','$', tip_value))
# print('{:<15}{:^1}{:>7.2f}'.format('Tax @ 7.5%','$', tax))
# print('{:<15}{:^1}{:>7.2f}'.format('Total due','$', total))
# print('\nThanks for using the program')

#Conditional logic

# print('Welcome to ABC Widget!')
# def main():
#     while True:
#         try:
#
#             widget_number = input1()
#             discount, total_before, discount_total, final_price = processing1(widget_number)
#             output1(widget_number, discount, total_before, discount_total, final_price)
#         except Exception as err:
#             print(err)
#         answer = input('\nWould you like to run this program again? Enter Y or N: ')
#         while answer.upper() != 'Y' and answer.upper() != 'N':
#             answer = input('Please enter Y or N: ')
#         if answer.upper() == 'N':
#             print(f'\nThank for using the program')
#             break
#
#
# def input1():
#     widget_number = 0
#     print('How many widgets would you like to buy?')
#     widget_number = getPosint()
#     return widget_number
#
#
# def getPosint():  # ensures "int-able" input over 0
#     posInt = input('\tEnter a positive whole number: ')
#     while posInt.isnumeric() is False or posInt == '0':
#         posInt = input('\tPlease enter a whole number, greater than 0: ')
#     posInt = int(posInt)
#     return posInt
#
# def processing1(widget_number):
#     discount = 0
#     total_before = 0
#     total_before = widget_number*99
#     if widget_number < 10:
#         discount = 0
#     elif widget_number >= 10 and widget_number < 20:
#         discount = 0.1
#     elif widget_number >= 20 and widget_number < 50:
#         discount = 0.2
#     elif widget_number >= 50 and widget_number < 100:
#         discount = 0.3
#     elif widget_number >= 100:
#         discount = .4
#     discount_total = total_before * discount
#     final_price = total_before - discount_total
#     return discount, total_before, discount_total, final_price
#
# def output1(widget_number, discount, total_before, discount_total, final_price):
#     print(f'\nYou are buying {widget_number} widgets, earning a {discount*100}% discount')
#     print('{:<15}{:>5}{:>8.2f}'.format('Retail price at $99 ea.:', '$', total_before))
#     print('{:<15}{:>6}{:>8.2f}'.format('Amount you saved today:', '$', discount_total))
#     print('{:<15}{:>7}{:>8.2f}'.format('Discount price b4 tax:', '$', final_price))
#
# main()


#Functions, loops and lists



def main():
    while True:
        try:
            print('\nWelcome to the personal budget program!')
            needs_list, costs_list, total = input1()
            output1(needs_list, costs_list, total)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    needs_list = ['Rent','Food', 'Trnasport', 'Other']
    costs_list = []
    total = 0
    for index in range(len(needs_list)):
        print(f'How much did you spend on {needs_list[index]}')
        cost_counter = getPosint()
        costs_list.append(cost_counter)
        total += cost_counter
    return needs_list, costs_list, total

def getPosint(): # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == '0':
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

def output1(needs_list, costs_list, total):

    print('Here\'s your overall budget:')
    for index in range(len(needs_list)):
        print('{:15}'.format(needs_list[index]), end= '')
    print()
    for index in range(len(costs_list)):
        print('${:<14,.2f}'.format(costs_list[index]), end= '')
    print()
    print(f'\nYour total monthly budget is ${total:.2f}')

main()
