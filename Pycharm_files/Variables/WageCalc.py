'''Author: Thomas Mullins
Date: 1/24/19
Definition: Wages for 40 hours plus ten hours of overtime
'''
regularWage=float(15.34)
overtimeWage=(regularWage*float(1.5))
totalWages=((regularWage*40)+(overtimeWage*10))
#print(totalWages)
print('Regular Wages', format(regularWage, '12.2f'))
print('Overtime Wage', format(overtimeWage, '12.2f'))
print('Total Wages', format(totalWages, '14.2f'))



