'''M. Bock 6/11/2019 This program tracks coffee stand sales by drink,
price, subtotal per drink and grand total for both cups and sales.
The results are printed into columns
'''

# collect data input & assign to variables
drink_types = int(input('How many different types of drinks did you sell today? '))
total_cups = 0
total_sales = 0.0
for type in range(drink_types):
    drink_name = input(f'\nName of the drink type #{type + 1}: ')
    for size in range(3):
        cups_sold = int(input(f'\tNumber of cups of {drink_name} size {size + 1} sold: '))
        price = float(input(f'\tPrice of {drink_name} size {size + 1}: $ '))
        subtotal = round(cups_sold * price, 2)
        print('\t{:<12}Sz.{:>2,d}{:>9,d}{:>8}{:>4,.2f}{:>8}{:>9,.2f}'.format(drink_name, size + 1, cups_sold,'$',price,'$',subtotal))
        total_cups += cups_sold
        total_sales += subtotal
print('\nToday\'s Drink Sales for the Reporting Period')
print('{:<12}{:^13}{:^12}{:^13}'.format('Types','Cups Sold','','Total'))
print('{:<12}{:>7,d}{:>20}{:>7.2f}'.format(drink_types,total_cups,'$',total_sales))
