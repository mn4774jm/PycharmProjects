import math
import random

# when function is called it takes the arguments and uses them as replacements
#for its stand in variables. In this instance stringData = text and repeat = n
'''def main():
    stringData = input('please enter a string: ')
    repeat = int(input('How many times to repeat? '))
    stringRepeater(stringData, repeat)

def stringRepeater(text, n):
    repeatedString = text*n
    print('Here\'s your string...')
    print(repeatedString)

main()'''

#loop-2fun.py

'''def main():
    while True:

        try: #Exception start
            small, large = input1()
            total = processing1(small, large)
            output1(total)
        except Exception as err: #General exception end
            print(err)

        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Welcome to our counting program.\n It also adds up the digits as you count')
    small = input('Please enter a small number, 0 or higher: ')
    while small.isnumeric() is False or int(small) <= 0:
        small = input('Please enter a whole number, 0 or higher: ')
    small = int(small)

    large = input(f'Please enter a whole number larger than {small}: ')
    while large.isnumeric() is False or int(large) <= 0:
        large = input('Please enter a whole number, 0 or higher: ')
    large = int(large)
    return small, large

def processing1(x,y):
    total = 0
    for number in range(x, y+1):
        print(number)
        total += number
    return total

def output1(x):
    print(f'Your total sum is {x}')


main()'''

#quizAvgFun

def main():
    while True:
        try:
            studentNum, quizNum = input1()
            totalForAll, totalAvg = processing1(studentNum, quizNum)
            #output1(total, average)
            output2(totalForAll, totalAvg)
        except Exception as err:  # General exception end
            print(err)

        answer = input(f'\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break


def input1():
    studentNum = input('How many students are in the group? ')
    while studentNum.isnumeric() is False or int(studentNum) <= 0:
        studentNum = input('Please enter a whole number, 0 or higher: ')
    studentNum = int(studentNum)

    quizNum = input('How many quizzes are they taking? ')
    while quizNum.isnumeric() is False or int(quizNum) <= 0:
        quizNum = input('Please enter a whole number, 0 or higher: ')
    quizNum = int(quizNum)
    return studentNum, quizNum

def processing1(studentNum, quizNum):
    totalForAll= 0.0
    totalAvg = 0.0
    for student in range(studentNum):
        total = 0
        average = 0
        print(f'Quiz info for student #{student + 1}')

        for quiz in range(quizNum):
            # Input score for each quiz, +1 for each quiz in range
            score = float(input(f'\tEnter score for quiz #{quiz + 1}:'))
            score = int(score)

            # Variables for output average
            total += score
            average = total / quizNum
            totalForAll += score
            totalAvg += totalForAll / quizNum

            # print statement for total points
        print(f'Total quiz points for student = {total: .2f}')
        print(f'Quiz average for student = {average: .2f}%')

    return totalForAll, totalAvg

def output2(totalForAll, totalAvg):
    print(f'The total score for all students is {totalForAll}. ')
    print(f'The total average for all students is {totalAvg}')


#def output1(total, average): #calls for average from processing
    #print(f'Total quiz points for student = {total: .2f}')
    #print(f'Quiz average for student = {average: .2f}%')
main()











