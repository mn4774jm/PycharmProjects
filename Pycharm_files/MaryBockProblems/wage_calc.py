'''
Thomas Mullins
wage_calc.py
Definition: Write a program that calculates regular and overtime wages
6/1/19
'''

def main(): #Define main
    while True:#Validation start
        try:
            #Call function block
            hours_worked=input1()
            total=processing1(hours_worked)
            output1(total, hours_worked)

        except Exception as err:
            print(err)
        #Repeat block
        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Welcome to the wage calc program')
    #User input block created
    print('Enter the number of hours worked this week: ')
    #Validation
    hours_worked = getPosint()
    return hours_worked

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0:
        posInt = input('\tPlease enter a whole number, zero or greater: ')
    posInt = int(posInt)
    return posInt

def processing1(hours_worked):
    #Wage calculations
    wage = 15.34
    overtime = 15.34*1.5
    if hours_worked >40:
        r_wage = 40*wage
        ot_wage = (hours_worked-40)*overtime
        total = r_wage+ot_wage
    else:
        total = hours_worked*wage
    return total

def output1(total, hours_worked):
    #Print statement
    print(f'You worked a total of {hours_worked:,.2f} hours earning ${total:,.2f}')

main()