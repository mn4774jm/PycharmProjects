'''midterms1'''

# print('Welcome to Bob\'s diner!')
# meal_price = input('Please enter the price of your meal: ')
# meal_price = float(meal_price)
# tip_percent = input('Enter tip percent -> .15, .20, etc.: ')
# tip_percent = float(tip_percent)
# tip_print = tip_percent*100
# tip_value = tip_percent*meal_price
# tax = meal_price*.075
# total = meal_price+tax+tip_value
#
# print('Meal Price:''{:>10}{:>7.2f}'.format('$',meal_price))
# print(f'Tip @ {tip_print}:''{:>10}{:>7.2f}'.format('$',tip_value))
# print(f'Tax @ 7.5%:''{:>10}{:>7.2f}'.format('$',tax))
# print('Total Due: ''{:>10}{:>7.2f}'.format('$',total))
# print('\nThanks for dining at Bob\'s!')

'''midterm2'''
# import re
#
#
# def main():
#     while True:
#         try:
#             num_widget = input1()
#             num_widget, discount, cost, amount_saved, total = processing1(num_widget)
#             output1(num_widget, discount, cost, amount_saved, total)
#         except Exception as err:
#             print(err)
#         answer = input('Would you like to run this program again? Enter Y or N: ')
#         while answer.upper() != 'Y' and answer.upper() != 'N':
#             answer = input('Please enter Y or N: ')
#         if answer.upper() == 'N':
#             print(f'\nThank for using the program')
#             break
#
# def input1():
#     userRegex = re.compile(r'\d+')
#     print('\nWelcome to ABC widget!\nHow many widgets do you want to buy?')
#     num_widget = input('\tEnter a whole positive number: ')
#     mo = userRegex.search(num_widget)
#     num_widget = int(num_widget)
#     while mo == None or num_widget <= 0:
#         num_widget = input('\tEnter a whole number, greater then 0:')
#         mo = userRegex.search(num_widget)
#         num_widget = int(num_widget)
#     return num_widget
#
# def processing1(num_widget):
#     discount = 0
#     if num_widget < 10:
#         discount = 0
#     elif num_widget >= 10 and num_widget <= 19:
#         discount = 0.1
#     elif num_widget >= 20 and num_widget <= 49:
#         discount = 0.2
#     elif num_widget >= 50 and num_widget <= 99:
#         discount = 0.3
#     elif num_widget >= 100:
#         discount = 0.3
#
#     cost = num_widget*99
#     amount_saved = cost*discount
#     total = cost - amount_saved
#     return num_widget, discount, cost, amount_saved, total
#
# def output1(num_widget, discount, cost, amount_saved, total):
#     print(f'\nYou are buying {num_widget} widgets, earning a {discount*100}% discount!')
#     print('Retail Prive @ $99 ea.: ''{:5}{:>2.2f}'.format('$', cost))
#     print('Amount you saved today: ''{:5}{:>2.2f}'.format('$', amount_saved))
#     print('Discount price b4 tax:  ''{:5}{:>2.2f}'.format('$', total))
#
#
# main()

'''midterm 3'''

# def main():
#     needs, costs, total = input1()
#     output1(needs, costs, total)
#
# def input1():
#     needs = ['Rent', 'Food', 'Transport', 'Other']
#     costs = []
#     total = 0
#     print('\nWelcome to the personal budget program!')
#     for index in range(len(needs)):
#         print(f'How much did you spend on {needs[index]}?')
#         cost_counter = getPosint()
#         costs.append(cost_counter)
#         total += cost_counter
#     return needs, costs, total
#
# def output1(needs, costs, total):
#     print('\nHere is your overall budget:')
#     for index in range(len(needs)):
#         print('{:15}'.format(needs[index]), end='')
#     print()
#     for index in range(len(costs)):
#         print('${:<14,.2f}'.format(costs[index]), end= '')
#     print()
#     print(f'Your total monthly budget is ${total}.')
#
# def getPosint(): # ensures "int-able" input over 0
#     posInt = input('\tEnter a positive whole number: ')
#     while posInt.isnumeric() is False or posInt == '0':
#         posInt = input('\tPlease enter a whole number, greater than 0: ')
#     posInt = int(posInt)
#     return posInt
#
# main()

'''Dictionaries'''

