'''Team8.py The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''
import random

strategy_name = 'Jacques & Zaka Beat next to last move'

def beat_move(move):
    if move=='r':
        return 'p'
    if move == 'p':
        return 's'
    if move=='s':
        return 'r'

def move(my_history, their_history):
    '''This player always starts with rock
    '''
    if len(their_history)<2:
        return 'r'
    if their_history[-2]==their_history[-2]:
        return beat_move(their_history[-2])
    return random.choice(['p','r','s'])
    
  