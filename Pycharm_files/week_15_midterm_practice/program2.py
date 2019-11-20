'''Thomas Mullins
Date 5/2/19
Final_practice_2.py
Definition: Write a program that asks the user to enter a sentence.
After validating input, the program will count the number of times each letter
of the alphabet appears in the user's sentence. Upper and lower case letters
should be included in each letter's total count (case insensitive).
If a letter appears 0 times, that should be reported as well.  '''

import re

def main():
    #import re for validation
    import re
    #Exception handling
    try:

            #call functions
            message = input1()
            processing1(message)
        #Exception handling end
    except Exception as err:
        print(err)


def input1():
    #regex for validation
    regex = re.compile(r'\w+\s[!.?;]?')
    #welcome statement
    print('Welcome to the letter machine!')
    #ask for user input
    message = input('Please enter a sentence: ')
    #Pattern match
    mo = regex.search(message)
    #Loop if validation check doesn't pass
    while mo == None:
        message = input('Please enter a sentence with words and spaces: ')
        mo = regex.search(message)
    return message

def processing1(message):
    #Print opening strings
    print(f'You entered the following sentence:\n{message}')
    print('Here is your character count:')
    #Remove blank space
    message = message.strip()
    #All lower to match list
    message = message.lower()
    #Alphabet list
    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    #Print range for letters
    for i in range(0, 26):
        print(Alphabet[i], sep=' ', end= ' ')
    print()
    #Print number of letters
    for i in range(0, 26):
        print(message.count(Alphabet[i]), sep= ' ', end=' ')


main()