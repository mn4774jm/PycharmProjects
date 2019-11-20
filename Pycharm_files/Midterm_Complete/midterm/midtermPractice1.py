'''Author: Thomas Mullins
Definition: This program calculates the total cost of a restaurant meal, and creates a summary receipt with meal price, tip, tax & total.
midtermPractice1.py
Date: 3/8/19'''

#Header
print('Welcome to Bob\'s Diner!')

#User input for meal price
mealPrice = input('Enter the price of your meal: ')
#Assigned float
mealPrice = float(mealPrice)
#User input for tip %
tipPercent = input('Enter tip percent -> .15, .20, etc.: ')
#Assigned float to tip percent
tipPercent = float(tipPercent)
#Calculate tip value
tipValue = tipPercent*mealPrice
#caluculate tax
tax = float(.075)*mealPrice
#Calculate total due
totalDue = mealPrice + tipValue + tax

#Print Statement and formatting
print(f'\nMeal price\t$\t{mealPrice:>5.2f}')
#multiply by 100 for correct tip representation on check
print(f'Tip @ {tipPercent*100}%\t$\t{tipValue:>5.2f}')
print(f'Tax @ 7.5%\t$\t{tax:>5.2f}')
print(f'Total due\t$\t{totalDue:>5.2f}')
print('\nThanks for dining at Bob\'s')