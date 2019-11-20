

print('Welcome to the personal budget program!')
def main():
    while True:
        try:
            needs_list, cost_list = input1()
            total = processing1(cost_list)
            output1(needs_list, cost_list, total)
        except Exception as err:
            print(err)

        answer = input('\nWould you like to run this program again? Enter Y or N: ')
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Please enter Y or N: ')
        if answer.upper() == 'N':
            print(f'\nThank you for using the program')
            break

def input1():
    needs_list = ['Rent', 'Food', 'Transport', 'Other']
    cost_list = []
    for items in range(len(needs_list)):
        print(f'How much do you spend on {needs_list[items]}?')
        need = get_posint()
        cost_list.append(need)
    return needs_list, cost_list

def get_posint():  # request and validate positive integer
    posint = input('\tEnter a whole positive number: ')
    while posint.isnumeric() is False or int(posint) < 0:
        posint = input('\tPlease enter a valid number: ')
    posint = int(posint)
    return posint

def processing1(cost_list):
    total = 0
    for items in range(len(cost_list)):
        total += cost_list[items]
    return total

def output1(needs_list, cost_list, total):
    print('Here is your overall budget:')
    #loop for needs heading
    for items in range(len(needs_list)):
        print(f'{needs_list[items]:15}', end = '')
    print()#print to andvance to the next line
    for items in range(len(cost_list)):
        #conditional to format first item left alignment
        if items == 0:
            print(f'${cost_list[0]:<14.2f}', end = '')
        else:
            print(f'${cost_list[items]:<14.2f}', end = '')
    print(f'\nYour total monthly budget is ${total:0.2f}')

main()