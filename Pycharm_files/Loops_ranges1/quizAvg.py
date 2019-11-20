'''Author: Thomas Mullins
Date: 2/19/19
quizAvg.py
Definition: Calculate and display the total and average quiz score for each student in a group.
'''
def main():
    while True:
        try:
            studentNumber, quizScores = input1()
            total_all, average_all   = processing1(studentNumber, quizScores)
            output1(total_all, average_all )
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ').upper()
        while answer != 'Y' and answer != 'N':
            answer = input('Please enter Y or N: ').upper()
        if answer == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    # Assign variables
    print('How many students do you have? ')
    studentNumber = getPosint()
    # Get the number of test scores per student
    print('How many quizzes per student? ')
    quizScores = getPosint()
    return studentNumber, quizScores

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0:
        posInt = input('\tPlease enter a whole number, zero or greater: ')
    posInt = int(posInt)
    return posInt

def processing1(studentNumber, quizScores):

    # Determine each student’s average test score and start loop 1
    for student in range(studentNumber):
        # accumulator for quiz scores
        total = 0.0
        total_all = 0.0
        # header for student quiz scores loop
        print(f'Quiz info for student #{student + 1}')
        #Start 2nd loop; quiz scores
        for quiz in range(quizScores):
            print(f'\tEnter score for quiz #{quiz + 1}:')
            score = float_regex()
            #add the score to accumulator
            total += score
            average = total / quizScores
        print(f'Total quiz points for student #{student + 1} = {total: .2f}')
        print(f'Quiz average for student #{student + 1} = {average: .2f}')
        total_all += total
        # Calculate the average test score for this student
        average_all = total_all/quizScores
    return total_all, average_all

def float_regex():
    import re
    floatRegex = re.compile(r'(-)?\d+(\.)?(\d+)?')
    user_input = input('Please Enter a number: ')
    mo = floatRegex.search(user_input)
    while mo == None or float(user_input) < 0:
        user_input = input('Enter only numeric values: ')
        mo = floatRegex.search(user_input)
    user_input = float(user_input)
    return user_input

def output1(total_all, average_all):
    #Display the average

    print(f'Total quiz points for all students = {total_all: .2f}')
    print(f'Quiz average for all students = {average_all: .2f}')
    print() #Space to break up data; easier to read

main()