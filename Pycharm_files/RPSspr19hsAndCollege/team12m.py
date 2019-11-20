'''Team1.py The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''
import random

strategy_name = 'Shane Ivan Hanna- Kick rocks Explosion - not running'

history ={'r':0,'p':0,'s':0}

percent_variable = 30


def beat_move(move):
        if move == 'r':
            history['r']= +1
            opponent = history_process(history)
            if opponent > 15:
                return 'p'

        if move == 'p':
            history['p']= +1
            opponent = history_process(history)
            if opponent > 15:
                return 's'

        if move=='s':
            history['s']= +1
            opponent = history_process(history)
            if opponent > 15:
                return 'r'

def move(my_history, their_history):
    '''This player always starts with rock
    '''
    if len(their_history)<2:
        return 'r'
    if their_history[-1]==their_history[-2]:
        return beat_move(their_history[-1])

    return random.choice(['r','p','s'])

def history_process(history):
    sum = 0
    for i in history.values():
          sum += i
          percent = int(sum/3)
          return percent
