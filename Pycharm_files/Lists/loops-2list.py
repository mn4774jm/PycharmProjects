'''Author: Thomas Mullins
Date: 2/28/19
loops-2list.py
Definition: Recreate the loops-2fun to use a list'''


#Header
print('Welcome to our counting program.\nIt also adds up the digits as you count!')
print()
# Define main block
def main():
#exception start
    while True:
        try:
            #Variables assigned to input data; call input()
            small, large = inputData()
            total, list =calculations(small, large)
            output(total, list)

            #scrpt to print for exception
        except Exception as err:
            print('Please enter only numeric data')

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'Y':
            print(f'\nThank for using the program')
            break
#def inputData block start

def inputData():
        print('Please enter a small number.')
        small = getPosint()
        print(f'Now, enter a number larger than {small}: ')
        large = getPosint()
        while small >= large:
            print(f'Sadly, you entered "{large}," which happens to be smaller than your first entry. Please try again.')
            large = getPosint()
        return small, large #store return data

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0:
        posInt = input('\tPlease enter a whole number, zero or greater: ')
    posInt = int(posInt)
    return posInt

def calculations(small, large): #start of calculation block
    total=0 # zero out total
    list = []#list is created
    for index in range(small, large+1): #range loop is created
        list.append(index)#adding index in range to lists
        total += index #totaling all index
    return total, list # return data

def output(total, list): #output block start
    print(f'\nThe total number you counted is: {total}') #print total
    print(list) #print list

main() #call main

