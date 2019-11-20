import random


strategy_name = 'Yankuba & Ben Winning Strategy'


def move(my_history, their_history):
    if len(their_history) == 0:
        return random_move()
    else:
        my_last = my_history[-1]
        their_last = their_history[-1]
        if my_last == 'r':
            if their_last == 'p':  # Lost
                return 's'  # Play what would've beat their last
            elif their_last == 's':  # Win
                return 'p'  # Play what would've beat our last
            else:  # Tie
                return random_move()  # Random

        elif my_last == 'p':
            if their_last == 's':  # Loss
                return 'r'  # Play what would've beat their last
            elif their_last == 'r':  # Win
                return 's'  # Play what would've beat our last
            else:
                return random_move()  # Random

        elif my_last == 's':
            if their_last == 'r':  # Loss
                return 'p'  # Play what would've beat their last
            elif their_last == 'p':  # Win
                return 's'  # Play what would've beat our last
            else:
                return random_move()  # Random

        else:
            return random_move()


def random_move():
    pick = random.choice(['r', 'p', 's'])
    return pick  # Return random choice
