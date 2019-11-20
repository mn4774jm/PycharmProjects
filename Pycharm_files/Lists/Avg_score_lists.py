'''Average quiz score 2'''

def main():
    while True:
        try:
            student_number, quiz_num = input1()
            list_of_All, total_average = processing1(student_number, quiz_num)
            output1(student_number, quiz_num, list_of_All, total_average)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':  # Validation to ensure y or n answer
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break  # Program breaks if n is selected

def input1():

    print('How many students are taking quizzes?')
    student_number = get_posint()
    print('How many quizzes will each take?')
    quiz_num = get_posint()
    return student_number, quiz_num

def get_posint():  # request and validate positive integer
    posint = input('\tPlease enter a whole number: ')
    while posint.isnumeric() is False or int(posint) == 0:
        posint = input('\tYou can only enter a number 1 or higher: ')
    posint = int(posint)
    return posint

def processing1(student_number, quiz_num):
    total_all = int(0)
    list_of_all = []
    for student in range(student_number):
        print(f'Quiz information for student #{student+1}.')
        score_list = []
        total_points = 0
        for quiz in range(quiz_num):
            print(f'Score for quiz #{quiz+1}:')
            score = get_posint()
            score_list.append(score)
            total_points += score
            total_all +=score
        avg_points = total_points/quiz_num
        total_average = total_all/quiz_num/student_number
        print(f'Quiz score list for student #{student+1}: ',end= '')
        print(*score_list, sep= ', ')
        print(f'\tTotal points = {total_points}')
        print(f'\tQuiz Average = {avg_points}')
        list_of_all.append(score_list)
    return list_of_all, total_average

def output1(student_number, quiz_num, list_of_all, total_average):
    print(f'Overall results for {student_number} students & {quiz_num} quizzes:')
    print(f'Here is the list of lists: {list_of_all}')
    print(f'Group average = {total_average}')
    print('Thanks for using the program')

main()