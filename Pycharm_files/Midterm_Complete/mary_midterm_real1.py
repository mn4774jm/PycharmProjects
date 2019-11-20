print('Dragon Adventures - Beijing Tour Estimator')

def main():
    while True:
        try:

            party, beach, host = input1()
            hotel_cost, activities, beach_price, subtotal, host_percent, grand_total = processing1(party, beach, host)
            output1(party, beach, host, hotel_cost, activities, beach_price, subtotal, host_percent, grand_total)

        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('\nHow many people are in your party?')
    party = get_posint()
    print('How many people will go on the optional beach trip? ')
    beach = get_posint()
    print('What percent will go towards host gifts (3-5%)?')
    host = float_regex()
    return party, beach, host

def get_posint():  # request and validate positive integer
    posint = input('\tEnter a whole positive number: ')
    while posint.isnumeric() is False or int(posint) < 0 or int(posint) >= 121:
        posint = input('\tPlease enter a valid number: ')
    posint = float(posint)
    return posint

def float_regex():
    import re
    floatRegex = re.compile(r'(-)?\d+(\.)?(\d+)?')
    regex = input('Enter a numeric value: ')
    mo = floatRegex.search(regex)
    while mo == None or float(regex) < 3 or float(regex) >5:
        regex = input('Enter only numeric values: ')
        mo = floatRegex.search(regex)
    regex = float(regex)
    return regex

def processing1(party, beach, host):
    hotel_cost = party*375.00
    activities = party*150.00
    beach_price = beach*100.00
    subtotal = hotel_cost+activities+beach_price
    host_percent = subtotal*(host/100)
    grand_total = subtotal+host_percent
    return hotel_cost, activities, beach_price, subtotal, host_percent, grand_total

def output1(party, beach, host, hotel_cost, activities, beach_price, subtotal, host_percent, grand_total):
    print('\nHere\'s your Tour Estimate!')
    print('{:<10.0f}{:>5}{:>10}{:>10.2f}'.format(party, 'Hotel stays @ $375 each', '$', hotel_cost))
    print('{:<10.0f}{:>5}{:>8}{:>10.2f}'.format(party, 'Activity Fees @ $150 each','$', activities))
    print('{:<10.0f}{:>5}{:>12}{:>10.2f}'.format(beach, 'Side trips @$100 each', '$', beach_price))
    print('{:<10}{:>33}{:>10.2f}'.format('Subtotal','$', subtotal))
    print('{:<10.1f}{:>5}{:>21}{:>10.2f}'.format(host, 'Gift portion', '$', host_percent))
    print('{:<10}{:>18}{:>10.2f}'.format('Total, excluding air fare', '$', grand_total))


main()


