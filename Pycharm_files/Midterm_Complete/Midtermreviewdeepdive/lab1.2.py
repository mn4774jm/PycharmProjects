#Compare formatting strategies – add to your code file, run & analyze.

cups = int(input('How many cups of coffee were sold?'))
price = float(input('How much is a cup of coffee?'))
coffeeSales = cups*price

print('--Using format function')
print('Total sales = $' + format(coffeeSales, '.2f'))

print('--Using python 3x shorthand formatting')
print(f'Total sales = ${coffeeSales:.2f}')

print('--Using shorthand formatting to create a simple 2 column table')
print(f'Cups sold:\t $ {cups:>6.2f}')
print(f'Cup price:\t $ {price:>6.2f}')
print(f'Total/day:\t $ {coffeeSales:>6.2f}')

print('--Using longhand .format method - for more control.')
print('{:<20}{:>3}{:>7.2f}'.format('Cups sold', '$', cups))
print('{:<20}{:>3}{:>7.2f}'.format('Price per cup', '$', price))
print('{:<20}{:>3}{:>7.2f}'.format('Total sales', '$', coffeeSales))

'''milesTraveled = float(input('How many miles did you travel? '))
gasUsed = float(input('How many gallons of gas did you use? '))
gasPrice = float(input('What is the current price of gas?' ))

tripCost = gasPrice * gasUsed
MPG = milesTraveled/gasUsed

print('Welcome to the Gas Calculator program')
print('These are your trip details:')
print('{:<20}{:>}{:>7}'.format('Miles Traveled','',milesTraveled))
print('{:<20}{:>}{:>6.2}'.format('Gas Used','$',gasUsed))
print('{:<20}{:>}{:>6.2}'.format('Gas Price','$',gasPrice))
print(f'And your fuel efficiency was {MPG} MPG.')'''
