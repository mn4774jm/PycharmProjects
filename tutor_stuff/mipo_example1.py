#
# print('Welcome to More Than One Basket. You tell us the eggs and we tell you how many baskets you will need.')
#
#
# def inputs():
#     number_of_eggs = getPosint(message="Now, how many eggs are we working with?: ")
#     return number_of_eggs
#
# def getPosint(message):  # ensures "int-able" input over 0
#     posInt = input(message)
#     while posInt.isnumeric() is False or int(posInt) <= 0:
#         posInt = input('\tPlease enter a whole number, greater than 0: ')
#     posInt = int(posInt)
#     return posInt
#
# def processing(number_of_eggs):
#     basket_size = 6
#     basket_number = round(number_of_eggs / basket_size)
#     if basket_number % 6 != 0:
#         basket_number = int(basket_number) + 1
#     if basket_number < 1:
#         basket_number = 1
#     return basket_number
#
# def output(eggs, baskets):
#     plural = 's'
#     singular = 'them'
#     if eggs is 1:
#         singular = 'it'
#     if baskets < 2:
#         plural = ''
#     print("Each of our handcrafted in America baskets can hold 6 eggs safely.")
#     print(f"As you have {eggs} egg{plural} you will need {baskets} basket{plural} to safely carry {singular}.")
#
# def main():
#     try:
#         number_of_eggs = inputs()
#         basket_number = processing(number_of_eggs)
#         output(number_of_eggs, basket_number)
#
#         restart = input("Care to dance again? Enter Y or N: ").upper()
#         while restart != 'Y' and restart != 'N':
#             restart = input('Please only enter Y or N: ').upper()
#         if restart == 'Y':
#             main()
#         else:
#             print("Thanks for using the program and bawk-b-bye!")
#     except Exception as err:
#         print(err)
#
# main()

