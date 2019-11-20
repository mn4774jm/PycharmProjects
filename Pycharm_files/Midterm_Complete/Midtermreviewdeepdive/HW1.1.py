#gasCalc.py

milesTraveled = float(input('How many miles did you travel? '))
gasUsed = float(input('How many gallons of gas did you use? '))
gasPrice = float(input('What is the current price of gas?' ))

tripCost = gasPrice * gasUsed
MPG = milesTraveled/gasUsed

print('Welcome to the Gas Calculator program')
print('These are your trip details:')
print('{:<20}{:>}{:>7}'.format('Miles Traveled','',milesTraveled))
print('{:<20}{:>}{:>6.2}'.format('Gas Used','$',gasUsed))
print('{:<20}{:>}{:>6.2}'.format('Gas Price','$',gasPrice))
print(f'And your fuel efficiency was {MPG} MPG.')