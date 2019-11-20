'''villians = ['Voldemort', 'Darth Vader', 'Sauron']
quizScores = [10, 9, 10, 8]
rainfallAmts = [0.8, 1.1, 1.3, 2.1, 0.6, 0.2, 7.6]
mixedItems = ['Hello', 100, 5.55]
listOfLists = [[1,2,3],[4,5,6]]

firstVillian = villians[0]
print(firstVillian)
secondQuizScore = quizScores[1]
print(secondQuizScore)
fifthRainfall = rainfallAmts[4]
print(fifthRainfall)

villians[0] = 'Catwoman'
print(villians)
quizScores[1] = 10
print(quizScores)
rainfallAmts[4] = 1.2
print(rainfallAmts)

listOfColleges = ['MCTC', 'Metro State', 'SPC', 'MCTC']
for index in range(len(listOfColleges)):
    print(f'College #{index+1}')
    print(f'Name: {listOfColleges[index]}')
print('\n')

rainfallAmts = [0.8, 1.1, 1.3, 2.1, 1.2, 0.2, 7.6]
totalRain = 0.0
for index in range(len(rainfallAmts)):
    totalRain += rainfallAmts[index]
avgRain = totalRain/len(rainfallAmts)
print(f'Total rain = {totalRain:.2f} and Avg. rain = {avgRain:.2f}\n')

numbers = [1,2,3,4,5,6,7,8,9,10]
for index in range(len(numbers)):
    squared = numbers[index]**2
    print(f'{numbers[index]:>2d} squared is {squared: >3d}')'''

print('Welcome to the guest list builder')
guests = []
while True:
    newGuest = input('Type in the name & enter(hit twice to quit):')
    if newGuest == '':
        break
    else:
        guests.append(newGuest)
print(guests)
print(*guests, sep = ',')


