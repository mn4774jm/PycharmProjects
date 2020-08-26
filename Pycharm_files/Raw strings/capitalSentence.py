'''Author: Thomas Mullins
Date: 4/7/19
Description: Write a program that accepts input of multiple sentences into one
input prompt, all ending with a period, but case insensitive.
capitalSentences.py
'''
#Define main
def main():
    #Begin exception handling
    while True:
        try:
            #Calls and arguments
            sentences = input1()
            capital_sentences = processing1(sentences)
            output1(capital_sentences)

         #End exception handling
        except Exception as err:
            print(err)

        #Repeat block
        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

#Define input1
def input1():
    print('\nWelcome to the paragraph splitter!')
    print('Please enter 3 sentences, each ending with a period.')
    sentences = input('You don\'t have to capitalize them: ')

    #Validation block using while loop
    while sentences.isnumeric() is True or sentences == '':
        sentences = input('No numbers please\nEnter three sentences, each ending with a period.: ')

    return sentences

#Define processing1
def processing1(sentences):
    sentences = sentences.lower()
    #Split string into list at periods
    all_sentences = sentences.split('.')
    #Remove last argument with pop
    all_sentences.pop()
    #Empty list created
    capital_sentences = []

    #Begin for loop to modify list items
    for sentence in all_sentences:
        #Remove whitespace
        sentence = sentence.strip()
        #Capitalize first letter in each list
        sentence = sentence.capitalize()
        #Add period back into list items at end
        sentence = f'{sentence}.'
        #Add each modified list item to empty list
        capital_sentences.append(sentence)
    return capital_sentences
#Define output1
def output1(capital_sentences):
    print('Here are your sentences: ')

    # Enumerate function used to add count in front of each item
    # for count, index in enumerate(capital_sentences, 1):
    #     print(f'{count}.', index)

    for i in range(len(capital_sentences)):
        print(str(i+1)+f'. {capital_sentences[i]}')

    #print fixed list
    print(f'Your sentence list fixed is:\n{capital_sentences}')


#Call main
main()

