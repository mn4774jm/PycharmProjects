#! python 3
"""
M. Bock 11/6/2019 - this file shows step 1 to change example program to be
more dynamic. The new program asks the user to enter a url, and constructs a
file name to save results. If completed, the program would scrape a portion
of the page, write to file, re-open the file and display.
"""

from bs4 import BeautifulSoup as soup       # As soup so you don't have to keep typing BeautifulSoup
import requests


def main():
    # User can set source URL - showing example of light validation & correction.
    str_url = input('Enter a valid URL to download and save. ').strip()
    while 'https://' not in str_url and 'http://' not in str_url:
        str_url = input('Try again to enter a valid URL. ').strip()
    # Set filename for saving results. This one is based on URL.
    # Remove problem characters.
    str_filename = str_url[8:].replace('/','').replace('.','') + '.txt'

    # example code w/comments on additional adaptations needed
    try:
        # Display status messages
        print("\nDownloading poem from URL: ", str_url)  # take out references to poem
        print("Saving to                : ", str_filename)
        # Get specified webpage in soup html parsed format
        imported_webpage = GetWebpage(str_url)
        # Ask user if they'd like to see the source html
        while True:
            str_input = input("\nWould you like to see the unprocessed HTML? (y/n) : ")  # Get user input
            if str_input == "y" or str_input == "yes":    # If yes display source html /// for some reason if I use .lower, it does not work.
                print("\n### Displaying raw html ###")
                print("\n", imported_webpage)
                print("\n###   End of raw html   ###")
                break
            elif str_input == "n" or str_input == "no":   # If no, then display nothing and continue on..
                break
            else:
                print("Invalid input. Please try again.") # If no matching option detected, display error message and ask again.
        # Extract Poem --> changes needed - in new version don't limit to poems
        str_poem = ExtractPoem(imported_webpage)  # see above
        # Export
        ExportFile(str_poem, str_filename)
        # Re-import file
        print("\nSave complete, re-importing file.")
        str_content = ImportFile(str_filename)
        # Display contents of file on screen
        print("\nFile read into memory, displaying contents:\n")
        Display(str_content)
    except Exception as err:  # generic exception handling, if something goes wrong
        print("\nCongratulations. You broke the time continuum. Internal error\n")
        print(err)
    # added restart feature for ease of testing
    restart = input('Would you like to start over? Enter y or n: ')
    if restart == 'y':
        main()
    else:
        print('Thanks for using the program.')


def GetWebpage(str_url):
    # Get web page
    page_html = requests.get(str_url)
    # Parse with BeautifulSoup's html parser
    page_soup = soup(page_html.text, "html.parser")
    # Return result in soup format
    return page_soup

''' to make this function work for a dynamic, user-defined URL
 show the user what html elements exist in the requested page. 
 Let them pick from existing elements & reject others.'''
def ExtractPoem(page_soup):
    # Locate div tag, class - 'poem_body' --> to do: make this dynamic
    found = page_soup.find("div", {"class": "poem_body"})
    # This strips all the leading white space from each paragraph
    poem = "\n".join(line.strip() for line in found.p.text.split("\n"))
    # Return parsed poem as string
    return poem


def ExportFile(str_content, str_filename):
    # Open specified file in write mode  (not write - binary like the last one)
    export_file = open(str_filename, 'w')
    # Write contents out to file
    export_file.write(str_content)
    # Close file
    export_file.close()
    # In a more complex program I'd have it return a result such as success/fail


def ImportFile(str_filename):
    # Open specified file in read mode
    import_file = open(str_filename, 'r')
    # Read contents of file in variable
    str_content = import_file.read()                   # read file contents into variable
    # Close file
    # import_file.close   - not necessary to disabled
    return str_content


def Display(content):
    # Pretty simple, display contents of file. It's already formatted correctly
    print(content)


# Engage
if __name__ == '__main__':
    main()