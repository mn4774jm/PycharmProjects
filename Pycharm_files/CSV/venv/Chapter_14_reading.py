'''Working with CSV Files and JSON data'''

'''The CSV (comma-seperated values) module'''
#Each line in a csv file represents a row in a spreadsheet; commas seperate rows
#CSV files are simple and lack many features you might find in excel

# 1.Don’t have types for their values—everything is a string
#
# 2. Don’t have settings for font size or color
#
# 3. Don’t have multiple worksheets
#
# 4. Can’t specify cell widths and heights
#
# 5. Can’t have merged cells
#
# 6. Can’t have images or charts embedded in them

'''Reader objects'''
# import csv #import csv
# #To read data from a csv file you need to create a reader object.
# #Open file using open()
# exampleFile = open('example.csv')
# #Use csv.reader() to assign to exampleReader
# exampleReader = csv.reader(exampleFile)
# #Convert exampleReader into a list
# exampleData = list(exampleReader)
# print(exampleData)
#
# print(exampleData[0][0])
# print(exampleData[0][1])
# print(exampleData[0][2])
# print(exampleData[1][1])
# print(exampleData[6][1])

'''Reading Data from reader objects in a for loop'''
# import csv
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

'''Writer objects'''
# #Writer objects let you write data to a CSV; csv.writer() function.
# import csv
# #Create outputfile object and create output.csv
# outputFile = open('output.csv', 'w', newline='')
# #Create the writer object
# outputWriter = csv.writer(outputFile)
# print(outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham']))
# print(outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']))
# print(outputWriter.writerow([1, 2, 3.141592, 4]))
# outputFile.close()

'''The delimiter and lineterminator keyword arguments'''
#Used as a format tool
import csv
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
print(csvWriter.writerow(['apples', 'oranges', 'grapes']))
print(csvWriter.writerow(['eggs', 'bacon', 'ham']))
print(csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam']))
csvFile.close()