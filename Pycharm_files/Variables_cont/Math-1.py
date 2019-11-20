"""Author: Thomas Mullins
Date:2/3/19
Math-1.py
Definition: Try out some math functions. Use online help and import math function"""

#Variables
#sqrt=(math.sqrt(2))
#header
print('Import Math')
import math
#Format will follow header - script - header - script pattern
# print("\nRounding Down") #math.trunc(x)
print(f'7.89 rounded down = {math.trunc(7.89):0.0f}')

# print('\nRound 54.345395 to 54.345')
print(f'54.345395 rounded to 3 decimal places = {54.345395:0.3f}')

# print('\nCalculate the square root of 2') #math.sqrt(x)
print(f'The square root of 2 = {math.sqrt(2)}')

# print('\nCalculate the sin of 7') #math.sin(x)
print(f'The sin Value of 7 = {math.sin(7)}')

# print('\nDisplay the Value of pi') #math.pi
print(f'The value of pi = {math.pi}')

# print('\nDisplay pi Rounded to 3 places')
print(f'The value of pi rounded = {math.pi:0.3f}')