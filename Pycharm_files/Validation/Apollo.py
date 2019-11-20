'''Author: Thomas Mullins
Date: 2/7/19
Apollo.py
Definition: Improve Apollo program by adding additional comments and custom feedback'''

#year = int(input('What year did Apollo 11 land on the moon? '))
#if year != 1969:
	#print(f'Sorry, {year} is the wrong answer.')
#else:
#	print(f'Correct! {year} is right!')

year = int(input('What year did Apollo 11 land on the moon? '))
if year == 1969:
	print(f'Correct! {year} is right!')
elif year == 1968: #Try to add range in the future
    print('So very close!')
elif year == 1970:
    print('Almost! Try a little lower.')
else: # No further data points required currently
	print(f'Sorry, {year} is the wrong answer.')
