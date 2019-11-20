'''Author: Thomas Mullins
Definition: Write a program that asks for user input for how many widgets
they want to buy and givethem output stating how much they owe, saved and the
pretax value.
midtermPractice2.py
Date: 3/8/19'''

#Header
print('Welcome to ABC widget!')
#Define main program block
def main():
    #Exception start
    try:
    #Input data called
        numWidget = inputData()
    #Processing called
        discount, numWidget, total, amountSaved, discountPrice = processing(numWidget)
    #Output called
        output(numWidget, discount, total, amountSaved, discountPrice)
    #Restart asked after all other functions called
        # Ask user if they would like to restart
        restart = input('Would you like to start over? Enter y or n: ')
        # If statement to define next step
        if restart == 'y':
            print()
            main()#If yes call main again
        else:
            print('Thanks for using the program')

    except Exception as err: #General exception end
        print(err)

def inputData(): #user input data block
    print('How many widgets do you want to buy?')
    numWidget = input('\tEnter a whole positive number: ')

    # Validation
    while not numWidget.isnumeric() or int(numWidget) < 0:
    #If not numeric user is asked to reenter input
        numWidget = input('\tPlease enter a whole number, greater than 0:')
    #Return data for number of widgets
    return numWidget

def processing(numWidget):#Processing block for all calculations
    discount = 0
    numWidget = int(numWidget)
    if numWidget < int(10): #Conditional logic start
        discount = 0
    elif numWidget >= 10 and numWidget <=19:
        discount = .1
    elif numWidget >= 20 and numWidget <=29:
        discount = .2
    elif numWidget >= 30 and numWidget <= 39:
        discount = .3
    elif numWidget >= 40:
        discount = .4
    #Calculations start
    total = numWidget*99
    total = int(total)
    amountSaved = numWidget*discount
    discountPrice = total - amountSaved
    #Return all defined variables
    return discount, numWidget, total, amountSaved, discountPrice

#Output data block
def output(numWidget, discount, total, amountSaved, discountPrice):
    print(f'\nYou are buying {numWidget} widgets, earning a {discount*100: <0.0f}% discount.')
    print(f'Retail price @ $99 ea:\t$\t{total: ^5.2f}')
    print(f'Amount you saved today:\t$\t{amountSaved: >7.2f}')
    print(f'Discount price b4 tax:\t$\t{discountPrice: ^5.2f}')

#Main called
main()
