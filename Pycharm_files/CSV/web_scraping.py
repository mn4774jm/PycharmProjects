'''Author: Thomas Mullins
date: 4/25/19
Description: write a program to download a txt file from online, open
and read the file, and then display the output.
web_scraping.py'''


import requests #import module
#Create variable to hold get txt
response1 = requests.get('http://www.gutenberg.org/cache/epub/32095/pg32095.txt')
#check status for errors
response1.raise_for_status()
#Store txt using wb for chunking, 'wb' = write binary
playfile = open('PussNBoots.txt', 'wb')
#Start loop to chunk data
for chunk in response1.iter_content(100000):
    playfile.write(chunk)#method writes to file
#Close file
playfile.close()
#Print limited text
print(response1.text[675:1000])

