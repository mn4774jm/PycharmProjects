def main():
    stringData = input('Please enter a string: ') # input a string
    repeat = int(input('How many times to repeat? ')) # input a number
    stringRepeater(stringData, repeat) # function call with 2 arguments

def stringRepeater(text, n): # called function receiving 2 parameter values
    repeatedString = text * n
    print('Here\'s your string...')
    print(repeatedString)

main() #function call



