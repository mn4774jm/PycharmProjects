'''Thomas Mullins
coin_counter.py
Def: Program asks the user for the numbers of coins that they have by type add values up both physical and monetary'''

def main():
    while True:
        try:

            quarters, dimes, nickles, pennies = input1()
            q_total, d_total, n_total, p_total, total_coins, grand_total = processing1(quarters, dimes, nickles, pennies)
            output1(quarters, dimes, nickles, pennies, q_total, d_total, n_total, p_total, total_coins, grand_total)

        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('Welcome to the Coin Counter Program')
    print('How many quarters do you have?')
    quarters = getPosint()
    print('How many dimes do you have?')
    dimes = getPosint()
    print('How many nickles do you have?')
    nickles = getPosint()
    print('How many pennies do you have?')
    pennies = getPosint()
    return quarters, dimes, nickles, pennies

def getPosint():  # ensures "int-able" input over 0
    posInt = input('\tEnter a positive whole number: ')
    while posInt.isnumeric() is False:
        posInt = input('\tPlease enter a whole number: ')
    posInt = int(posInt)
    return posInt

def processing1(quarters, dimes, nickles, pennies):
    q_value = 0.25
    d_value = 0.1
    n_value = 0.05
    p_value = 0.01
    q_total = quarters*q_value
    d_total = dimes*d_value
    n_total = nickles*n_value
    p_total = pennies*p_value
    total_coins = quarters+dimes+nickles+pennies
    grand_total = q_total+d_total+n_total+p_total
    return q_total, d_total, n_total, p_total, total_coins, grand_total

def output1(quarters, dimes, nickles, pennies, q_total, d_total, n_total, p_total, total_coins, grand_total):
    print('\nThe Total Value of Your Coins')
    print('{:<10}{:>15}{:>16}'.format('Coin Type', 'Number', 'Value'))
    print('{:<10}{:^25}{:2}{:>2.2f}'.format('Quarters', quarters,'$', q_total))
    print('{:<10}{:^25}{:2}{:>2.2f}'.format('Dimes', dimes,'$', d_total))
    print('{:<10}{:^25}{:2}{:>2.2f}'.format('Nickles', nickles,'$', n_total))
    print('{:<10}{:^25}{:2}{:>2.2f}'.format('Pennies', pennies,'$', p_total))
    print('{:<10}{:^25}{:2}{:>2.2f}'.format('Total', total_coins,'$', grand_total))

main()