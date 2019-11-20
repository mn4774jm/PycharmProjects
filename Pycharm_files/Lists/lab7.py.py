


'''# use longhand method when you need to work on each list item separately
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index in range(len(numbers)):
	squared = numbers[index] ** 2
	print(f'{numbers[index] :>2d} squared is {squared :>3d}')'''


print('Welcome to the Guest List Builder')


guests = []
while True:
	newGuest = name_regex()
	if newGuest == '':
		break
	else:
		guests.append(newGuest)
#print(guests) # compare results
print(*guests, sep = ", ")

for index in range(len(guests)):
	if index < len(guests) -1:
		print(f'Guest #{index + 1} is {guests[index]}, ', end = "")
	else:
		print(f'and Guest #{index + 1} is {guests[index]}.')

print('{:<30}{:>7}'.format('Guest Name','Ticket'))
for index in range(len(guests)):
	print('{:<30}{:>2}{:>5}'.format(guests[index],'#',index + 1001))
print('{:.<30}{:.>7}'.format('Total',len(guests)))


# print(guests)
# nixedSecondGuest = guests.pop(1)
# print('Name removed: ', nixedSecondGuest )
# print('Guest list: ', guests)
#
# if 'Sauron' in guests:
# 	guests.remove('Sauron')
# else:
# 	print('No such guest.')
# print('Guest list: ', guests)


# guests.sort()
# print(guests)





