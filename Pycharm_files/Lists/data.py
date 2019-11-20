data = [7, 8, 9, 10]
copyOfData = data[:]
print(copyOfData)
copyOfData.remove(8)
print(data)
print(copyOfData)

print()

data = [7, 8, 9, 10]
aliasOfData = data
print(aliasOfData)
aliasOfData.remove(8)
print(data)
print(aliasOfData)
