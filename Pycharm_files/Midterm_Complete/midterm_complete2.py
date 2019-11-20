'''Author: Thomas Mullins
Date: 3/21/19
midterm2.py
definition: ABC Van Service charges $6.00 per rider, with a maximum of 6 passengers.
The mileage rate depends on the number of miles to be driven '''
#Defining main function
def main():
    while True: #Exception handling start
        try:
            #Functions to call during main()
            passengers, miles = input1()
            price_per_mile, passenger_fee, milage_fee, total = processing1(passengers, miles)
            output1(passengers, miles, price_per_mile, passenger_fee, milage_fee, total)

        except Exception as err:
            print(err) #Exception handling end

        #Restart feature
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N': #Validation to ensure y or n answer
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break #Program breaks if n is selected

def input1(): #defining input; ask for and record user input
    print('\nWelcome to ABC Van Service')
    print('How many passengers are traveling? (limit 6)')
    passengers = getPosint2() #call getPosint2 to validate int and under 6
    print('How many miles to your destination?')
    miles = getPosint1() #call getPosint1 to validate int greater than 0
    return passengers, miles #return parameters

#Function to validate positive integers over zero
def getPosint1():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == '0':
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

#Function to validate positive integers under 6
def getPosint2():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt >= '7': #requires van passengers to be less than or equal to 6 people
        posInt = input('\tPlease enter a whole number (limit 6): ')
    posInt = int(posInt)
    return posInt
#Function for conditional logic calculatiosn
def processing1(passengers, miles): #Arguments
    price_per_mile = 0
    if miles < 10: #Conditional logic begins using if/elif
        price_per_mile = 1.5
    elif miles >= 10 and miles <= 19:#Less than 10
        price_per_mile = 1.25
    elif miles >= 20 and miles <= 49:#Between 10 and 19
        price_per_mile = 1.0
    elif miles >= 50 and miles <= 99:#between 20 and 49
        price_per_mile = 0.75
    elif miles >= 100: #100 and over
        price_per_mile = 0.5

    #Calculations for fees and base rates
    passenger_fee = (passengers *6)
    milage_fee = (miles *price_per_mile)
    total = (passenger_fee + milage_fee) #return parameters

    return price_per_mile, passenger_fee, milage_fee, total #Return calculatiosn

#output functions to display information using shorthand and tuple methods
def output1(passengers, miles, price_per_mile, passenger_fee, milage_fee, total): #arguments
    print(f'Cost of van for {passengers}, traveling {miles} miles, at ${price_per_mile:.2f}:')#Overview of user input
    print('{:<20}{:>6}{:>9.2f}'.format('Passenger fees:', '$', passenger_fee))  # passenger fee
    print('{:<20}{:>6}{:>9.2f}'.format('Milage fees:', '$', milage_fee))  # mileage fees
    print('{:<20}{:>6}{:>9.2f}'.format('Total trip cost:', '$', total))  # Total price for fees

main()