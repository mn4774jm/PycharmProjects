def main():
    while True:
        try:
            length, width, height, unit = input1()
            #getPosint()
            area = processing1(length, width, height)

            output1(area, unit)
        except Exception as err: #General exception end
            print(err)

        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank you for using the program.')
            break

def input1():
    #length =0
    #height = 0
    #width = 0
    unit = input('What unit of measurement are you using? in, cm, etc. ')
    length = float(input('Enter length? '))

    width = float(input('What is the width? '))

    height = float(input('What is the height? '))



    return length, width, height, unit
1
def processing1(length, width, height):
    area = 0
    area = length * width * height
    return area

def output1(area, unit):
    print(f'The volume og the box is: {area}{unit}.')

main()


