'''Author: Thomas Mullins
Date: 2/14/19
loop-2.py
Definition: Write a program which asks the user for a small number.
'''

#Header
print('Welcome to our counting program.\nIt also adds up the digits as you count!')

while True:
#Variables
    small = input('Please enter a small number, 0 or higher: ')
    large = input('Now, enter a larger number that you want to count up to: ')

#Validation
    if small.isnumeric() and large.isnumeric:
        small = int(small)
        large = int(large)
# if statement to make sure small id less than large
        if small < large:
                i = small -1
                total = 0
#Subtract from large by one if higher than small
                while i <= large -1:
                    print(i +1)
                    i = i+1
                    total = total +1


        else :
            print('Enter a number larger than the first entry')
#print output
            print(f'The total number you counted is: {total}')
            break #break from loop

    else:
        print('Please enter a whole number for both') #User error message

