'''Author:Thomas Mullins
Date: 1/24/19
Description: Calculate bus fares for the month in a table format'''
#Variables
rushRide=12
regRide=7
rglrBus=float(1.75)
rushBus=float(3.00)
totlBus=((rglrBus*7)+(rushBus*12))
#print('Regular Fare', format(rglrBus, '12.2f'))
#print('Rush Fare   ', format(rushBus, '12.2f'))
#print('Total Fare  ', format(totlBus, '12.2f'))

#Format data descriptions
print('Bus Fare Program\nFare Type\tRides\tPrice\tTotal Spent')
print('Regular'\t str(regRide) #, format(rglrBus, '12.2f'))