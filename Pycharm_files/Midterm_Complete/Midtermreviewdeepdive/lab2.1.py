'''temp = float(input('Enter the temperature: '))
if temp > 0:
    print(f'The temperature {temp}f is greater than 0 – thankfully!')
elif temp == 0:
    print('The temperature is exactly 0!')
else:
    print(f'The temperature {temp}f is less than 0 - brrr!')
print('That\'s all folks!')'''

#Apollo

'''year = int(input('What year did Apollo 11 land on the moon? '))
if year != 1969:
	print(f'Sorry, {year} is the wrong answer.')
else:
	print(f'Correct! {year} is right!')'''

#Grade.py

'''score = input('Enter quiz score – whole number 0-100: ')
# validation block
if score.isnumeric() is False:
	print('Try the program again; it only takes whole numbers.')
else:
    score = int(score)
    if score >= 90:
        print('Grade: A')
    elif score >= 80:
        print('Grade: B')
    elif score >= 70:
        print('Grade: C')
    elif score >= 60:
        print('Grade: D')
    elif score >=0:
        print('Grade: F')
    else:
        print('Your grade is currently undefined.')'''

#if-1.py

pennies = input('Enter the number of pennies in the jar: ')
if pennies.isnumeric() is False:
    print('Please enter only whole numeric numbers')
else:
    if pennies <=0:
        print('Looks like you don\'t have any pennies, friend.')
    elif pennies == 100:
        print('You have exactly one dollar.')
    else:
        print(f'You have ${pennies: .2f} in pennies.')
print('Thanks for using the program')

