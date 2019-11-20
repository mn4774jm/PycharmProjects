""" M. Bock 6/17/2019 This program asks the user how many integers they would like to pick for their list,
 The program randomly selects that number of integers, and saves each pick in a list. The program sorts and
  adds the numbers, then determines min and max. It displays the information in different ways
  - with a short cut, a loop & a sentence. """

import random

print('Welcome to our random number game.')

def main():
    try:
        num_list = inputs()
        total, min_num, max_num = processing(num_list)
        outputs(num_list, total, min_num, max_num)

        restart = input('\nWould you like to pick again? Enter y or n: ').lower()
        if restart == 'y':
            print('Let\'s play again...')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:
        print(err)


def inputs():  # collect information needed, from user and by random selection
    print('How many integers should the computer pick for your list?')
    picks = get_posint()  # user sets list length
    num_list = []  # initialize empty list
    for pick in range(picks):  # loop runs user-defined number of times
        num_picked = random.randint(0, 9)  # pick a random int for each trip through the loop
        num_list.append(num_picked)  # add the number picked to the list
    num_list.sort()  # sort the list - best to do this here
    return num_list

def get_posint():  # request and validate positive integer
    posint = input('Please enter a whole number: ')
    while posint.isnumeric() is False or int(posint) == 0:
        posint = input('You can only enter a number 1 or higher: ')
    posint = int(posint)
    return posint

def processing(num_list):
    total = sum(num_list)  # accumulate the total of the numbers counted
    min_num = min(num_list)  # identify and save the min
    max_num = max(num_list)  # identify and save the max
    return total, min_num, max_num

def outputs(num_list, total, min_num, max_num):
    print(f'\nHere is your list of {len(num_list)} integers - randomly selected & sorted:')
    print(num_list)   # print sorted list without other formatting
    print('Here is your list - printed w/shortcut method:')
    print(*num_list, sep=", ")  # shortcut printing removes brackets
    print('Here is your list - printed via a loop, with total: ')
    for index in range(len(num_list)):  # loop printing for ultimate control
        if index < len(num_list) - 1:
            print(f'{num_list[index]} + ', end="")  # print all nums except last one
        else:
            print(f'{num_list[index]} = {total}')  # print for last num & total
    print(f'Your list minimum was {min_num} and maximum was {max_num} this time.')


main()