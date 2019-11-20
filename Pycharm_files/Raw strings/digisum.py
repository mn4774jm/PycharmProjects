'''
Author: Thomas Mullins
Date: 4/3/19
digiSum.py
Definition: Write a program that asks the user to input a five digit integer.
'''


def main(): #define main
    while True:#Exception handling start
        try:
            #Call functions thorugh main
            numbers1 = input1()
            num_list, num_total = processing1(numbers1)
            output1(num_list, num_total, numbers1)

        #exception handling end and error printing
        except Exception as err:
            print(err)

        #repeat?
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

#Define input
def input1():
    print('\nWelcome to the digit adding machine!\nPlease enter a 5-digit integer.')
    #User input and creation of numbers1 variable
    numbers1 = input('Numbers only from 10000 to 99999 - no comma: ')
    #Validation
    while numbers1.isdecimal() is False or int(numbers1) < int(10000) or int(numbers1) > 99999:
        numbers1 = input('Please enter only integers between 10000 and 99999: ')
    # return
    return numbers1

#Define processing1; assign arguments
def processing1(numbers1):
    num_list = [] #Empty list created
    #Loop start
    for digit in range(len(numbers1)):
        #Collect individual digits from loop
        number = int(numbers1[digit])
        #Add numbers as list items to num_list
        num_list.append(number)
        #Get sum from list
    num_total = sum(num_list)
    #return
    return num_list, num_total

#define output1; assign arguments
def output1(num_list, num_total, numbers1):
    #Create empty string
    num_string = ''
    #Begin loop
    for index in range(len(num_list)):
        #accumulate string
        num_string += f'{num_list[index]} '
    #adding total to num_string
    num_string = num_string.split()
    num_string = ' + '.join(num_string)
    num_string += f' = {num_total}'
    print('If your integer is ' + numbers1 + ', your result is....')
    print(num_string)

#call main
main()

