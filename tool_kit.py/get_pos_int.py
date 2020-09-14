
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

# prompt version
def inputs():
    number_of_eggs = getPosint(prompt="Now, how many eggs are we working with?: ")
    return number_of_eggs

def getPosint(prompt='Enter a positive whole number: '):  # ensures "int-able" input over 0
    posInt = input(prompt)
    while posInt.isnumeric() is False or posInt == 0:
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

