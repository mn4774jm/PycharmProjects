'''Requires scrabblewords.txt in the same folder as this program and an internet connection to run correctly'''

import webbrowser, re

print(f'\n{"-"*10} Welcome to the Scrabble Calculator v0.06 {"-"*10}\n')
def main():
    try:
        displayMenu()
        while True:
            command = input("Command: ").lower()
            if command == "start":
                game()
            elif command == "rules":
                webbrowser.open('https://scrabble.hasbro.com/en-us/rules')
            elif command == "exit":
                print("Thank you for using the program.")
                break
            else:
                print ("Not a valid command. Please try again.") #response if input not recognized

    except KeyError: #exception handling for ditionary issues
        print ("Key Error ")

def displayMenu(): #Define displayMenu to offer user options
    print ("Let's Do This!\nType one of the following options:\n")
    print ("Start  - Start the game")
    print ("Rules  - For when you came unprepared (Requires an internet connection)")
    print ("Exit   - For when you opened this by mistake")
    print()

def game():
    while True: # Function calls, exception handling, repeat option
        try:
            player_list, player_dict = input1()
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
    # Initialize dict and list
    player_dict = {}
    player_list = []

    # Ask for player input with validation
    player_numb = getPosint()
    for i in range(player_numb):
        #Player input for names and stored to player_list
        player = input(f'Enter player #{len(player_list) + 1}\'s name: ').title()
        player_list.append(player)
    print('\nPress the Enter key twice to end the game or\nPress ? to consult the dictionary.\n')
    # initialize player turn at zero for loop
    player_turn = 0
    # Condition assigned as true and loop start
    game_is_playing = True
    while game_is_playing is True:
        #lists player name from player list using player turn as index
        score = input(f'Enter score for {player_list[player_turn]}\'s turn: ')
        # Conditionals for dictionary and regular play
        if score == '?':
            dictionary_mode()
        #if player hits enter w/o entering information, else triggers and game ends
        elif score != '':
            # Validation for score input
            while score.isnumeric() is False or int(score) < 0:
                score = input('\tPlease enter a whole number or "?" to access the dictionary: ')
                if score == "?":
                    dictionary_mode()
            score = int(score)
            # use setdefault to assign a key and empty list to dictionary/append score to dictionary for each player
            #player list is used as the key for the dictionary
            #player turn working as the index
            player_dict.setdefault(f'{player_list[player_turn]}', []).append(score)
            # assign variable to temp hold list and print after each play/conditional to maintain game flow
            run_score = player_dict[player_list[player_turn]]
            print(run_score)
            #Check player turn number. if not last players turn in list, advance counter. Else, return counter to 0
            if f'{player_list[player_turn]}' != f'{player_list[-1]}':
                player_turn += 1
            else:
                player_turn = 0
        # break loop w/ False
        else:
            game_is_playing = False
    return player_list, player_dict

# Validation for number of players. May be overkill. consider removing and using simple validation for player_numb
def getPosint():
    posInt = input('\nHow many players?: \n')
    # print()
    while posInt.isnumeric() is False or int(posInt) < 2:
        posInt = input('\tPlease enter a whole number between 2 and 4 players: ')
    posInt = int(posInt)
    return posInt

# Asks for user input and searches txt document for match using input as the pattern.
# Also validates for at least two letters.

def dictionary_mode():
    #open dixtionary txt file
    start = open('scrabblewords.txt', 'r')
    #start read mode and store txt info in a variable for use later
    scrabble_words = start.read()
    #print header
    print(f'\n{"-"*25} Dictionary {"-"*26}\n')
    #Ask user for word to check
    word_to_Check = input('Enter word you would like to check: ').upper()
    #Condition to ensure that at least two letter are entered
    while len(word_to_Check) < 2:
        #Changed to .upper to match txt doc
        word_to_check = input('Please enter a word that is at least two letters long: ').upper()
    #compile regex using user entered word as perameter, store in variable
    word_regex = re.compile(f'{word_to_Check}')
    #mo stores word if found during search, otherwise stores None
    mo = word_regex.search(scrabble_words)
    #Change user word to title case to make it pretty for the user
    word_fixed = word_to_Check.title()
    # Conditional block. If pattern was not found, returns None. else word is valid
    if mo == None:
        print(f'Oops... Looks like {word_fixed} isn\'t a word.\n')
    else:
        print(f'Congrats, {word_fixed} is indeed a word.\n')
        #Close txt file
        start.close()
    return

# Collects sum and max value from from player_dict and stores them by player name in new dictionaries
# Could be improved if player_dict nested in a new dictionary using dict_final and dict_max as keys.

def processing1(player_list, player_dict):
    dict_final = {}
    dict_max = {}
    #Loop to store player list in new variable; sum totals and append to new dictionary
    for i in range(len(player_list)):
        score = player_dict[player_list[i]]
        sum_score = sum(score)
        dict_final.update({player_list[i]:sum_score})
    #Loop to store player list for max play, add to dictionary for max score
    for i in range(len(player_list)):
        score = player_dict[player_list[i]]
        sum_score = max(score)
        dict_max.update({player_list[i]: sum_score})
    return dict_final, dict_max

# Player output including score list, max value play, and player totals
def output1(player_list, player_dict, dict_final, dict_max):
    print(f'\n{"-"*20} Final Tally! {"-"*20}')
    print('{:<29}{:>15}{:>10}'.format('Player Name', 'Max', 'Total'))
    for i in range(len(player_list)):
        print('{:<24}{:>20}{:>10}'.format(player_list[i], dict_max[player_list[i]], dict_final[player_list[i]]))
        print(f'Score List: {player_dict[player_list[i]]}\n')

main()

