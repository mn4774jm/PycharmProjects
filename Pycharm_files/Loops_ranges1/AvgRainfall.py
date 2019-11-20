'''Author: Thomas Mullins
Date:2/19/19
AvgRainfall.py
Definition: Write a program that collects rainfall data and calculates the average rainfall for a user-defined number of years.
'''
def main():
    while True:
        try:
            years = input1()
            totalAll, averageAll = processing1(years)
            output1(totalAll, averageAll)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ').upper()
        while answer != 'Y' and answer != 'N':
            answer = input('Please enter Y or N: ').upper()
        if answer == 'N':
            print(f'\nThank for using the program')
            break

def input1():
#Variables outside of loop
    print('Welcome to the Average Rainfall Program.')
    years = input('How many years do you want to track? ')
    while years.isnumeric() is False:
        years = input('Please enter numeric values greater than 1 only: ')
    years = int(years)
    return years

def processing1(years):
    totalAll = 0.0
    months = 12
    #average rain in loop 1
    for avgRain in range(years):
        total = 0.0 #Value to reset rainfall for each iteration
    #header for each year
        print(f'Rainfall info for year #{avgRain + 1}')
    #Input for each month, beginning of loop 2
        for month in range(months):
            rain = float(input(f'\tEnter rainfall for month #{month + 1}: '))
    #tracking totals for individual years and total years
            total += rain
            totalAll += rain
    #Averages for individual years and total years; calculations
        average = total / months
        averageAll = totalAll / years / months
    #print script for yearly totals
        print(f'Total rain in inches for year #{avgRain + 1} = {total: .2f}')
        print(f'Year #{avgRain + 1} monthly Avg rainfall = {average: .2f}')
    return totalAll, averageAll

def output1(totalAll, averageAll):
    #print script for totals/averages for all years; outside loops
    print(f'\nTotal rain, all years = {totalAll: 0.2f}')
    print(f'Average monthly rain, all years = {averageAll: 0.2f}')
    print('Thank you for using the program!')

main()



