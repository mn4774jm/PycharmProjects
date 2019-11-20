villains = ['Voldemort', 'Darth Vader', 'Sauron']
quizScores = [10, 9, 10, 8]
rainfallAmts = [0.8, 1.1, 1.3, 2.1, 0.6, 0.2, 7.6]
mixedItems = ['Hello', 100, 5.55]
listOfLists = [[1,2,3], [4,5,6]]

firstVillain = villains[0]
print(firstVillain)
secondQuizScore = quizScores[1]
print(secondQuizScore)
fifthRainfall = rainfallAmts[4]
print(fifthRainfall)

villains[0] = 'Catwoman'
print(villains)
quizScores[1] = 10
print(quizScores)
rainfallAmts[4] = 1.2
print(rainfallAmts)

villains = ['Catwoman', 'Darth Vader', 'Sauron']
villains.append('Lex Luthor')
print(villains)
villains.append('Magneto')
print(villains)

villains = ['Catwoman', 'Darth Vader', 'Sauron', 'Lex Luthor', 'Magneto']
if 'Darth Vader' in villains:
	print('Darth Vader is in the list')
else:
	print('Darth Vader is NOT in the list')

if 'Voldemort' in villains:
	print('Voldemort is in the list')
else:
	print('Voldemort is NOT in the list')
