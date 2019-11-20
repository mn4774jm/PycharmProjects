# Use format() function inside the print() function to control the look.
print(format(12345.6789, '.1f'))
print(format(12345.6789, '.2f'))

# Add comma separators:
print(format(12345.6789, ',.2f'))

# Specify the minimum column width:
print(format(12345.6789, '12.2f'))

# How to add a period line
print('{:.<30}{:.>7}'.format('Total',len(guests)))


#formatting choices

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

#across list formatting ex.

#Starts for loop taking the length of list 'Catagories' as the range and assigns to 'item'
for item in range(len(catagories)):
    print('(0:<15)$(1:<10.2f').format(catagories[item], budget[item])

# print the budget items
# when printing, "end" by default is a new line, the "end=''" command replaces it with nothing


#This is for printing two rows: see example in practice.py, midtermpractice3

#Beginning of for loop to print all items in list
for i in range(len(needs_list)):
    print('{:15}'.format(needs_list[i]), end='')#End prevents a default \n from printing after each item
print()
# print the costs of each item in list
for i in range(len(costs)):
    print('${:<14,.2f}'.format(costs[i]), end='')

print('\nYour total monthly budget is ${:,.2f}'.format(sum(costs)))

#This will print two columns
#for loop to print the items in both the needs_list and costs list; column version
for index in range(len(needs_list)):
    print('{:<30}{:>2}{:>5}'.format(needs_list[index], '$', f'{costs[index]}'))
print(f'Your total monthly budget is ${total}')


#shortcut to print without brackets and quotation marks
#with an optional seperator.
(*listname, sep= ",")



