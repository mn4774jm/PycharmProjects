# import webbrowser, pyperclip, requests
#
# '''Using pyperclip and webbrowser modules'''
# # #Minneapolis, MN
# # address = pyperclip.paste() #Pastes the data copied to clipboard
# # webbrowser.open('https://www.google.com/maps/place/' + address)
# #
# # '''Downloading data & files from the web'''
# # import requests # Required to function
#
# response1 = requests.get('https://automatetheboringstuff.com/files/rj.txt')   # accesses URL and finds file
# print(type(response1))   # returns the type of the response1 variable
# print(response1.status_code)   # check out all the HTTP response status codes on python.org
# print(response1.status_code==requests.codes['OK'])   # common way to check if HTTP response is OK
# print(len(response1.text))    # shows the length of the text file
# print(response1.text[0:250])    # print part of the text file [startindex:stopindex]
#
#

import csv
example_file = open('example.csv', encoding = 'utf-8') 	# open file into a variable – encoding sometimes needed
example_reader = csv.reader(example_file)			# creates Reader object to iterate thru variable data
example_data = list(example_reader) 				# creates a Python list for easier handling
print(example_data)   							# what's the data structure here?
print(len(example_data))							# this shows length of what?
print(example_data[0][0])  						# access values using index for [row] and [column]
print(example_data[0][1])
print(example_data[6][0])
print(example_data[6][1])

