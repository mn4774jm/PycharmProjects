'''Author: Thomas Mullins
Date: 2/19/19
QuizAvg.py
Definition: Calculate and display the total and average quiz score for each student in a group.
'''
#Beginng of first loop
while True:
#Variables
#Ask number of students
    studentNumber = int(input('How many students are in the group?'))
    studentCounter = 0
    quizNumber = int(input('How many quizzes do they take?'))
    quizCounter = 1
    totalScore = 0

    if studentNumber.isnumeric() and quizNumber.isnumeric():
        studentNumber = int(studentNumber)
        quizNumber = int(quizNumber)

        while quizCounter <= quizNumber:
            score = int(input(f'\tEnter Score for quiz #{quizCounter}:'))
            totalScore = totalScore + score
            averageScore = totalScore/quizNumber
            quizCounter = quizCounter + 1
        else:
            print(f'Total quiz points for student #{studentCounter} is {totalScore}\nStudent #{studentCounter} quiz average is {averageScore}%')

        break

