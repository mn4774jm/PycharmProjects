'''Thomas Mullins
grade.py
Definition: Program that asks for a student's quiz score and reports back the grade received
6/6/19'''

def main():
    while True:
        try:

            score = input1()
            output1(score)

        except Exception as err:
            print(err)

        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Welcome to the grade program')
    print('What was your quiz score?')
    score = getPosint()
    return score

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or int(posInt) < 0 or int(posInt) > 100:
        posInt = input('\tPlease enter a whole number, between 0 and 100: ')
    posInt = int(posInt)
    return posInt

def output1(score):
    if score >=90:
        print('Great job, you got an A!')
    elif score >=80:
        print('Looks like a B to me!')
    elif score >= 70:
        print('Middle of the road C. May want to revise some study habits')
    elif score >= 60:
        print('This is a D. Try a little harder next time.')
    elif score == '':
        print('Undefined')
    elif score < 60:
        print('Ouch... F...See you in summer school!')
    else:
        print('Wait? How the... WHAT HAVE YOU DONE?!')

main()
