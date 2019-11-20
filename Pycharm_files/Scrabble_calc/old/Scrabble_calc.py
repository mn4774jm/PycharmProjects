

print('\nWelcome to the Scrabble Calculator. Let\'s do this!')
def main():

    while True:
        try:
            player_list = input1()
            player_1_score, player_2_score = input2(player_list)
            player_1_final, player_2_final, player_1_max, player_2_max = processing1(player_1_score, player_2_score)
            output1(player_list, player_1_score, player_2_score, player_1_final, player_2_final, player_1_max, player_2_max)
        except Exception as err:
            print(err)
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank you for using the program')
            break

def input1():
    
    player_list = []
    for items in range(2):
        player = input(f'Enter player #{len(player_list)+1}\'s name: ')
        player_list.append(player)
    return player_list

def input2(player_list):
    player_1_score = []
    player_2_score = []
    turn = player_list[0]
    while True:
        game_is_playing = True
        while game_is_playing:
            if turn == player_list[0]:
                score = input(f'Enter score for {turn}\'s turn.\n\tPress enter twice to end:')
                if score != '':
                    while score.isnumeric() is False or int(score) < 0:
                        score = input('\tPlease enter a whole number: ')
                    score = int(score)
                    player_1_score.append(score)
                    turn = player_list[1]
                else:
                    game_is_playing = False
            else:
                score = input(f'Enter score for {turn}\'s turn.\n\tPress enter twice to end:')
                if score != '':
                    while score.isnumeric() is False or int(score) < 0:
                        score = input('\tPlease enter a whole number: ')
                    score = int(score)
                    player_2_score.append(score)
                    turn = player_list[0]
                else:
                    game_is_playing = False
        return player_1_score, player_2_score

def processing1(player_1_score, player_2_score):
    player_1_final = sum(player_1_score)
    player_1_max = max(player_1_score)
    player_2_final = sum(player_2_score)
    player_2_max = sum(player_2_score)
    return player_1_final, player_2_final, player_1_max, player_2_max

def output1(player_list, player_1_score, player_2_score, player_1_final, player_2_final, player_1_max, player_2_max):
    print('Final Tally!:')
    print(f'Final details for {player_list[0]}:')
    print(f'Score List: {player_1_score}')
    print(f'With a final total score of {player_1_final} and a high single play score of {player_1_max}!')

    print(f'\nFinal details for {player_list[1]}:')
    print(f'Score List: {player_2_score}')
    print(f'With a final total score of {player_2_final} and a high single play score of {player_2_max}!')

    if player_1_final > player_2_final:
        print(f'And the winner is.... {player_list[0]}!')
    elif player_1_final == player_2_final:
        print('And the winner is... Well fuck me, it\'s a tie!')
    else:
        print(f'And the winner is.... {player_list[1]}!')

main()