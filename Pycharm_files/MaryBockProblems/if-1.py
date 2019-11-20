def main():
    while True:
        try:

            pennies = input1()
            penny_value = processing1(pennies)
            output1(penny_value, pennies)

        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Enter the number of pennies in the jar')
    pennies = getPosint()
    return pennies

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0:
        posInt = input('\tPlease enter a whole number, greater then zero: ')
    posInt = int(posInt)
    return posInt

def processing1(pennies):
    penny_value = pennies*0.01
    return penny_value

def output1(pennies, penny_value):
    if pennies < 100:
        print('Not quite a dollar yet. Keep saving!')
    else:
        print(f'You have more then one dollar.\n${penny_value:.2} to be exact.')

main()
