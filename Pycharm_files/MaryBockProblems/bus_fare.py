'''
Thomas Mullins
bus_fare.py
Definition: Write a program that calculates the total cost of bus far from regular and rush hour rates from user input
6/6/19
'''


def main():
    while True: #Exception handling
        try:
            #Function call block
            reg_ride, rush_ride=input1()
            total, reg_fare, rush_fare, total_rides=processing1(reg_ride, rush_ride)
            output1(total, reg_ride, reg_fare, rush_ride, rush_fare, total_rides)

        except Exception as err:
            print(err)

        #Repeat function
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Welcome to the bus fare calculator')
    #User input
    print('How many times did you ride during regular fare hours? ')
    #validation
    reg_ride = getPosint()
    #Validation
    print('How many times did you ride during Rush Hour? ')
    rush_ride = getPosint()

    return reg_ride, rush_ride

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0:
        posInt = input('\tPlease enter a whole number, zero or greater: ')
    posInt = int(posInt)
    return posInt

def processing1(reg_ride, rush_ride):
    #All math equations and processes
    reg_fare = reg_ride*1.75
    reg_fare = float(reg_fare)
    rush_fare = rush_ride*3.0
    rush_fare = float(rush_fare)
    total = reg_fare+rush_fare
    total_rides = reg_ride+rush_ride
    total_rides = int(total_rides)
    return total, reg_fare, rush_fare, total_rides

def output1(total, reg_ride, reg_fare, rush_ride, rush_fare, total_rides):
    #Output formatting block
    print(f'\nTotal monthly bus fare for {total_rides} trips = ${total:,.2f}.')
    print('{:<10}{:>15}{:>15}{:>15}'.format('Type', 'Trips', 'Fare', 'Total'))
    print('{:<10}{:>15.0f}{:>15}{:>8}{:>7.2f}'.format('Regular', reg_ride, '$1.75', '$', reg_fare))
    print('{:<10}{:>15.0f}{:>15}{:>8}{:>7.2f}'.format('Rush', rush_ride, '$3.00', '$', rush_fare))


main()