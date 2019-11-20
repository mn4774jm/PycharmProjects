'''Thomas Mullins
apollo.py
def: Ask user to guess the year of the moon landing and report back if they are correct. Tells user if they are close
6/6/19'''

def main():
    while True:
        try:

            year = input1()
            output1(year)

        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break


def input1():
    print('What year was the moon landing?')
    year = getPosint()
    return year

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a 4 digit year: ')
    while posInt.isnumeric() is False:
        posInt = input('\tPlease enter only whole numbers: ')
    posInt = int(posInt)
    return posInt


def output1(year):
    if year == 1969:
        print('Correct! The moon landing was July 20, 1969')
    elif year == 1968 or year == 1970:
        print('Very close, but it looks like you\'re still a year off.')
    else:
        print('Bummer, nope.')

main()