'''Improvements: 1) Modify player input block to use a loop ? '''

print(f'\n{"-"*20} "Nice" Mode Engaged {"-"*21}\n')
import re

def main():
    while True:
        try:
            player_list,player_1_score, player_2_score, player_3_score, player_4_score, player_dict = input1()
            dict_final, dict_max = processing1(player_list, player_dict)
            output1(player_list, player_dict, dict_final, dict_max)
        except Exception as err:
            print(err)
        answer = input('\nWould you like to rumble again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank you for using the program')
            exit()

def input1():
    #Initialize dicts and list
    player_dict = {}
    player_list = []
    player_1_score = []
    player_2_score = []
    player_3_score = []
    player_4_score = []
    #Ask for player input with validation
    player_numb = getPosint()
    for i in range(player_numb):
        #Player input for names and stored to player_list
        player = input(f'Enter player #{len(player_list) + 1}\'s name: ').title()
        player_list.append(player)
    print('\nPress the Enter key twice to end the game or\nPress ? to consult the dictionary.\n')
    #begin infinate conditional loop
    while True:
        game_is_playing = True
        turn = player_list[0]
        while game_is_playing:
            score = input(f'Enter score for {turn}\'s turn: ')
            if score == '?':
                dictionary_mode()
            elif score != '':
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

def getPosint():
    posInt = input('\nHow many players?: ')
    print()
    while posInt.isnumeric() is False or int(posInt) < 2 or int(posInt) > 4:
        posInt = input('\tPlease enter a whole number between 2 and 4 players: ')
    posInt = int(posInt)
    return posInt

def dictionary_mode():
    start = open('scrabblewords.txt', 'r')
    scrabble_words = start.read()
    print(f'\n{"-"*25} Dictionary {"-"*26}\n')
    shade = input('Enter word you would like to check: ').upper()
    word_regex = re.compile(f'{shade}')
    mo = word_regex.search(scrabble_words)
    shade_fixed = shade.title()
    if mo == None:
        print(f'Oops... Looks like {shade_fixed} isn\'t a word.\n')
    else:
        print(f'Congrats, {shade_fixed} is indeed a word.\n')
        start.close()
    return

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
    print(f'\n{"-"*20} Final Tally! {"-"*20}')
    print('{:<20}{:>15}{:>10}'.format('Player Name', 'Max', 'Total'))
    for i in range(len(player_list)):
        print('{:<15}{:>20}{:>10}'.format(player_list[i], dict_max[player_list[i]], dict_final[player_list[i]]))
        print(f'Score List: {player_dict[player_list[i]]}\n')

main()

if turn == player_list[0]:
    player_1_score.append(score)
    player_dict[player_list[i]] = score
    print(player_dict.items())


elif turn == player_list[1]:
    player_2_score.append(score)
    player_dict[player_list[1]] = score
    print(player_dict[turn])
    if len(player_list) == 2:
        turn = player_list[0]
    else:
        turn = player_list[2]