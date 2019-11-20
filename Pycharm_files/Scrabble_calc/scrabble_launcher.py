'''Launcher program to work in conjuction with the scrabble6_nice.py and scrabble6_grrr.py files
pycharm interpreter version 3.7 used with webbrowser module installed'''

import webbrowser

print(f'\n{"-"*10} Welcome to the Scrabble Calculator v0.06 {"-"*10}\n')
def main():
    try:
        displayMenu()
        while True:
            command = input("Command: ").lower()
            if command == "nice":
                import scrabble6_nice.py
            elif command == "noice":
                import scrabble6_grrr.py
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
    print ("Nice   - For the standard version")
    print ("Noice  - For when you are surrounded by secret assassins")
    print ("Rules  - For when you came unprepared (Requires an internet connection)")
    print ("Exit   - For when you opened this by mistake")
    print()

main()







