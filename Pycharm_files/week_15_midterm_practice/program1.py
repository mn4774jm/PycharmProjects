'''Thomas Mullins
Date: 5/2/19
practice-1.py
Definition: Write a program to ask for a 3 digit number. Then provide data for several
user input descriptions'''
#import regex for validation

import re

while True:
    try:
        #Print welcome
        print('Welcome to the digit processing machine!')
        #Set Regex for validation of only 3 numbers
        numRegex = re.compile(r'\d\d\d')#seems to be ineffectual
        #input statement
        userNumber = input('Please enter a three-digit number, 100 to 999: ')
        userInt = int(userNumber)
        #validation for over 999
        while userInt >=1000 or userInt <=99:
            userNumber = input('You can only enter numbers from 100 to 999: ')
            userInt = int(userNumber)
        #Search for pattern match
        mo = numRegex.search(userNumber)
        #While loop for validation
        while mo == None:
            userNumber = input('You can only enter numbers from 100 to 999: ')
            mo = numRegex.search(userNumber)
        #Print user entered number
        print('{:<5}{:>25}'.format('If your integer is:', str(userNumber)))
        #Turn string list into int
        numAdded = [int(d) for d in str(userNumber)]
        #add values and print
        numAdd = numAdded[0]+numAdded[1]+numAdded[2]
        print('{:<5}{:>23}'.format('Your digits added up:', str(numAdd)))
        #Multiply values and print
        numMult = numAdded[0]*numAdded[1]*numAdded[2]
        print('{:<5}{:>21}'.format('Your digits multiplied:', str(numMult)))
        #Sort numbers
        numAdded.sort()
        #Call for first number in list
        print('{:<5}{:>22}'.format('Your minimum digit is:', str(numAdded[0])))
        #Call for last number in list
        print('{:<5}{:>22}'.format('Your maximum digit is:', str(numAdded[2])))
    except Exception as err:
        print(err)
    break
