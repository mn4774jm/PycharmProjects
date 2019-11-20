'''Author: Thomas Mullins
Definition: The program calculates a personal budget based on four budget categories that should be saved into a list: Rent, Food, Transport, Other
midtermPractice3.py
Date: 3/9/19'''


def main():
    needs, costs, costCounter, total = inputdata()
    output(needs, costs)
    #totalCost = processing(costs)
    monthly(total)

    # Ask user if they would like to restart
    restart = input('\nWould you like to start over? Enter y or n: ')
    # If statement to define next step
    if restart == 'y':
        print()
        main()  # If yes call main again
    else:
        print('Thanks for using the program')


def inputdata():
    print('Welcome to the personal budget program!')
    needs = ['Rent', 'Food', 'Transport', 'Other']
    costs =[]
    total = 0

    for index in range(len(needs)):
        costCounter = 0
        print(f'How much do you spend for {needs[index]}?')
        costCounter = getPosint()
        costCounter = int(costCounter)
        costs.append(costCounter)
        total += costCounter
    return needs, costs, costCounter, total

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == '0':
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

#def processing(costCounter):


def output(needs, costs):
    print(f'\nHere\'s your overall budget:')
    print(f'{needs[0]}\t\t{needs[1]}\t\t{needs[2]}\t\t{needs[3]}')
    print(costs)

def monthly(total):
    print(f'Your total monthly budget is ${total}.')



main()
