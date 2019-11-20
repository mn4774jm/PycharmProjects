'''Author: Thomas Mullins
Date: 4/3/19
Definition: Write a program that asks the user to type the first, middle and last name of a person into a single input prompt.
initials.py
'''

#Define main
def main():
    while True:#Start exception handling
        try:
            #Functions call
            full_name = input1()
            name_title, name_list, first, middle, last = processing1(full_name)
            output1(name_title, first, middle, last)

        except Exception as err:#end exception
            print(err)#print error message if encountered

        #reapeat function
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

#Define input1
def input1():
    print('\nWelcome to the initials generator!')
    print('Please enter a full name.')
    full_name = input('Include a first, middle, and last names: ')
    while full_name.isnumeric():#Validation
        full_name = input('Include a first, middle, and last names: ')
    return full_name #Return argument

#Define processing1
def processing1(full_name):
    initial_list = [] #Initialize list
    name_title = full_name.title()#Convert name to title format
    name_list = name_title.split()#split list
    #splice first letter of each list item
    first = name_list[0][0]
    middle = name_list[1][0]
    last = name_list[2][0]
    #return arguments
    return name_title, name_list, first, middle, last

#Define output1 function
def output1(name_title, first, middle, last):
    print('If the full name is '+str(name_title)+'...')
    print('The initials are '+ first + '.' + middle + '.' + last +'.')
#call main
main()
