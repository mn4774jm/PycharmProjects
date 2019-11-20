'''
Author: Thomas Mullins
Date: 4/18/19
randomQuizGenerator.py
Definition - Creates quizzes with questions and answers in
random order, along with the answer key.'''

import random
import os
import pprint
current = os.getcwd()
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Ask user if they would like to create a new folder for created files w/ validation
print('\nWould you like to create a new folder location?'
      '\nEntering "N" will write files to '+current)
answer = input('Please enter Y or N: ')
while answer.upper() != 'Y' and answer.upper() != 'N':
    answer = input('Please enter Y or N: ')
if answer.upper() == 'Y':
#Create new folder and change directory to write the files to
    where = input('New folder location: ')
    os.makedirs(f'{where}')
    os.chdir(f'{where}')
    capitalsItems = list(capitals.items())
    pprint.pprint('Full capitals list: '+ str(capitalsItems))

else: #Else will wrie to the cwd
    capitalsItems = list(capitals.items())
    pprint.pprint('Full capitals list: ' + str(capitalsItems))

# Generate 35 quiz files.
for quizNum in range(35): 
    # Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1} )')
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys()) # get all states in a list
    random.shuffle(states) # randomize the order of the states

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):

        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values()) # get a complete list of answers
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # remove the right answer
        wrongAnswers = random.sample(wrongAnswers, 3) # pick 3 random ones

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions) # randomize the order of the answers

        # Write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f'   {"ABCD"[i]}. {answerOptions[i]}\n')
        quizFile.write('\n')

        # Write out the answer key to a file.
        answerKeyFile.write(f'{questionNum + 1}. {"ABCD"[answerOptions.index(correctAnswer)]}\n')
    quizFile.close()
    answerKeyFile.close()

'''
Enable the user to create a new folder to add the newly created files to and automatically change cwd to that selected
folder before writing. This could be accomplished with the use of os.makedirs(); which might look something like 
os.makedirs('/users/tom/pycharmprojects/state_capitals'). That would be followed with the change directories function 
before writing begins. ex) os.chdir('/users/tom/pycharmprojects/state_capitals'). I have taken the liberty of adding
this to the current program with a friendly-ish user interface. 
'''
