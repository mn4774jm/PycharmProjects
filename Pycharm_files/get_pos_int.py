
#Example for get_pos_int


def input1():
    print('How many students are taking quizzes: ')
    studentNum = getPosint()
    print('How many quizzes are they taking?')
    quizNum = getPosint()
    return studentNum, quizNum

#GetPosInt does not need to me called in main; only during validation

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == '0':
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

