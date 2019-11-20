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
#Create rows and columns using commas for column seperation
(outputWriter.writerow(['Class', 'Day', 'Time', 'Location']))
(outputWriter.writerow(['Data Comm.', 'M/W', '9:45 - 12 PM', 'T\\3080']))
(outputWriter.writerow(['Windows', 'M', '12:45 PM - 3:15 PM', 'T\\3050']))
(outputWriter.writerow(['IT Prep', 'T', '10:10 AM - 12:15 PM' , 'T\\3030']))
(outputWriter.writerow(['Programming', 'Th', '12:00 PM - 3:00 PM', 'T\\3010']))
(outputWriter.writerow(['Hard Knocks', 'Every', 'All', 'The Streets']))
#Close File
outputFile.close()

#Open file into variable
class_file = open('csv_lab.csv', encoding = 'utf-8')
#Read file to variable
class_reader = csv.reader(class_file)
#create list
class_data = list(class_reader)

#For loop for each item in csv
for lines in class_data:
    #For loop to format each line w/spacing
    for item in lines:
        print(format(item, '25'), end='')
    print()
