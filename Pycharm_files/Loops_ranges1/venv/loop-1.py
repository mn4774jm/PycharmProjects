'''Author: Thomas Mullins
Date: 2/14/19
loop-1.py
Definition: For each item below, include print statements that say what each loop is doing.'''

#Header
print('These are the numbers from 0 through 5')
for count in range(0,6): # #Starts at 0 ends at 5, 6 acts as a cap
	print(f'{count}')

#Header
print('These are the numbers from 1 through 20')
for count in range(1,21): #Starts at 1 not 0
	print(f'{count}')

#Header
print('These are the even numbers from 0 through 24')
for count in range(0, 25, 2):# even requires step argument at end
    print(f'{count}')

#Header
print('These are the odd numbers from 37 through 53')
for count in range(37, 54, 2): #Must start at 37, 2 used to jump to next odd
    print(f'{count}')

#Header
print('Write a loop that prints 10, 20, 30, 40, 50, 60')
for count in range(10, 61, 10): #Step argument of 10, 61 in center to stop at 60
    print(f'{count}')

#Header
print('Write a loop counting down from 30 through 20')
for count in range(30, 19, -1):#Negative value still functions as int
    print(f'{count}')



