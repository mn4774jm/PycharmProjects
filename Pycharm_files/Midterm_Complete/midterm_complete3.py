'''Author: Thomas Mullins
Date: 3/21/19
Definition: Create a program where users make a list of items they need to buy
with a list of prices, and a total
midterm3.py'''
#Defining main
def main():
    while True:#Exception handling
        try:
            #List of functions to call including parameters and arguments
            items_list, cost_counter, num_items, total = input1()
            output1(items_list, cost_counter, total)
        except Exception as err:
            print(err)#Exception handling end

        # Restart feature
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':  # Validation to ensure y or n answer
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break  # Program breaks if n is selected

#Defining input function
def input1(): #as only calculation present was adding up the total; combined input and processing
    print('\nWelcome to the shopping list program!')
    items_list = [] #empty list for items
    cost_counter = [] #Empty list for cost
    total = 0 #total counter starts at 0
    print('How many items are on your shopping list today?')
    num_items = getPosint1() #call for validation
    for item in range(num_items): #loop for item types
        product = input(f'\tEnter item #{item + 1}: ')
        items_list.append(product) #add items to list

    for index in range(len(items_list)):#Loop for item prices
        print(f'Enter the price of {items_list[index]} - round to the nearest whole dollar')
        cost = getPosint1() #call for validation
        cost_counter.append(cost) #add price to cost_counter list
        total += cost
    return items_list, cost_counter, num_items, total #return parameters
#validation block
def getPosint1():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == '0':
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

#Define output function
def output1(items_list, cost_counter, total):#arguments arranged positionally
    print('\nHere is your shopping list:')
    for index in range(len(items_list)):#loop to print both item type and cost
        print('{:<20}{:>6}{:>9.2f}'.format(items_list[index], '$', cost_counter[index]))
    print('{:<20}{:>6}{:>9.2f}'.format('Estimated total:', '$', total))#Estimated cost total print

#call main
main()
