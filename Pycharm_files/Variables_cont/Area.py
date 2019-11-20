'''Author: Thomas Mullins
Date: 2/3/19
Area.py
Definition: Write a program to gather user input to calculate the area of a rectangle'''

#Variables
measure=str(input('What is your measurement unit? (in., ft,. cm., etc.)'))
length=float(input(f'What is the length of the rectangle in {measure}?'))
width=float(input(f'What is the width of the rectangle in {measure}?'))
area=length*width

#Header
print('\n')
print('Welcome to Rectangle Area Calculator!')
#script
#print(measure)
#print(length)
#print(width)
print(f'Your rectangle is{area: 0.2f} square {measure}!')

