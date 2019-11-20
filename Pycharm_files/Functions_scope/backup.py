'''Author: Thomas Mullins
definition: Calculate student and class averages, including created functions, getPosnt, exception handling, and restart
quizAvg_list.py
3/5/19'''

#Define main code block
def main():
    try: #Exception handling start
        #Call inputs
        numStudents, numQuizzes = inputs()
        #Call Processing
        listOflists, overallAverage = processing(numStudents, numQuizzes)
        #Call for output at end of program
        finalOutputs(listOflists, overallAverage, numStudents, numQuizzes)
        #Ask user if they would like to restart
        restart = input('Would you like to start over? Enter y or n: ')
        #If statement to define next step
        if restart == 'y':
            main()
        else:
            print('Thanks for using the program')
    #End exception handling; print error if present
    except Exception as err:
        print(err)
#Get user input for number of students/quizzes
def inputs():
    print('How many students are taking quizzes?')
    numStudents = getPosint() #call getPosInt to handle input errors
    print('How many quizzes will each one take?')
    numQuizzes = getPosint() #call getPosInt to handle input errors
    #return numStudents and numQuizzes as arguments to input function
    return numStudents, numQuizzes

#function to check for numeric > 0
def getPosint(): #validation block
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == '0':
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

#Processing block for looping data
def processing(numStudents, numQuizzes):
    #Initialize group variables; set all to zero
    overallTotal = 0
    overall_average = 0.0
    #Empty list for end block
    listOflists = []

    #Start loop for student count in range; inside processing
    for student in range(numStudents):
    #initilize student level variables. restarts for each student
        studentTotal = 0
        studentAverage = 0.00
    #Empty list for individual student scores
        studentScorelist = []
        print(f'Quiz info for student #{student + 1}: ') #Add to student (+1) to get accurate student number count

    #Start loop for quiz scores; loop inside student loop
        for quiz in range(numQuizzes):
        #User input
            print(f'\tScore for quiz #{quiz + 1}:')
        #Call getPosint function for valid input
            quizScore = getPosint()
        #Accumulate student total
            studentTotal += quizScore
        #Student list to save quiz scores
            studentScorelist.append(quizScore)
        #Calculate student average
        studentAverage = studentTotal / numQuizzes
        #call loopOutputs to print individual data
        loopOutputs(studentTotal, studentAverage, student, studentScorelist)
        #Add student total points to overall total at top of processing
        overallTotal += studentTotal
        #Add each students list to list of lists
        listOflists.append(studentScorelist)
    #Overall average calculation assigned
    overallAverage = overallTotal / numStudents / numQuizzes
    return listOflists, overallAverage #outside quiz loop

#Def function for individual quiz scores
def loopOutputs(studentTotal, studentAverage, student, studentScorelist):
    #(+1) for correct student count. quiz score formatting doesn't seem to work; still indenting
    print(f'Quiz score list for student #{student + 1}: {studentScorelist} ')
    print(f'\tTotal points = {studentTotal}')
    print(f'\tQuiz Average = {studentAverage :<0.2f}')

#def function block for tabulated data
def finalOutputs(listOflists, overallAverage, numStudents, numQuizzes):
    print(f'Overall results for {numStudents} students & {numQuizzes} quizzes ')
    print('Here is the list of lists: ', listOflists)
    print(f'Group average = {overallAverage:<0.2f}')

main()