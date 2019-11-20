'''Final_practice2
write a program that asks the user to enter a sentence and then count the letters'''

import re

def main():
    while True:
        try:
            sentence = input1()
            processing1(sentence)
        except Exception as err:
            print(err)
        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Welcome to the letter counting machine!')
    regex = re.compile(r'\w+\s[!?.]?')
    sentence = input('Please enter a sentence: ')
    mo = regex.search(sentence)
    while mo == None:
        sentence = input('Please enter a sentence with words and spaces: ')
        mo = regex.search(sentence)
    return sentence

def processing1(sentence):
    sentence = sentence.strip()
    sentence = sentence.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    print(f'You entered the following sentence:\n{sentence}')
    for index in range(0,26):
        print(alphabet[index], end=' ')
    print()

    for index in range(0,26):
        print(sentence.count(alphabet[index]), end=' ')
    print()



main()