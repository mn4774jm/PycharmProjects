print('Welcome to Podunk College!')
def main():
    while True:
        try:
            score = input1()
            course, class_needed, total_cost = processing1(score)
            output1(score, course, class_needed, total_cost)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('What was the score on your accuplacer reading test?')
    score = get_posint()
    return score

def get_posint():  # request and validate positive integer
    posint = input('\tEnter a score from 0 - 120: ')
    while posint.isnumeric() is False or int(posint) < 0 or int(posint) >= 121:
        posint = input('\tPlease enter a valid number: ')
    posint = int(posint)
    return posint

def processing1(score):
    #conditionals for classes
    if score < 38:
        course = "Adult Basic Ed"
        class_needed = 3
    elif score > 38 and score <= 59:
        course = "Reading 100"
        class_needed = 2
    elif score > 59 and score <= 77:
        course = "Reading 200"
        class_needed = 1
    else:
        course = "College English"
        class_needed = 0
    #conditional for making ABE free
    credit_cost = 500
    if score < 38:
        total_cost = (class_needed-1)*credit_cost
    else:
        total_cost = class_needed*500
    return course, class_needed, total_cost

def output1(score, course, class_needed, total_cost):
    print(f'\nWith a Reading Accuplacer score of {score}...')
    print('{:<25}{:>25}'.format('Your English class is:', course))
    print('{:<25}{:>23}'.format('Pre-college classes needed:', class_needed))
    print('{:<25}{:>15}{:>10.2f}'.format('Cost @ $500 per class:', '$',total_cost))
    print('\n*NOTE: ABE classes are free')

main()