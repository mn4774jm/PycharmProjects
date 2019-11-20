'''Thomas Mullins
color_mixer.py
Def: program that asks user to enter two primary colors and reports back what color the combo makes
6/6/19'''

def main():
    while True:
        try:
            color1, color2 = input1()
            output1(color1, color2)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ').upper()
        while answer != 'Y' and answer != 'N':
            answer = input('Please enter Y or N: ').upper()
        if answer == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('What happens when you mix two different primary colors?')
    print('Enter your first color')
    color1 = validation1()
    print('Enter a second color: ')
    color2 = validation1()
    return color1, color2

def output1(color1, color2):
    if color1 == 'red' and color2 == 'blue' or color1 == 'blue' and color2 == 'red':
        print(f'By mixing {color1} and {color2} you\'ve created purple!')
    elif color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red':
        print(f'By mixing {color1} and {color2} you\'ve created orange!')
    elif color1 == 'blue' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'blue':
        print(f'By mixing {color1} and {color2} you\'ve created green!')
    elif color1 == color2:
        print(f'As it turns out, if you combine {color1} and {color2} you get... well... {color1}. Good for you.')
    else:
        print('If you can see this you broke something. Bad dog! No cookie!')

def validation1():
    import re 
    valid_regex = re.compile(r'red|blue|yellow')
    regex = input('\tRed, Yellow, or Blue?:  ').lower()
    mo = valid_regex.search(regex)
    while mo == None:
        regex = input('Please enter only primary colors: ').lower()
        mo = valid_regex.search(regex)
    return regex

main()