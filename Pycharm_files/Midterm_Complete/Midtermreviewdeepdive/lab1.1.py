'''
#wageCalc.py
wage = float(18)
OT = float(wage)*1.5
hours = float(0)
if hours <= 40:
    hours = float(input('How many hours did you work this week?'))
    pay = hours*wage
    print(f'You have earned ${pay: .2f} for the week')
elif hours > 40:
    pay = hours*wage*OT
    print(f'You have earned ${pay: .2f} this week.')'''


'''
#AvgGrade.py
# Define variables
score1 = 45
score2 = 74
score3 = 63

# Calculate the average of the 3 scores
averageScore = (score1 + score2 + score3) / 3.0
averageScore = int(averageScore)

# Display the average
print(f'The average test score is {averageScore:.2f}')'''

#BusFare
regFare = float(1.75)
rushFare = float(3)

regRides = 7
rushRides = 12

regtotal = regFare*regRides
rushtotal = rushFare*rushRides

finaltotal = regtotal+rushtotal

print(f'I have spent ${finaltotal: .2f} this month on the bus fares.')


