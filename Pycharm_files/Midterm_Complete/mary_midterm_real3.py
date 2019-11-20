print('Welcome to the donor management app.')

def main():
    while True:
        try:

            donor_list, donation_list = input1()
            total, max_amount, average = processing1(donation_list)
            output1(donor_list, donation_list, total, max_amount, average)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to enter more donations? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break

def input1():
    donor_list = []
    donation_list = []
    print('First, make a list of today\'s donors.')
    print('\tHit enter twice to end.')
    while True:
        donor = input(f'Donor #{len(donor_list)+1}: ').title()
        if donor != '':
            donor_list.append(donor)
        else:
            break
    print('Now record the amounts donated.')
    for items in range(len(donor_list)):
        print(f'Amount for {donor_list[items]}')
        new_donation = get_posint()
        donation_list.append(new_donation)
    return donor_list, donation_list

def get_posint():  # request and validate positive integer
    posint = input('\tEnter a whole positive number: $ ')
    while posint.isnumeric() is False or int(posint) < 0:
        posint = input('\tPlease enter a valid number: ')
    posint = int(posint)
    return posint

def processing1(donation_list):
    total = sum(donation_list)
    max_amount = max(donation_list)
    average = total/len(donation_list)
    return total, max_amount, average

def output1(donor_list, donation_list, total, max_amount, average):
    print('\nToday\'s Donations')
    for items in range(len(donor_list)):
        print('{:<20}{:>15}{:>10.2f}'.format(f'Amount for {donor_list[items]}', '$', donation_list[items]))
    print('{:<20}{:>15}{:>10.2f}'.format(f'Total', '$', total))
    print('{:<20}{:>15}{:>10.2f}'.format(f'Max', '$', max_amount))
    print('{:<20}{:>15}{:>10.2f}'.format(f'Average', '$', average))
main()


