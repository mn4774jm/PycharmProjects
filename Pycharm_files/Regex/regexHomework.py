'''
Author: Thomas Mullins
Description: Write a program using regex that can identify input of numerals including decimals
and negative numbers, if the user wants.
regexHomework.py
Date: 4/11/19
'''
#Import regex module
import re
#Define main block
def main():
    #Exception handling
    while True:
        try:
            #Various calls to other functions
            patternMatch = input1()
            patternMatch2 = processing1(patternMatch)
            output1(patternMatch2)

        except Exception as err:
            print(err)
        #Repeat option block
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThat\'s fine... We\'re sure that you\'re a very important person.')
            break
#Define input1 function block
def input1():
    #Compile regular expressions
    floatRegex = re.compile(r'(-)?\d+(\.)?(\d+)?')
    vanillaRegex = re.compile(r'\d+')
    #Introduction print statement
    print('Welcome to the float validation program!\nHere we can validate negatives,'
          ' decimals, and plain old whole numbers.')
    #User input variable created
    userInput = input('\nWhat\'cha got for us? Don\'t worry, no judgements here: ')
    #.search() to find relevent defined data; assign to variable
    patternMatch = floatRegex.search(userInput)
    #While loop for validation
    while patternMatch == None:
        userInput = input('\nAhem... Enter a number: ')
        patternMatch = floatRegex.search(userInput)
    # if vanillaRegex.search(userInput):
    #     print('I know we said no judgements, but \"Ya Basic\". ')

        #processing1(patternMatch)

    else:
        #Return patternMatch for argument use
        return patternMatch
#Define processing1 function
def processing1(patternMatch):
    #patternMatch2 created to hold all group info
    patternMatch2 = patternMatch.group(0)
    #return patternMatch2 for use as argument
    return patternMatch2
#Define output1 function
def output1(patternMatch2):
    #print statement for final output
    print('Your number is: ' + patternMatch2)
#call main function
main()