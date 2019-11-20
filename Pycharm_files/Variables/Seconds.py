'''Author: Thomas Mullins
Date:1/28/19
Definition: Calculate and display the number of seconds in a year'''

# Define variables
secondsPerminute = int(60)
secondsPerhour = int(60)*secondsPerminute
secondsPerday = int(60)*secondsPerhour
secondsPeryear = int(365)*secondsPerday
Total= int(secondsPeryear)
#print(Total)
#print('There are '+ str(Total)+ " seconds in a year.")
#Format
format(Total, ",.0f")
print('There are '+(str(format(Total, ",.0f")))+ ' seconds in a year.')
