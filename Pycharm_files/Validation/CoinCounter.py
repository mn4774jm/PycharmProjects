'''Author: Thomas Mullins
Date: 2/11/19
CoinCounter.py
Definition: A coin jar usually has mixed coins. Write a program that asks the user how many 25c quarters they have in a
jar, and how many 10c dimes, 5c nickels, and 1c pennies.
'''


#Variables and input
# Can avoid Validation if int(input() is used instead; in this instance
quarters = input('How many quarters do you have? Enter a whole number:') #Defining quarters
dimes = input('How many dimes do you have? Enter a whole number:') #Defining dimes
nickles = input('How many nickles do you have? Enter a whole number:') #Defining nickles
pennies = input('How many pennies do you have? Enter a whole number:') #Defining pennies

#Validation
if quarters.isnumeric() or dimes.isnumeric() or nickles.isnumeric() or pennies.isnumeric():

#Defining input as integers
    quarters = int(quarters)
    dimes = int(dimes)
    nickles = int(nickles)
    pennies = int(pennies)

#Variable calculations for correct monatary addition in USD terms
    qValue = (quarters/4)
    dValue = (dimes/10)
    nValue = (nickles/20)
    pValue = (pennies/100)
    cCount = (quarters+dimes+nickles+pennies) #Calc for sum of physical coins
    cValue = (qValue+dValue+nValue+pValue) #Calc for monatary sum

#Print scrpt and output, all columns include > to line up accordingly.
    print('\nTotal value of your coins.\nCoin Type\t\t\tNumber\t\t\tValue') #Header including
    print(f'Quarters:  {quarters:>15.0f}{f"${qValue:.2f}":>15}')# Nested brackets for dollar sign
    print(f'Dimes:     {dimes:>15.0f}{f"${dValue:.2f}":>15}') # Nested brackets for dollar sign
    print(f'Nickles:   {nickles:>15.0f}{f"${nValue:.2f}":>15}') # Nested brackets for dollar sign
    print(f'Pennies:   {pennies:>15.0f}{f"${pValue:.2f}":>15}') # Nested brackets for dollar sign
    print(f'Total:     {cCount:>15.0f}{f"${cValue:.2f}":>15}') #N ested brackets for dollar sign

if cValue >= 10: #Message for if user is over $10
    print('\nCongrats! You\'ve passed the $10 mark!')
elif cValue <= 10: #Message for if user is under $10
    print('\nNot quite $10, friend. Keep saving!')
else: #Does not function?
    print('Please enter only whole numeric coin amounts')




