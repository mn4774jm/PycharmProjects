'''Author: Thomas Mullins
Date: 2/22
mipo.py
Definition: Write a program to ask for user input to find the volume of a cube'''


print('Welcome to the Volume Calculator')

#define main program block
def main():
    #Exception start
    try:
        #Collect input for length, width, and height
        length=float(input('Enter length: '))
        width= float(input('Enter width: '))
        height=float(input('Enter height: '))

        #call calculateVolume from next def
        calculateVolume(length,width,height)

        #ask for input for repeat
        answer = input('Would you like to use the program again? Y/N:')

        #start of if loop for y/n
        if answer == 'N' or answer == 'n':
            print('Thank you for using the program')
        #statement to repeat
        elif answer == 'Y' or answer =='y':
            print('----------------------')
        # main called again for 'y' answer
            main()

    except Exception as err:
        print('Please use only numerical values')

def calculateVolume(length1,width1,height1):
    volume=length1*width1*height1
    print(f'The volume of your box is {volume: 0.2f}')

main()

