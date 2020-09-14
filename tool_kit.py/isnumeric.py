#isnumeric

small = input('Please enter a small number, 0 or higher: ')
while not small.isnumeric() or int(small) < 0:
    small = input('Please enter a small numberm 0 or higher: ')
small = int(small)
return small