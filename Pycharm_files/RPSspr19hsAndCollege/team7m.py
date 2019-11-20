'''team7.py The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''

import random

strategy_name = 'Henry and Chou\'s Ol Reliable'

def move(my_history, their_history):
    if len(my_history)==0:
        my_move = 'p'
    elif len(my_history)%2 == 0:
        my_move = 's'
    else:
        my_move = random.choice(['r', 'p', 's'])
    return my_move