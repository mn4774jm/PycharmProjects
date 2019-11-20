'''team4.py The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''
strategy_name = 'RockEarlyPaperEvenRandomOdd'
import random

def random_move():
    pick = random.choice(['r', 'p', 's'])
    return pick
    
def move(my_history, their_history):
    if len(my_history)<5:
        my_move = 'r'
    elif len(my_history)%2 == 0:
        my_move = 'p'
    else:
        my_move = random_move()
    return my_move
    
        