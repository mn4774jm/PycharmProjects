""" Dylan and Austin 5/14/19 We took team1's strategy and made it more Random. We also tried an anti-team4 strategy but it didn't work.
"""
import random

strategy_name = 'DS & AP random Beat'       
                     
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
        return random.choice(['r', 'p', 's'])
    if their_history[-1]==their_history[-2]:
        return beat_move(their_history[-1])
    if my_history[-1]==my_history[-2] and their_history[-1]!=their_history[-2]:
        return random.choice(['r', 'p', 's'])
    # if len(their_history)<4:
    #     if their_history[-1]==their_history[-3]:
    #         return beat_move(their_history[-1])
    #     elif their_history[-2]==their_history[-4]:
    #         return beat_move(their_history[-2])
    #     else:
    #         return random.choice(['r','p','s'])
    return random.choice(['r','p','s'])