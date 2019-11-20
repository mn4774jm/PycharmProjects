'''Web Scraping'''

'''impert webbrowser'''
# #Importing webbrowser and entering the open command autoloads a web page
# import webbrowser
#
# webbrowser.open('http://inventwithpython.com/')

'''Downloading files from the web with the requests module'''

import requests
#
# #The requests.get() function takes a string of URL to download.
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# type(res)
#
# #Checking for download success
# requests.codes.ok
#
# #Checking for errors; will display error messages
# res.raise_for_status()

'''Saving Downloaded Files to the Hard Drive'''
#To write a web page to a file, you can use a loop
# 1. Call requests.get() to download the file.
#
# 2. Call open() with 'wb' to create a new file in write binary mode.
#
# 3. Loop over the Response object’s iter_content() method.
#
# 4. Call write() on each iteration to write the content to the file.
#
# 5. Call close() to close the file.

'''Viewing the source HTML of a web page'''
# 1. control click on a web page in your browser
# 2. select view page source

'''Opening your browsers developer tools'''
# Press F12 on chrome and internet explorer for windows
# command-option-I on chrome for mac

'''Using developer tools to find HTML elements'''
# command-click on an element to launch the developer tools window.
# This will show you the HTML that produces that part of the web page.

'''Passing HTML with the beautifulsoup module'''
#Module used for extracting info from HTML pages

import bs4

'''Creating a beautiful soup object from html'''
import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup('features="html.parser"',res.text)
type(noStarchSoup)

