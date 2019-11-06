#midtermpractice1

# print(f'Welcome to Bob\'s Diner!')
#
# meal_price = input('Enter the price of your meal: ')
# meal_price = float(meal_price)
# tip_percent = input('Enter tip percent: -> .15, .20, etc. : ')
# tip_percent = float(tip_percent)
# tip_value = meal_price * tip_percent
# tax = meal_price * 0.075
# total_due = meal_price + tax + tip_value
#
# print(f'\nMeal Price\t${meal_price:>7.2f}')
# print(f'Tip @ {tip_percent}%\t${tip_value:>7.2f}')
# print(f'Tax @ 7.5%\t${tax:>7.2f}')
# print(f'Total due\t${total_due:>7.2f}')
# print(f'\nThanks for dining at Bob\'s ')

# midtermpractice2
#
# def main():
#     while True:
#         try:
#             widget_number = input1()
#             discount, widget_value, discount_value, final_price = processing1(widget_number)
#             output1(widget_number, discount, widget_value, discount_value, final_price)
#         except exception as err:
#             print(err)
#
#         answer = input('Would you like to run this program again? Enter Y or N: ')
#         while answer.upper() != 'Y' and answer.upper() != 'N':
#             answer = input('Please enter Y or N: ')
#         if answer.upper() == 'N':
#             print(f'\nThank for using the program')
#             break
#
# def input1():
#     print('\nWelcome to ABC Widget!')
#     print('\tHow many widgets would you like to buy?')
#     widget_number = getPosint()
#     return widget_number
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
#     widget_value = 99*widget_number
#     if widget_number < 10:
#         discount = 0.0
#     elif widget_number >= 10 and widget_number <= 19:
#         discount = .01
#     elif widget_number >= 20 and widget_number <= 49:
#         discount = .02
#     elif widget_number >= 50 and widget_number <= 99:
#         discount = .03
#     elif widget_number >= 100:
#         discount = .04
#     else:
#         discount = 0.00
#     discount = float(discount)
#     discount_value = widget_value * discount
#     final_price = widget_value - discount_value
#     return discount, widget_value, discount_value, final_price
#
# def output1(widget_number, discount, widget_value, discount_value, final_price):
#     print(f'\nYou are buying {widget_number} widgets, earning a {discount*100}% discount.')
#     print(f'Retail price @ $99 each:\t$\t{widget_value: >5.2f}')
#     print(f'Amount you saved today:\t\t$\t{discount_value: >7.2f} ')
#     print(f'Discount price before tax:\t$\t{final_price: >5.2f}')
#
# main()

#midterm_practice3

def main():
    while True:
        try:
            print(f'\nWelcome to the personal budget program!')
            needs_list, costs, total, cost_counter, total = input1()

            output1(needs_list, costs, total)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    needs_list = ['Rent', 'Food', 'Transport', 'Other']
    costs = []
    total = 0
    for index in range(len(needs_list)):

        print(f'How much did you spend on {needs_list[index]}?')
        cost_counter = getPosint()
        costs.append(cost_counter)
        total += cost_counter
    return needs_list, costs, total, cost_counter, total

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == '0':
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

def output1(needs_list, costs, total):
    # for i in range(len(needs_list)):
    #     print('{:15}'.format(needs_list[i]), end='')
    # print()
    # for i in range(len(costs)):
    #     print('${:<14,.2f}'.format(costs[i]), end='')
    #     print()

    for index in range(len(needs_list)):
        print('{:<30}{:>2}{:>5}'.format(needs_list[index], '$', f'{costs[index]}'))
    print('{:<0}{:>4}{:>5}'.format('Your total monthly budget is', '$', f'{total}'))



main()

# print('Welcome to the Guest List Builder')
# guests = []
# while True:
# 	newGuest = input('Type name & enter (hit enter twice to quit): ')
# 	if newGuest == '':
# 		break
# 	else:
# 		guests.append(newGuest)
# print(guests) # compare results
# print(*guests, sep = ", ")
#
# #This will print guest names with their placement number in the list +1
# for index in range(len(guests)):
# 	if index < len(guests) -1:
# 		print(f'Guest #{index + 1} is {guests[index]}, ', end = "")
# 	else:
# 		print(f'and Guest #{index + 1} is {guests[index]}.')
#
#
# print('{:<30}{:>7}'.format('Guest Name','Ticket'))
# for index in range(len(guests)):
# 	print('{:<30}{:>2}{:>5}'.format(guests[index],'#',index + 1001))
# print('{:.<30}{:.>7}'.format('Total',len(guests)))
