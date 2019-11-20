'''team5.py The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''

strategy_name = 'BeatLastMove2'

def move(my_history, their_history):
    '''This player beats its opponent's last move.
    
    Returns whatever would beat their last move, either 'r', 'p', or 's'.
    If there was no last move, returns 'r'.
    '''
    if len(their_history)==0:
        my_move = 'r'
    else:
        prediction = their_history[-1]
        my_move = beat_prediction(prediction)
    return my_move
    

        
def beat_prediction(prediction):
    '''prediction is a string of one character: r, p, or s
    returns 'r', 'p', or 's'
    '''
    if prediction =='r':
        winning_move = 'p'
    elif prediction == 'p':
        winning_move = 's'
    elif prediction == 's':
        winning_move = 'r'
    else:
        winning_move = '' 
        print('Error in beat_prediction(): prediction was not r, p, or s.')
    return winning_move