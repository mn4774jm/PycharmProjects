"""
team8.py The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
"""
import random

strategy_name = 'Deanna&Andrew-Team8'


def random_move():
    pick = random.choice(['r', 'p', 's'])
    return pick


def move(my_history, their_history):
    if len(my_history)<2:
        my_move = 'p'
    elif len(my_history)%3== 0:
        my_move = 'r'
    else:
        if my_history[-1] == their_history[-2]:
            my_move = their_history[-1]
        elif their_history[0] == their_history[-2]:
            my_move = their_history[0]
        else:
            my_move = random_move()
    return my_move
