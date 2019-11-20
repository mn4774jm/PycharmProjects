'''Author: Thomas Mullins
date: 4/25/19
Description: write a program to download a txt file from online, open
and read the file, and then display the output.
web_scraping.py'''

# import webbrowser, pyperclip, requests
# response1 = requests.get('http://www.gutenberg.org/cache/epub/32095/pg32095.txt')
# response1.raise_for_status()
# playfile = open('PussNBoots.txt', 'wb')
# for chunk in response1.iter_content(100000):
#     playfile.write(chunk)
# playfile.close()
# print(response1.text[675:1000])


'''Author: Thomas Mullins
Date: 4/25/19
Description: Create a .csv file with at least 3 columns and 6 rows of data
csv_read.py'''

#Writer objects let you write data to a CSV; csv.writer() function.
import csv
#Create outputfile object and create output.csv
outputFile = open('csv_lab.csv', 'w', newline='')
#Create the writer object
outputWriter = csv.writer(outputFile)
(outputWriter.writerow(['Class', 'Day', 'Time', 'Location']))
(outputWriter.writerow(['Data Comm.', 'M/W', '9:45 - 12 PM', 'T\\3080']))
(outputWriter.writerow(['Windows', 'M', '12:45 PM - 3:15 PM', 'T\\3050']))
(outputWriter.writerow(['IT Prep', 'T', '10:10 AM - 12:15 PM' , 'T\\3030']))
(outputWriter.writerow(['Programming', 'Th', '12:00 PM - 3:00 PM', 'T\\3010']))
(outputWriter.writerow(['Hard Knocks', 'Every', 'All', 'The Streets']))
outputFile.close()


example_file = open('csv_lab.csv', encoding = 'utf-8') 	# open file into a variable – encoding sometimes needed
example_reader = csv.reader(example_file)			# creates Reader object to iterate thru variable data
example_data = list(example_reader) 				# creates a Python list for easier handling


for lines in example_data:
    for item in lines:
        print(format(item, '25'), end='')
    print()

