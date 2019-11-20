'''Team9.py The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''
#Sol and Devon, This will be the best one ever!!!
#The first couple of turns are random. Then it predicts RPS after around those turns.

import random
strategy_name = 'Sol & DR BeatPredict2'

def beat_move(move):
    if move=='r':
        return 'p'
    if move == 'p':
        return 's'
    if move=='s':
        return 'r'

def move(my_history, their_history):
    '''This is random
    '''
    if len(their_history)<4:
        return random.choice(['r','p','s'])
    if their_history[-2]==their_history[-4]:
        return beat_move(their_history[-2])
    return random.choice(['r','p','s'])
    