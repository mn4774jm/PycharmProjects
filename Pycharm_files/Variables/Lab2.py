'''Author: Thomas Mullins
Date: 1/24/19
Definition: Lab2'''
numberOfCds=45
numberOfLps=23
numberOfAlbums=numberOfCds+numberOfLps
print(numberOfAlbums)
college='MC' # Python IDs this as a string variable
numberOfCds=3 #Python IDs this as an integer variable
print('hello world')
#myName=Tom
#myname!=myName
total = 1000
#print('Total wages = $' + total) # this line errors
#There are two common ways to combine numerical data and strings in a print statement:
print('Total wages = $' + str(total)) # OR
print('Total wages = $', total)
# Use format() function inside the print() function to control the look.
print(format(12345.6789, '.1f'))
print(format(12345.6789, '.2f'))

# Add comma separators:
print(format(12345.6789, ',.2f'))

# Specify the minimum column width:
print(format(12345.6789, '12.2f'))
num1 = 123.456
num2 = 1.2345
num3 = 123456.56789
print('Number 1', format(num1, '12.2f'))
print('Number 2', format(num2, '12.2f'))
print('Number 3', format(num3, '12.2f'))
# Try this code to format a floating point number as a percent:
print(format(0.5, '%'))
print(format(0.5, '.0%'))
print(format(0.5, '.2%'))
# You can also use the format() function to work with an integer:
print (format(123456, '10,d'))
