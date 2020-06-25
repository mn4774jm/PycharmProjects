# '''Final_practice1.py'''
#
# def main():
#     while True:
#         try:
#
#             number = input1()
#             new_num_added, num_added, num_add, num_mult=processing1(number)
#             output1(new_num_added, number, num_added, num_add, num_mult)
#
#         except Exception as err:
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
#     print('\nWelcome to the digit processing machine!')
#     number = input('Please enter a three-digit number, 100 to 999: ')
#     number = int(number)
#     while number <100 or number > 999:
#         number = input('You can only enter numbers from 100 to 999:')
#         number = int(number)
#     return number
#
# def processing1(number):
#     num_added = [int(d) for d in str(number)]
#     num_add = num_added[0]+num_added[1]+num_added[2]
#     num_mult = num_added[0]*num_added[2]+num_added[1]
#     new_num_added = num_added.sort()
#     return num_added, new_num_added, num_add, num_mult
#
# def output1(new_num_added, number, num_added, num_add, num_mult):
#     print('{:<0}{:>15}'.format('If your integer is:', number))
#     print('{:<0}{:>13}'.format('Your digits added up:', num_add))
#     print('{:<0}{:>11}'.format('Your digits multiplied:', num_mult))
#     print('{:<0}{:>12}'.format('Your minimum digit is:', str(new_num_added[0])))
#     print('{:<0}{:>12}'.format('Your maximum digit is:', str(new_num_added[2])))
#
# main()

def main():

    number = input1()
    num_added, num_add, num_mult, num_sort=processing1(number)
    output1(number, num_added, num_add, num_mult, num_sort)

def input1():
    print('Welcome to the digit processing machine!')
    number = input('Please enter a three digit number, 100 to 999: ')
    number = int(number)
    while number < 100 or number >999:
        number = input('You can only enter numbers from 100 to 999: ')
        number = int(number)
    return number

def processing1(number):
    num_added = [int(d) for d in str(number)]
    num_add = num_added[0]+num_added[1]+num_added[2]
    num_mult = num_added[0]*num_added[1]*num_added[2]
    num_sort = num_added.sort()
    return num_added, num_add, num_mult, num_sort

def output1(number, num_added, num_add, num_mult, num_sort):
    print('{:.<0}{:.>17}'.format('If your integer is',number))
    print('{:.<0}{:.>15}'.format('Your digits added up', num_add))
    print('{:.<0}{:.>13}'.format('Your digits multiplied', num_mult))
    print('{:.<0}{:.>14}'.format('Your minimum digit is', str(num_added[0])))
    print('{:.<0}{:.>14}'.format('Your maximum digit is', str(num_added[2])))



main()

