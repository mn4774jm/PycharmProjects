'''Improvements: 1) find a way to modify for use with an infinate amount of players '''

print('\nWelcome to the Scrabble Calculator. Let\'s do this!')
def main():
    # while True:
    #     try:
    player_list,player_1_score, player_2_score, player_3_score, player_4_score, player_dict = input1()
    dict_final, dict_max = processing1(player_list, player_dict)
    output1(player_list, player_dict, dict_final, dict_max)
        # except Exception as err:
        #     print(err)
        # answer = input('\nWould you like to run this program again? Enter Y or N: ')
        # while answer.upper() != 'Y' and answer.upper() != 'N':
        #     answer = input('Please enter Y or N: ')
        # if answer.upper() == 'N':
        #     print(f'\nThank you for using the program')
        #     break

def input1():
    player_dict = {}
    player_list = []
    player_1_score = []
    player_2_score = []
    player_3_score = []
    player_4_score = []
    player_numb = getPosint()
    for i in range(player_numb):
        player = input(f'Enter player #{len(player_list) + 1}\'s name: ').title()
        player_list.append(player)
    while True:
        game_is_playing = True
        turn = player_list[0]
        while game_is_playing:
            score = input(f'Enter score for {turn}\'s turn.\n\tPress enter twice to end:')
            if score != '':
                while score.isnumeric() is False or int(score) < 0:
                    score = input('\tPlease enter a whole number: ')
                score = int(score)
                if turn == player_list[0]:
                    player_1_score.append(score)
                    player_dict.update({player_list[0]: player_1_score})
                    print(player_dict[turn])
                    turn = player_list[1]
                elif turn == player_list[1]:
                    player_2_score.append(score)
                    player_dict.update({player_list[1]:player_2_score})
                    print(player_dict[turn])
                    if len(player_list) == 2:
                        turn = player_list[0]
                    else:
                        turn = player_list[2]
                elif turn == player_list[2]:
                    player_3_score.append(score)
                    player_dict.update({player_list[2]:player_3_score})
                    print(player_dict[turn])
                    if len(player_list) == 3:
                        turn = player_list[0]
                    else:
                        turn = player_list[3]
                else:
                    player_4_score.append(score)
                    player_dict.update({player_list[3]:player_4_score})
                    print(player_dict[turn])
                    turn = player_list[0]
            else:
                game_is_playing = False
        return player_list, player_1_score, player_2_score, player_3_score, player_4_score, player_dict

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tHow many players?: ')
    while posInt.isnumeric() is False or int(posInt) <= 0 or int(posInt) > 4:
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

def processing1(player_list, player_dict):
    dict_final = {}
    dict_max = {}
    for i in range(len(player_list)):
        score = player_dict[player_list[i]]
        sum_score = sum(score)
        dict_final.update({player_list[i]:sum_score})

    for i in range(len(player_list)):
        score = player_dict[player_list[i]]
        sum_score = max(score)
        dict_max.update({player_list[i]: sum_score})
    return dict_final, dict_max

def output1(player_list, player_dict, dict_final, dict_max):
    print(f'\n{"-"*10}Final Tally!{"-"*10}')
    for i in range(len(player_list)):
        print(f'Final details for {player_list[i]}:')
        print(f'Score List: {player_dict[player_list[i]]}')
        print(f'With a final total score of {dict_final[player_list[i]]} and a high single play score of '
              f'{dict_max[player_list[i]]}!')

main()