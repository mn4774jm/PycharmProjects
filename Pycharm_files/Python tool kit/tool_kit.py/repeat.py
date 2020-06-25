
#Repeat the program?
        #Asks for user input of yes or no. Answer is capitalized by .upper() so that user error is mitigated
        answer = input('\nWould you like to run this program again? Enter Y or N: ').upper()
        while answer != 'Y' and answer != 'N':
            answer = input('Please enter Y or N: ').upper()
        if answer == 'N':
            print(f'\nThank for using the program')
            break