'''Author: Thomas Mullins
Date: 2/7/19
grade.py
Definition: Develop a program to calculate quiz grade data in clean and friendly way '''
#score = int(input('Enter quiz score: '))
#if score >= 90:
#	print('Grade: A')
#elif score >= 80:
#	print('Grade: B')
#elif score >= 70:
#	print('Grade: C')
#elif score >= 60:
#    print('Grade: D')
#elif score >= 50:
#    print('Grade: F')


score = input('Enter quiz score – whole number 0-100: ')
# validation block
if score.isnumeric() is False:
	print('Try the program again; it only takes whole numbers.')
else: #Exists on the line by itself for all intents and purposes
    score = int(score)
    if score >= 90: #Tested
        print('You got an A!\nExcellent Work!')
    elif score >= 80: #Tested
        print('You\'ve earned a B!\nWell Done!')
    elif score >= 70: #Tested
        print('You have earned a C\nWelcome to the middle of the pack.')
    elif score >60: #Tested
        print('Grade: D\nYou have passed this course.')
    else: #No grade F script required beyond this #Tested
        print('You have received an F for this course.\nBetter luck this summer!')
