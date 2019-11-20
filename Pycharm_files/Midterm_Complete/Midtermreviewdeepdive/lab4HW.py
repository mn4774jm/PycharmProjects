
#loop-2list.py

'''def main():
    while True:
        try:

            small, large = input1()
            countingList, totalCount = processing(small, large)
            output1(countingList, totalCount)

        except exception as err:
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

def processing(small, large):
    countingList = []
    totalCount = 0.0
    print('Here is a number list printed via a loop:')
    for i in range(small, large+1):
        countingList.append(i)
        totalCount += i
    return countingList, totalCount

def output1(countingList, totalCount):

    print(f'You counted {countingList} = {totalCount}')

main()'''

#quizAvg_list.py

def main():

    studentNum, quizNum = input1()
    listOflists, totalAvg, total, student, studentList, studentTotal, studentAvg = processing1(studentNum, quizNum)
    #getPosint()
    output1(studentNum, quizNum, listOflists, totalAvg)
    #output2(student, studentList, studentTotal, studentAvg)

def input1():
    print('How many students are taking quizzes: ')
    studentNum = getPosint()
    print('How many quizzes are they taking?')
    quizNum = getPosint()
    return studentNum, quizNum

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == '0':
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

def processing1(studentNum, quizNum):
    total = 0
    listOfLists = []
    for student in range(studentNum):
        studentList = []
        studentTotal = 0
        studentAvg = 0
        print(f'\nQuiz info for student #{student+1}: ')
        for quiz in range(quizNum):
            print(f'Score for quiz #{quiz +1}: ')
            score = getPosint()
            studentList.append(score)
            studentTotal += score
            studentAvg = studentTotal / quizNum
        #print(f'Quiz score list for student #{student+1}: {studentList}')
        #print(f'Total points = {studentTotal}')
        #print(f'Quiz average is {studentAvg}')
        output2(student, studentList, studentTotal, studentAvg)
        listOfLists.append(studentList)
        total += studentTotal
    totalAvg = (total / (quizNum * studentNum))
    return listOfLists, total, totalAvg, student, studentList, studentTotal, studentAvg

def output1(studentNum, quizNum, listOfLists, totalAvg):
    print(f'\nOverall results for {studentNum} students & {quizNum} quizzes:')
    print(f'Here is the list of lists : {listOfLists}')
    print(f'Group average: {totalAvg}%')

def output2(student, studentList, studentTotal, studentAvg):
    print(f'Quiz score list for student #{student + 1}: {studentList}')
    print(f'Total points = {studentTotal}')
    print(f'Quiz average is {studentAvg:.2f}%')


main()
