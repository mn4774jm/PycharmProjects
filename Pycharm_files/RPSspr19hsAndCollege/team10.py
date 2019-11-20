'''Team10.py The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''
import random, statistics

strategy_name = 'Bock vs. Godzilla'

# my_history = ''
# their_history = 'rpsrpsrprp'


def move(my_history, their_history):
    my_play = ''
    counter_list = []
    if len(their_history) < 3:
        my_play = random.choice(['r','p','s'])
    else:
        count_r = their_history.count('r')
        count_p = their_history.count('p')
        count_s = their_history.count('s')
        if count_r > count_p and count_r > count_s:
           my_play = 'p'
        elif count_p > count_r and count_p > count_s:
           my_play = 's'
        elif count_s > count_r and count_s > count_p:
           my_play = 'r'
        else:
            counter_list = [count_r,count_p,count_s]
            counter_list.sort()
            if counter_list[0] == counter_list[1] == counter_list[2]:
                my_play = random.choice(['r','p','s'])
            elif counter_list[1] and counter_list[2] in [count_r,count_p]:
                my_play = random.choice(['p','s'])
            elif counter_list[1] and counter_list[2] in [count_r,count_s]:
                my_play = random.choice(['p','r'])
            elif counter_list[1] and counter_list[2] in [count_p,count_s]:
                my_play = random.choice(['s','r'])
            else:
                my_play = random.choice(['r','p','s'])
        # print(my_play)
        # print(counter_list)   
    return my_play
    
# move(my_history,their_history)

    