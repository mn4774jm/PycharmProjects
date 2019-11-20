

print('\nWelcome to the Scrabble Calculator. Let\'s do this!')


def main():
    # while True:
    #     try:
    player_list = input1()
    player_1_score, player_2_score, player_dict = input2(player_list)
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
    player_list = []
    #player_numb = getPosint()
    player_numb = 2
    for i in range(player_numb):
        player = input(f'Enter player #{len(player_list) + 1}\'s name: ').title()
        player_list.append(player)
    return player_list

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tHow many players?: ')
    while posInt.isnumeric() is False or int(posInt) <= 0:
        posInt = input('\tPlease enter a whole number, greater than 0: ')
    posInt = int(posInt)
    return posInt

def input2(player_list):
    player_dict = {}
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
                    player_dict.update({player_list[0]:player_1_score})
                    print(player_dict[turn])
                else:
                    game_is_playing = False

            else:
                score = input(f'Enter score for {turn}\'s turn.\n\tPress enter twice to end:')
                if score != '':
                    while score.isnumeric() is False or int(score) < 0:
                        score = input('\tPlease enter a whole number: ')
                    score = int(score)
                    player_2_score.append(score)
                    player_dict.update({player_list[1]: player_2_score})
                    print(player_dict[turn])
                    turn = player_list[0]
                else:
                    game_is_playing = False
        return player_1_score, player_2_score, player_dict


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
    print('Final Tally!:')
    for i in range(len(player_list)):
        print(f'Final details for {player_list[i]}:')
        print(f'Score List: {player_dict[player_list[i]]}')
        print(f'With a final total score of {dict_final[player_list[i]]} and a high single play score of '
              f'{dict_max[player_list[i]]}!')

main()