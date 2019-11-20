def main():
    while True:
        try:
            needs, costs, total = input1()
            output1(needs, costs, total)
        except Exception as err:
            print(err)

        answer = input('Would you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank for using the program')
            break


def input1():
    needs = ['Rent', 'Food', 'Transport', 'Other']
    costs = []
    total = 0
    print('Welcome to the personal budget program!')
    for items in range(len(needs)):
        print(f'How much did you spend on {needs[items]}?')
        cost = input('\tEnter a positive whole number: ')
        while cost == '0' or cost.isnumeric() is False:
            cost = input('Use a whole number greater than 0: ')
        costs.append(cost)
        cost = int(cost)
        total += cost

    return needs, costs, total

def output1(needs, costs, total):
    print('Here\'s your overall budget:')
    for items in range(len(needs)):
        print('{:15}'.format(needs[items]), end='')
    print()
    for items in range(len(costs)):
        print('${:<14}'.format(costs[items]), end='')
    print()
    print(f'You\'re total monthly budget is ${total:.2f}')

main()