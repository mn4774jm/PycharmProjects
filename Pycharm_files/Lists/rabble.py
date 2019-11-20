'''Author: Thomas Mullins
Date: 2/28/19
loops-2fun.py
Definition: Recreate the loops-2 using defs'''


#Header
print('Welcome to our counting program.\nIt also adds up the digits as you count!')

# Define main block
def main():
#exception start
    try:
        small, large = inputData()
        numberCount=calculations(small, large)

        output(numberCount)

    except Exception as err:
        print(err)

def inputData():
    small = input('Please enter a small number, 0 or higher: ')
    while not small.isnumeric() or int(small) < 0:

        print('Please enter a number larger than 0')
        small = input('Please enter a small number, 0 or higher: ')
    small = int(small)
    large = input('Now, enter a larger number that you want to count up to: ')
    while not large.isnumeric() or int(large) <= small:

        print('Please enter a number larger than your first entry')
    large = int(large)
    return small, large



def calculations(small, large):
    total=0
    x = small -1
    while x <= large -1:
        print(x+1)
        x=x+1
        total= x+total
        #print(f'The total number you counted is: {total}')
    return total


def output(total):
    print(f'The total number you counted is: {total}')

main()