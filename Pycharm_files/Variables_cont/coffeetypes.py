'''Author: Thomas Mullins
Date: 1/29/19
CoffeeTypes.py
Description: Define how many types of coffee products, cost, and daily totals'''

coffee=int(input('How many cups of coffee sold?'))
cofCost=float(input('Price of coffee?'))
tea=int(input('How many cups of tea sold?'))
teaCost=float(input('Price of tea?'))
cap=int(input('How many cups of cappuccino sold?'))
capCost=float(input('Price of cappuccino?'))
coffeeSales=coffee*cofCost
teaSales=tea*teaCost
capSales=cap*capCost
cupNumb=coffee+tea+cap
tltSales=coffeeSales+teaSales+capSales

#Write header and define print script/format
print('Drink Sales For Reporting Period\nDrink Type\t\tCups Sold\t\t\t Price\t\t Total')
print(f'Coffee {coffee:>18.0f}\t\t\t ${cofCost:>0.2f}\t\t ${coffeeSales:>0.2f}')
print(f'Tea    {tea:>18.0f}\t\t\t ${teaCost:>0.2f}\t\t ${teaSales:>0.2f}')
print(f'Cappuccino {cap:>14.0f}\t\t\t ${capCost:>0.2f}\t\t ${capSales:>0.2f}')
print(f'Total{cupNumb:>20.0f}\t\t\t\t\t\t ${tltSales:>0.2f}')
