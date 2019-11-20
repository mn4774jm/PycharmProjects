'''Author:Thomas Mullins
Date: 1/24/19
Description: Calculate bus fares for the month in a table format'''
#Variables
rushRide=int(12)
regRide=int(7)
rglrBus=float(1.75)
rushBus=float(3.00)
totlBus=((rglrBus*7)+(rushBus*12))
totlReg=(rglrBus*regRide)
totlRush=(rushBus*rushRide)

#print('Regular Fare', format(rglrBus, '12.2f'))
#print('Rush Fare   ', format(rushBus, '12.2f'))
#print('Total Fare  ', format(totlBus, '12.2f'))

#Header
print('Bus Fare Program\nFare Type\tRides\t($)Price\t($)Total Spent')
#Print sting for regular rate
print('Regular', str(format(regRide, '9.0f')+'\t$'+str(format(rglrBus, '11.2f'))+str(format(totlReg, '18.2f'))))
#Print string for rush rate
print('Rush', str(format(rushRide, '12.0f')+str(format(rushBus, '11.2f'))+str(format(totlRush, '18.2f'))))
