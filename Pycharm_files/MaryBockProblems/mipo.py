def main():
    while True:
        try:

            length, width, height, unit = input1()
            volume = processing1(length, width, height)
            output1(length, width, height,volume, unit)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ').upper()
        while answer != 'Y' and answer != 'N':
            answer = input('Please enter Y or N: ').upper()
        if answer == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print("Welcome to the volume calculator")
    unit = input('Please enter a unit of measurement (ft., in., etc.): ')
    print('Enter length')
    length = getPosint()
    print('Enter width ')
    width = getPosint()
    print('Enter length')
    height = getPosint()
    return length, width, height, unit

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False or posInt == 0:
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

def processing1(length, width, height):
    volume = length * width * height
    return volume

def output1(length, width, height, volume, unit):
    print(f'\nStatistics (in {unit}):')
    print('{:<10}{:>5}'.format('Length', length))
    print('{:<10}{:>5}'.format('Width', width))
    print('{:<10}{:>5}'.format('Height', height))
    print(f'The volume of your cube is {volume} {unit}')

main()
