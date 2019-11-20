# """
# Generate random numbers for the user
# Emulate rolling a dice, until user wants to quit
# Uses f-strings also known as format strings
# """
#
# import random
#
# want_to_quit = ''
#
# while not want_to_quit:
#     dice_value = random.randint(1, 6)
#     print(f'You rolled a {dice_value}')
#     want_to_quit = input('Press enter to roll again, any other key to quit ')


correct = input("what is the capital of wisconson ?")
answer = "madison"
attempt_counter = 1

while attempt_counter < 3 and correct != answer:
    attempt_counter += 1
    correct = input("Sorry, please try again: ")
if correct == answer:
    print(f'congratulations! The correct answer is {answer} and it took you {attempt_counter} attempts')
else:
    print(f'I\'m sorry but the correct answer is {answer}')







