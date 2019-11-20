'''Author: Thomas Mullins
Date: 2/28/19
loops-2fun.py
Definition: Recreate the loops-2 using defs'''


#Header
print('Welcome to our counting program.\nIt also adds up the digits as you count!')

# Define main block
def main():
#exception start
    while True:
        try:
            small, large = inputData()
            numberCount=calculations(small, large)
            output(numberCount)

        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ').upper()
        while answer != 'Y' and answer != 'N':
            answer = input('Please enter Y or N: ').upper()
        if answer == 'N':
            print(f'\nThank for using the program')
            break

def inputData():
    print('Please enter a small number.')
    small = getPosint()
    print(f'Now, enter a number larger than {small}: ')
    large = getPosint()
    while small >= large:
        print(f'Sadly, you entered "{large}," which happens to be smaller than your first entry. Please try again.')
        large = getPosint()
    return small, large

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0:
        posInt = input('\tPlease enter a whole number, zero or greater: ')
    posInt = int(posInt)
    return posInt

def calculations(small, large):
    total=0
    for numbers in range(small, large+1):
        print(numbers)
        total += numbers
    return total

def output(total):
    print(f'The total number you counted is: {total}')



main()