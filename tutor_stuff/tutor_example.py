# import re #import the library required for the function
#
# repeat = True
# while repeat:
#     name = input('Enter your first name')
#     # create a pattern to search
#     nameRegex = re.compile(r'^[a-zA-Z]+$')
#     # use search function on variable to ask for a return value
#     name_found = nameRegex.search(name)
#
#     # loop for validation
#     while name_found is None:
#         name = input('please enter your first name').title()
#         name_found = nameRegex.search(name)
#     print(f'your name is {name}')
#     again = input("would you like to try again? enter Y or N: ").upper()
#     while again != "Y" and again != "N":
#         again = input("Please enter only Y or N: ").upper()
#
#     if again == "N":
#         repeat = False
# print("Thanks for using the program!")


# nameRegex = re.compile(r'[a-zA-Z]')
'''
( = open parentheses
) = close parentheses
[ = open bracket
] = close bracket
'' = single quote
"" = double quote
'''

# basic MIPO (Main, Input, Processing, Output) template


def main():
    # this is exception handling; if the program does something
    # unexpected, error-wise, this stops the program from crashing
    try:
        # this is where you group your function calls and returned values
        word, number = inputs()
        word_length, num_length = processing(word, number)
        outputs(word, word_length, num_length, number)
    # end of exception handling
    except Exception as err:
        print(err)


def inputs():
    word = input('Write a word, please: ').strip()
    while word.isnumeric() or word == '':
        word = input('Please try again. Only letters will be accepted: ')
    number = input('Now enter a number(s): ')
    while not number.isnumeric():
        number = input('Almost! Try numbers though: ')
    return word, number


def processing(word, number):
    word_length = len(word)
    num_length = len(number)
    return word_length, num_length


def outputs(word, length, num_length, number):
    print(f'You decided to enter {word}. It is {length} characters long.')
    print(f'You also chose to enter the number {number}. It is {num_length} digits long')


main()

