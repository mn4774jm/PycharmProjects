'''Team1.py The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''
import random

strategy_name = 'Helen, Marty counter,random'

# def counter_strat(my_hist,their_hist):
#     if len(their_hist) == 0:
#         choice = 'p'
#     elif beat_move(my_hist[-1]) == beat_move(my_hist-2) and beat_move(my_hist[-3]) == beat_move(my_hist-4):
#         choice = random.choice(['r','p','s'])
#     else:
#         if len(my_hist)%2 == 0:
#             choice='p'
#         else:
#             choice = 'r'
#     return choice
#
#
# def beat_move(move):
#     if move=='r':
#         return 'p'
#     if move == 'p':
#         return 's'
#     if move=='s':
#         return 'r'
#
# def move_history(my_history, their_history):
#     '''This player always starts with rock
#     '''
#     if len(their_history)<2:
#         return 'r'
#     if their_history[-1]==their_history[-2]:
#         return beat_move(their_history[-1])
#     return random.choice(['r','p','s'])
#
#
#
# def move(my_history, their_history):
#     '''This player beats its opponent's last move.
#
#     Returns whatever would beat their last move, either 'r', 'p', or 's'.
#     If there was no last move, returns 'r'.
#     '''
#     if len(their_history) == 0:
#         my_move = 'r'
#     else:
#         prediction = their_history[-1]
#         my_move = beat_prediction(prediction)
#     return my_move
#
#
# def beat_prediction(prediction):
#     '''prediction is a string of one character: r, p, or s
#     returns 'r', 'p', or 's'
#     '''
#     if prediction == 'r':
#         winning_move = 'p'
#     elif prediction == 'p':
#         winning_move = 's'
#     elif prediction == 's':
#         winning_move = 'r'
#     else:
#         winning_move = ''
#         print('Error in beat_prediction(): prediction was not r, p, or s.')
#     return winning_move
#
# def counter_strat(my_hist,their_hist):
#     if beat_move(my_hist[-1]) == beat_move(my_hist-2) and beat_move(my_hist[-3]) == beat_move(my_hist-4):
#         choice = random.choice(['r','p','s'])
#     else:
#         choice = 'p'
#     return choice

def move(my_history, their_history):
    if len(my_history)==0:
        pick = 'r'
    elif len(my_history)%2 == 0:
        pick = 'p'
    else:
        pick = 'r'
    return pick

""" 
spspssrprprrppppspps

sppspprsrrsrsrspsrss

"""