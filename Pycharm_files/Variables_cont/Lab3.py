#city = 'Minneapolis'
#temp = 67
#chanceRain = 40
#gasPrice = 2.50
#guests = 1000
#print(f'Welcome! Around the {city} Hilton we have…')
#print('{0:<14}{1:^14}{2:^14}{3:^14}'.format('Temperature', 'Chance Rain', 'Gas Price', 'Guests'))
#print(f'{temp:>5d}F \t\t{chanceRain:>9d}% \t\t\t${gasPrice:<9.2f}{guests:^14,d}')

# using a "leader"
#city ='Minneapolis'
#temp = 67
#chanceRain = 40
#gasPrice = 2.50

#name1=input('Please type your name:')
#print('Hello,'+name1+'!')

#numberOfCds = int(input('Number of CDs? '))
#numberOfLps = int(input('Number of LPs? '))
#numberOfAlbums = numberOfCds + numberOfLps
#print('With', str(numberOfCds), 'CDs and', str(numberOfLps), 'LPs, the number of albums you have is', str(numberOfAlbums)+ '.')

#temp=float(input('Enter the patient\'s temperature:'))
#pay=float(input('Enter the employee\'s pay:'))
#print('Your temp is',str(temp),'and your pay is $', str(pay))

cups=int(input('How many cups of coffee sold?'))
price=float(input('Price of coffee?'))
coffeeSales=cups*price
#print('--Using format function')
#print('Total sales = $' + format(coffeeSales, '.2f'))

#print('--Using python 3x shorthand formatting')
#print(f'Total sales = ${coffeeSales:.2f}')

#print('--Using shorthand formatting to create a simple 2 column table')
#print(f'Cups sold:\t $ {cups:>6.2f}')
#print(f'Cup price:\t $ {price:>6.2f}')
#print(f'Total/day:\t $ {coffeeSales:>6.2f}')


print('{:<20}{:>3}{:>7.2f}'.format('Cups sold', '$', cups))
print('{:<20}{:>3}{:>7.2f}'.format('Price per cup', '$', price))
print('{:<20}{:>3}{:>7.2f}'.format('Total sales', '$', coffeeSales))


