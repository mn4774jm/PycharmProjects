'''Name: Thomas Mullins
Definition: Create a program that finds the average grade score for 3 quizzes
avg_grade.py
6/5/19'''


def main(): #Define main
    while True: #Begin validation
        try:
            #Call block
            quizzes, total=input1()
            avg_score = processing1(total)
            output1(quizzes, avg_score)

        except Exception as err:
            print(err)
        #Repeat program block
        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Welcome to the average score calculator:')
    #Collect user input
    print('How many quizzes will be taken? ')
    #Validation
    quizzes = getPosint()
    #Initialize total counter
    total = 0
    #Loop for quiz input
    for quiz in range(quizzes):
        score = input(f'\tEnter score for quiz #{quiz+1}: ')
        #Validation
        while score.isnumeric() is False or float(score) >100 or float(score) <0:
            score = input(f'Please enter only numeric values between 0 and 100.\n\tEnter score for quiz #{quiz+1}: ')
        score = float(score)
        #Counter
        total += score
    return quizzes, total

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0:
        posInt = input('\tPlease enter a whole number, zero or greater: ')
    posInt = int(posInt)
    return posInt


def processing1(total):
    #Average calculation
    avg_score = round((total)/3)
    return avg_score

def output1(quizzes, avg_score):
    #Print statement
    print(f'The average of the {quizzes} quiz scores is: {avg_score:,.2f}%')



main()