print('\n')
# Main def will always come first and should be empty
def main():
    try: #Exception handling begin
        #All main lines must be inside 'try:' to function

        #main program goes here
        #variables are assigned to inputData, data from input block always goes here
        quizScores, studentNumber = inputData() #inputData is called

        #Start of for loop to define student number
        for student in range(studentNumber):

            #set accumulator to zero
            total = 0.0

            #Header for student quiz score loop, and 1 for each loop
            print(f'Quiz info for student #{student + 1}')

            #averageQuiz defined
            averageQuiz = processing(quizScores, studentNumber)

            #Output called with averageQuiz used as argument
            output(averageQuiz)

    except Exception as err:
            print(err) #When an error occurs the error message will be printed

#Defining all input data
def inputData():

    #Ask user how many students
    studentNumber = int(input('How many students are in the group? '))

    #Ask user how many quizzes
    quizScores = int(input('How many quizzes do they take? '))

    #When inputData is called, quizScores and studentNumber is returned
    return quizScores, studentNumber

def processing(quizScores, studentNumber):

    #total set to zero for each student
    total = 0

    #set range for loop from "How many quizzes"
    for quiz in range(quizScores):

    #Input score for each quiz, +1 for each quiz in range
        score = float(input(f'\tEnter score for quiz #{quiz + 1}:'))

    #Variables for output average
        total += score
        average = total/quizScores

        #print statement for total points
    print(f'Total quiz points for student = {total: .2f}')
    return average

def output(average): #calls for average from processing
    print(f'Quiz average for student = {average: .2f}%\n')


main() #Call for
print('Thank you for using the program')
