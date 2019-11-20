'''Author: Thomas Mullins
Date:2/10/19
colorMixer.py
Definition: Write a program that asks the user to enter a 1st color choice from a set of options
:red, yellow, or blue, and then asks them to enter a second color choice from the remaining 2.'''

#Variables
#color1 = First primary color choice
#color2 = second primary color choice

print('What happens when you mix two different colors?') #Header
color1 = input('Enter a primary color - red, blue, or yellow:')
color2 = input('Enter a second primary color that is different from the first:')
if (color1 == 'red' and color2 =='blue') or (color1 == 'blue' and color2 == 'red'): #Purple combinations
    print('Red and Blue combine to make Purple!')
elif (color1 == 'Red' and color2 == 'Blue') or (color1 == 'Blue' and 'Red'): #additional combos to avoid user errors
    print('Red and Blue combine to make Purple!')
elif (color1 == 'Red' and color2 == 'blue') or (color1 == 'blue' and 'Red'): #additional combos to avoid user errors
    print('Red and Blue combine to make Purple!')
elif (color1 == 'red' and color2 == 'Blue') or (color1 == 'Blue' and 'red'): #additional combos to avoid user errors
    print('Red and Blue combine to make Purple!')

elif (color1 == 'yellow' and color2 == 'red') or (color1 == 'red' and color2 == 'yellow'): #orange combinations
    print('Red and Yellow combine to make Orange!')
elif (color1 == 'Yellow' and color2 == 'Red') or (color1 == 'Red' and color2 == 'Yellow'): #additional combos
    print('Red and Yellow combine to make Orange!')
elif (color1 == 'yellow' and color2 == 'Red') or (color1 == 'Red' and color2 == 'yellow'): #additional combos
    print('Red and Yellow combine to make Orange!')
elif (color1 == 'Yellow' and color2 == 'red') or (color1 == 'red' and color2 == 'Yellow'): #additional combos
    print('Red and Yellow combine to make Orange!')

elif (color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and 'blue'): #green combinations
    print('Blue and Yellow combine to make Green')
elif (color1 == 'Blue' and color2 == 'Yellow') or (color1 == 'Yellow' and 'Blue'): #additional combos
    print('Blue and Yellow combine to make Green')
elif (color1 == 'blue' and color2 == 'Yellow') or (color1 == 'Yellow' and 'blue'): #additional combos
    print('Blue and Yellow combine to make Green')
elif (color1 == 'Blue' and color2 == 'yellow') or (color1 == 'yellow' and 'Blue'): #additional combos
    print('Blue and Yellow combine to make Green')

else:
    print('Sadly, you did not input two different primary colors, or maybe no primary colors at all. \nThis is why we can\'t have nice things.')
print('The primary colors combine to make three secondary colors!')
