#! python 3
"""M. Bock 7/11/2019
This program should download, open and read a .txt file
It should display the results in an easy-to-read fashion.
"""

import requests     # add to top of code

# 2 lines from PPT slide 6 will fulfill the requirement
response4 = requests.get('https://www.w3.org/TR/PNG/iso_8859-1.txt')   # accesses URL and finds file
print(response4.text)    # print part of the text file if you add [startindex:stopindex]

# saving the data to a file or using read binary is optional.



