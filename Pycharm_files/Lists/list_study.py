'''Lists study session'''

# listOfColleges = ['MCTC', 'Metro State', 'SPC', 'MCTC']
# for index in range(len(listOfColleges)):
# 	print(f'College #{index+1}')
# 	print(f'Name: {listOfColleges[index]}')
# # for college in listOfColleges:
# #     print(f'College #{listOfColleges.index(college) + 1}')
# #     print(f'Name: {college}')

'''Using sum for averages'''

# rainfallAmts = [0.8, 1.1, 1.3, 2.1, 1.2, 0.2, 7.6]
# totalRain = 0.0
# for index in range(len(rainfallAmts)):
#     totalRain += rainfallAmts[index]
# avgRain = totalRain /len(rainfallAmts)
# print(f'Total rain = {totalRain:.2f} and Avg. rain = {avgRain:.2f}\n')
#
# total_rain2 = sum(rainfallAmts)
# avg_rain2 = sum(rainfallAmts) / len(rainfallAmts)
# print(f'Total rain = {total_rain2:.2f} and Avg. rain = {avg_rain2:.2f}')

'''Longhand for individual items'''

# numbers = [1,2,3,4,5,6,7,8,9,10]
# for index in range(len(numbers)):
#     squared = numbers[index]**2
#     print(f'{numbers[index]:>2d} squared is {squared:>3d}')

'''Adding items to a list .append()'''

# villians = ['Catwoman', 'Darth Vader', 'Sauron']
# villians.append('Magneto')
# print(villians)

'''Initializing lists'''
# emptyList = []
# print(emptyList)
# emptyList.append('ata!')
# print(emptyList)

'''Adding items to a list and print trick'''
''' Use a Loop to better control printing'''

# print('Welcome to the Guest List Builder')
# guests = []
# while True:
#     newGuest = input('Type name & enter (hit enter twice to quit: ')
#     if newGuest == '':
#         break
#     else:
#         guests.append(newGuest)
#     for index in range(len(guests)):
#         if index < len(guests) - 1:
#             print(f'Guest #{index + 1} is {guests[index]}, ', end='')
#         else:
#             print(f'and Guest #{index + 1} is {guests[index]}.')
# print(guests)
# print(*guests, sep= ', ')

'''Formatting options for lists '''

# print('Welcome to the Guest List Builder')
# guests = []
# while True:
#     newGuest = input('Type name & enter (hit enter twice to quit): ')
#     if newGuest == '':
#         print()
#         break
#     else:
#         newGuest = newGuest.title()
#         guests.append(newGuest)
# print('{:<30}{:>7}'.format('Guest Name', 'Ticket'))
# for index in range(len(guests)):
#     print('{:<30}{:>2}{:>5}'.format(guests[index],'#', index + 10001))
# print('{:.<30}{:.>7}'.format('Total',len(guests)))

'''The list() function'''

# numbers = list(range(1,10))
# print(numbers)
# print(*numbers, sep=', ')
#
# letters = list('Hennipen')
# print(letters)
# print(*letters, sep=', ')
#
# emptyList = list()
# print(emptyList)

'''In operator works w/ lists'''
# villians = ['Catwoman', 'DarthVader', 'Sauron', 'Lex Luther', 'Magneto']
# if 'Darth Vader' in villians:
#     print('Darth Vader is in the list')
# else:
#     print('Darth Vader is NOT in the list')

'''Adding lists together'''
# myBands = ['Prince', 'Daft Punk', 'Led Zeppelin']
# friendsBands = ['Lady Gaga', 'Rhianna', 'Beyonce']
# roadtripPlaylist = myBands + friendsBands
# print(*roadtripPlaylist, sep=', ' )

'''Remove VS Pop VS Delete'''
# #Removes last guest added
# print(guests)
# uninvited = guests.pop()
# print('Name removed: ', uninvited)
# print('Guest list: ', guests)
#
# #Removes guest in specific position
# print(guests)
# nixedSecondGuest = guests.pop(1)
# print('Name removed: ', nixedSecondGuest )
# print('Guest list: ', guests)
#
# #removes specific guest
# if 'Sauron' in guests:
# 	guests.remove('Sauron')
# else:
# 	print('No such guest.')
# print('Guest list: ', guests)

'''Sort method'''
# rainfallAmts = [0.8, 1.1, 1.3, 2.1, 1.2, 0.2, 7.6]
# rainfallAmts.sort()
# print(rainfallAmts)

'''Copying a list or just a slice'''
# data = [7, 8, 9, 10]
# copyOfData = data[:] #: by it self means range is all data
# print(copyOfData)
# copyOfData.remove(8)
# print(data)
# print(copyOfData)

'''Aliasing'''
#Does not make a copy. The two variables are now equal so changing one changes the other
# data = [7, 8, 9, 10]
# aliasOfData = data
# print(aliasOfData)
# aliasOfData.remove(8)
# print(data)
# print(aliasOfData)
#
# '''Loop-2list'''
#
# import re
#
# def main():
#     small, large = input1()
#     counter, total = processing1(small, large)
#     output1(counter, total)
#
# def input1():
#     userList = []
#     redux = re.compile(r'\d+')
#     print('Enter a small number to begin counting.')
#     small = input('\tEnter a whole number: ')
#     mo = redux.search(small)
#     while mo == None and small:
#         small = input('Please enter only whole numeric values: ')
#         mo = redux.search(small)
#     small = int(small)
#     print(f'Enter a number larger than {small}.')
#
#     large = input('Enter a whole number: ')
#     mo = redux.search(large)
#     while mo == None:
#         large = input('Please enter only whole numeric values: ')
#         mo = redux.search(large)
#
#     large = int(large)
#     return small, large
#
# def processing1(small, large):
#     counter = list(range(small, large+1))
#     total = 0
#     for numbers in range(small, large+1):
#         total += numbers
#     return counter, total
#
# def output1(counter, total):
#     print('Here is the number list printed w/ shortcuts:')
#     print(*counter, sep= ', ')
#     print('Here is the number list printed via a loop:')
#     print('You counted: ', end='')
#     print(*counter, sep=' + ', end= '')
#     print(' = 'f'{total}')
# #Find actual loop way to do this!!!!!!

# main()

'''Average quiz score 2'''
import re

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
    regex = re.compile(r'\d+')
    print('How many students are taking quizzes?')
    student_number = input('\tEnter a positive whole number: ')
    mo = regex.search(student_number)
    while mo == None:
        student_number = input('\tEnter a positive whole number: ')
        mo = regex.search(student_number)
    student_number = int(student_number)
    print('How many quizzes will each take?')
    quiz_num = input('\tEnter a positive whole number: ')
    mo = regex.search(quiz_num)
    while mo == None:
        quiz_num = input('\tEnter a positive whole number: ')
        mo = regex.search(quiz_num)
    quiz_num = int(quiz_num)

    return student_number, quiz_num


def processing1(student_number, quiz_num):
    total_all = int(0)
    list_of_all = []
    for student in range(student_number):
        print(f'Quiz information for student #{student+1}.')
        score_list = []

        total_points = 0
        avg_points = 0
        for quiz in range(quiz_num):
            print(f'Score for quiz #{quiz+1}:')
            score = input('\tEnter a whole positive number: ')
            score_list.append(score)
            total_points = int(total_points)
            score = int(score)
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