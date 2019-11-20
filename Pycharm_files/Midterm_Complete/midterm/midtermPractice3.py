'''Author: Thomas Mullins
Definition: The program calculates a personal budget based on four budget categories that should be saved into a list: Rent, Food, Transport, Other
midtermPractice3.py
Date: 3/9/19'''


def main():
    while True:

        try: #Exception start
        #Calling all functions
            needs, costs, costCounter, total = inputdata()
            output(needs, costs)
        #totalCost = processing(costs)
            monthly(total)
        except Exception as err: #General exception end
            print(err)

        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break


def inputdata(): #Define input data and computation (Tried to seperate)
    print('Welcome to the personal budget program!') #Print Header
    needs = ['Rent', 'Food', 'Transport', 'Other'] #Defining needs variables
    costs =[] #Empty list
    total = 0 #Total zeroed for monthly output

    for index in range(len(needs)): #Loop to get need amounts
        costCounter = 0 #Cost counter zeroed
        print(f'How much do you spend for {needs[index]}?') #ask for user input
        costCounter = getPosint() #run getPosint function
        costCounter = int(costCounter) #define cost counter as int
        costs.append(costCounter) #Add costs to list
        total += costCounter #Adds up costs for total
    return needs, costs, costCounter, total

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == '0':
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt


def output(needs, costs): #define output function
    print(f'\nHere\'s your overall budget:')
    needsList = ''
    costList = ''
    #print(f'{needs[0]}\t\t{needs[1]}\t\t{needs[2]}\t\t{needs[3]}')
    #print(costs)
    for i in range(len(needs)):
        # each item gets a 15 character space
        #needsList = needsList + '{:15}'.format(needs[i])
        needsList += '{:15}'.format(needs[i])
        costList += '${:14}'.format('{:.2f}'.format(costs[i]))

    print(needsList)#   ****PRACTICE THIS*** PPT Ch1.2********
    print(costList)

def monthly(total): #Define monthly output
    print(f'Your total monthly budget is ${total}.')



main()
