'''
Thomas Mullins
albums.py
Definition: Write a program that is used to add up the total number of albums from a users input
6/6/19
'''

def main():
    while True:#Validation block
        try:
            #Call block
            cd_num, lp_num = input1()
            total = processing1(cd_num, lp_num)
            output1(cd_num, lp_num, total)

        except Exception as err:
            print(err)

        #Repeat block
        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1(): #User input block
    print('Welcome to the album program')
    print('How many CDs do you have? ')
    #validation
    cd_num = getPosint()
    #Validation
    print('How many LPs do you own?')
    lp_num = getPosint()
    return cd_num, lp_num

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0:
        posInt = input('\tPlease enter a whole number, zero or greater: ')
    posInt = int(posInt)
    return posInt

def processing1(cd_num, lp_num): #Math processes
    total = cd_num+lp_num
    return total

def output1(cd_num, lp_num, total): #Output block
    print(f'With {cd_num} CDs and {lp_num} LPs you have a total of {total} albums.')

main()

