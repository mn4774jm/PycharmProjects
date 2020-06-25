'''
Thomas Mullins
Definition: Write a program that calculates and displays information about a
flight sale from MSP to CHI.
Final1.py
5/9/19
'''
#Define main
import pyinputplus as pyip
def main():
    #Exception handling
    while True:
        try:
            tickets, bags = input1()
            ticket_total, bag_total, total, tax, admin_fee, final_total, final_tax = processing1(tickets, bags)
            output1(ticket_total, bag_total, total, tax, admin_fee, final_total, tickets, bags, final_tax)
        except Exception as err:
            print(err)
        #Repeat function
        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')

        if answer.upper() == 'NO':
            print(f'\nThank for using the program')
            break

def input1():
    #User input
    print('Welcome to Andy\'s Flight Club!')
    print('Limit of 4 tickets & 2 suitcases ($20ea) per passenger.\n')
    tickets = input('Enter the number of tickets up to 4: ')
    #Validation for tickets
    while tickets.isnumeric() is False or int(tickets) >= 5 or int(tickets) == 0:
        tickets = input('\t\tEnter 1, 2, 3, 4 only: ')

    #Validation for bags
    bags = input('Enter the number of suitcases up to 2 per ticket: ')
    bags_allowed = int(tickets)*2
    while bags.isnumeric() is False or int(bags) < 0 or int(bags) > (int(tickets)*2):
        bags = input(f'Enter 0 through {bags_allowed} for your {tickets} tickets:')

    return tickets, bags


def processing1(tickets, bags):
    #Processing all totals
    ticket_total = tickets*123
    ticket_total = float(ticket_total)
    bag_total = bags*20
    bag_total = float(bag_total)
    total = bags+tickets
    tax = 0.075 *total
    final_tax = tax*100
    final_tax = float(final_tax)
    admin_fee = 10 * tickets
    admin_fee = float(admin_fee)
    final_total = total+tax+admin_fee

    return ticket_total, bag_total, total, tax, admin_fee, final_total, final_tax
#User output for all final prices
def output1(ticket_total, bag_total, total, tax, admin_fee, final_total, tickets, bags, final_tax):
    print('\nThanks for using Andy\'s Flight Club Calculator!')
    print('{:<20}{:>13}{:>9.2f}'.format(str(tickets)+'tickets @ $123 each', '$', ticket_total))
    print('{:<20}{:>12}{:>9.2f}'.format(str(bags) + 'suitcases @ $20 each', '$', bag_total))
    print('{:<20}{:>4}{:>9.2f}'.format('7.5% Tax (Tickets & suicases)', '$', final_tax))
    print('{:<20}{:>6}{:>9.2f}'.format('Admin Fees @ $10 per person', '$', admin_fee))
    print('{:<20}{:>6}{:>9.2f}'.format('Totla cost for your journey', '$', final_total))

main()

