'''DIctionary study period'''

# scores = {'Al':5, 'Betty':9, 'Cole':8, 'Bea':2}
# scores['Dora'] = 7
# scores['Al'] = 6
# print(scores)

'''List examples to compare'''
rooms = ['Kitchen', 'Bedroom', 'Bathroom']
# rooms.remove('Bedroom')
# rooms.append('Hallway')
# print(rooms)
#
# rooms_colors = {'kitchen':'Blue', 'Bedroom':'Green', 'Bathroom':'Pink'}
# rooms_colors.pop('Bedroom')
# rooms_colors['Hallway'] = 'Beige'
# kitchen_color = rooms_colors['kitchen']
# print('The kitchen will be painted ' + kitchen_color)

'''Dictionary examples'''
# countries = {'CA': 'Canada', 'US': 'United States',  'MX': 'Mexico', 'GB': 'Great Britain'}
# country = countries['MX']   # "Mexico"
#
# #code to re-set a value if the key already exists
# countries['GB'] = 'United Kingdom'
# print(countries['GB'])
#
# #code to add a key-value pair if not in dictionary
# countries['FR'] = 'France'
#
# code = 'EU'
# if code in countries:
#     country = countries[code]
#     print(country)
# else:
#     print('There is no country code: ' +code)
#
# for code in countries:
#     print(code+'\t'+countries[code])
#
# for code in countries.keys():
#     print(code+'\t'+countries[code])
#
# '''Unpacking a tuple for key and value'''
#
# #items method
# for code, country in countries.items():
#     print(code+'\t'+country)
#
# #values method is a little different
# for country in countries.values():
#     print(country)
#
# '''The get method'''
#
# #dictionary_name.get(key, default_value)
#
# country = countries.get('MX')
# print(country)
#
# #If entry doesn't exist; better than an error
# country = countries.get('IE', "unknown")
# print(country)
#
# '''Syntax for deleting an item'''
# #del countries['MX']
#
# checkCode = 'MX'
# if checkCode in countries:
#     country = countries[checkCode]
#     del countries[checkCode]
#     print(country + ' was deleted.')
# else:
#     print('There is no country for this code: '+checkCode)
# print(countries)
#
# '''More methods for deleting dictionary items'''
# #Code for using .pop() method
# country = countries.pop('US')#.pop() will still return the item
# print(country)
# # .clear() will erase the entire list
# countries.clear()
# print(countries)