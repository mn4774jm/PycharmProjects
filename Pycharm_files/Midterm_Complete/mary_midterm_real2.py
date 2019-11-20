print('Thanks for joining us at the MN-helpers gala!')

def main():
    while True:
        try:
            donation, tickets, donar_list = input1()
            recognition, total_cost, ticket_cost = processing1(donation, tickets, donar_list)
            output1(tickets, donation, recognition, ticket_cost, total_cost, donar_list)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    print('How much would you like to donate?')
    donation = get_posint()
    print('How many gala tickets do you need?')
    tickets = get_posint()
    donar_list = input('May we list you as a donar? Enter Y or N: ')
    while donar_list.upper() != 'Y' and donar_list.upper() != 'N':
        donar_list = input('Please enter Y or N only:')
    return donation, tickets, donar_list


def get_posint():  # request and validate positive integer
    posint = input('\tEnter a whole positive number: ')
    while posint.isnumeric() is False or int(posint) < 0:
        posint = input('\tPlease enter a valid number: ')
    posint = int(posint)
    return posint

def processing1(donation, tickets, donar_list):
    if donation >= 1000:
        ticket_cost = 0
        recognition = "Platinum"
    elif donation <1000 and donation >=500:
        ticket_cost = 10
        recognition = 'Gold'
    elif donation <500 and donation >= 100:
        ticket_cost = 15
        recognition = 'Silver'
    elif donation <= 100 and donation >= 0:
        ticket_cost = 20
        recognition = 'Bronze'
    else:
        ticket_cost = 25
        recognition = 'Friend'

    total_cost = tickets*ticket_cost

    return recognition, ticket_cost, total_cost

def output1(tickets, donation, recognition, ticket_cost, total_cost, donar_list):
    print('\nRECEIPT')
    print('{:<0}{:>20}'.format(f'Your gift of ${donation} means a lot!', recognition))
    print('{:<0}{:>10}{:>7.2f}'.format(f'Due at will call: {tickets} tickets @ ${ticket_cost}', '$', total_cost))
    if donar_list == "n":
        print('We won\'t list your name, but thank you for your donation\n')
    else:
        print()
    print('MN-helpers is non-profit. Show receipt to her tax preparer.')

main()