'''Thomas Mullins
area.py
Def: Take user data for length, width, and units to calculate a return area data
6/6/19'''

def main():
    while True:
        try:

            unit, length, width=input1()
            area=processing1(length, width)
            output1(unit, area)

        except Exception as err:
            print(err)

        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('\nWelcome to the Rectangle Area Calculator!')
    unit = input('What is your measurement unit? (in., ft., cm., etc) ')
    print(f'What is the length of the rectangle in {unit}? ')
    length = float_regex()
    print(f'What is the width of the rectangle in {unit}? ')
    width = float_regex()
    return unit, length, width

def float_regex():
    import re
    floatRegex = re.compile(r'\d+(\.)?(\d+)?')
    regex = input('\tEnter a numeric value: ')
    mo = floatRegex.search(regex)
    while mo == None or float(regex) < 0:
        regex = input('\tEnter only positive numeric values: ')
        mo = floatRegex.search(regex)
    regex = float(regex)
    return regex

def processing1(length, width):
    area = length*width
    return area

def output1(unit, area):
    print(f'Your rectangle is {area:,.2f} square {unit}.')

main()