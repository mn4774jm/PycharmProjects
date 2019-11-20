'''
Thomas Mullins
Definition: Write a program that uses a regular expression (regex) to find a Social Security Number within text that's
 entered by the user. See 4 sample inputs and results:
Final2.py
5/9/19
'''
#import module
import re
#Create regular pattern to match
socialRegex = re.compile(r'\d{3}[\-" "]?\d{2}[\-" "]?\d{4}')
#Initialize list
matches = []
#Define main block
def main(): #define main function
    while True:#Exception handling
        try:
            social, matches = input1()
            output1(social, matches)
        except Exception as err:
            print(err)
         #Repeat block
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    #Collect user data
    print('\nWelcome to the SSN finder!')
    social = input('Please enter a SSN, with instructions on using it: ')
    mo = socialRegex.search(social)
    #Use .search for validation
    while mo == None:
        print('No SSN found. Use one of these formats.')
        print('\txxx-xx-xxxx or xxx xx xxxx or xxxxxxxxx')
        social = input('Please enter a SSN, with instructions on using it: ')
        mo = socialRegex.search(social)
    #Collect matches using .findall
    matches = socialRegex.findall(social)
    return social, matches

def output1(social, matches):
    #Print user data
    print('Success!')
    print(f'You entered: {social}')
    print('It contains an SSN: ', end='')
    print(*matches, sep= "")


main()